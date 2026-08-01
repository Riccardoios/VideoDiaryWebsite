#!/usr/bin/env python3
"""Lint a videodiary.io article page for the mechanical SEO requirements.

Usage:
    python3 check_article.py website/guides/my-slug.html
    python3 check_article.py website/guides/my-slug.html --site website
    python3 check_article.py path/to/page.html --slug best-video-journaling-apps

Checks the things a human shouldn't have to eyeball: tag lengths, canonical/OG
consistency, JSON-LD validity, tracked CTA, heading structure, contextual link
counts and image alt text. With --site it also checks that the page was wired
into the rest of the site (sitemap, both guide grids, footer, inbound link).

Every prose check is scoped to the <article> element, so the duplicated header,
nav, footer and the JSON-LD block never count as page content.

Judgment calls (is it honest? is it well written?) are not checked here -- see
the pre-ship checklist in references/seo-technical.md.

Exit code is 1 if there is at least one FAIL, otherwise 0.
"""

import argparse
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

APP_ID = "1606008204"
PROVIDER_TOKEN = "pt=121784039"
SITE = "https://videodiary.io"
CT_MAX_LEN = 30  # Apple's campaign token limit

PASS, WARN, FAIL = "PASS", "WARN", "FAIL"
results = []

CHROME_TAGS = {"header", "footer", "nav", "aside"}
SKIP_TEXT_TAGS = {"script", "style", "svg"}


def record(status, check, detail=""):
    results.append((status, check, detail))


class Collector(HTMLParser):
    """Pulls out just what the checks need, tolerant of messy real-world HTML.

    Tracks which region each element is in. The site duplicates its header and
    footer into every page, so "is this inside <article>" is the difference
    between counting real content and counting boilerplate.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self.metas = []            # list of dicts
        self.links = []            # dicts: href, in_article, in_chrome
        self.canonical = None
        self.images = []           # attrs + in_article
        self.headings = []         # (level, text, in_article)
        self._heading_level = None
        self._heading_buf = []
        self._heading_in_article = False
        self.ld_blocks = []
        self._in_ld = False
        self._ld_buf = []
        self.prose = []            # article text only
        self.article_classes = []  # class attr of every element inside <article>

        self._chrome_depth = 0
        self._article_depth = 0
        self._skip_depth = 0

    @property
    def in_article(self):
        return self._article_depth > 0 and self._chrome_depth == 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in CHROME_TAGS:
            self._chrome_depth += 1
        elif tag == "article":
            self._article_depth += 1
        elif tag in SKIP_TEXT_TAGS:
            self._skip_depth += 1

        if self.in_article and a.get("class"):
            self.article_classes.append(a["class"])

        if tag == "title":
            self._in_title = True
            self.title = ""
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            if (a.get("rel") or "").lower() == "canonical":
                self.canonical = a.get("href")
        elif tag == "a":
            self.links.append({
                "href": a.get("href") or "",
                "in_article": self.in_article,
                "in_chrome": self._chrome_depth > 0,
            })
        elif tag == "img":
            self.images.append({**a, "in_article": self.in_article})
        elif tag in ("h1", "h2", "h3"):
            self._heading_level = int(tag[1])
            self._heading_buf = []
            self._heading_in_article = self.in_article
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_ld = True
            self._ld_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3") and self._heading_level is not None:
            self.headings.append((self._heading_level,
                                  "".join(self._heading_buf).strip(),
                                  self._heading_in_article))
            self._heading_level = None
        elif tag == "script" and self._in_ld:
            self.ld_blocks.append("".join(self._ld_buf))
            self._in_ld = False

        if tag in CHROME_TAGS:
            self._chrome_depth = max(0, self._chrome_depth - 1)
        elif tag == "article":
            self._article_depth = max(0, self._article_depth - 1)
        elif tag in SKIP_TEXT_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
        if self._heading_level is not None:
            self._heading_buf.append(data)
        if self._in_ld:
            self._ld_buf.append(data)
        if self.in_article and self._skip_depth == 0:
            self.prose.append(data)

    def meta(self, **match):
        for m in self.metas:
            if all((m.get(k) or "").lower() == v.lower() for k, v in match.items()):
                return m.get("content")
        return None

    def article_text(self):
        return re.sub(r"\s+", " ", "".join(self.prose)).strip()

    def article_links(self):
        return [l["href"] for l in self.links if l["in_article"]]

    def store_links(self):
        return [l for l in self.links
                if f"id{APP_ID}" in l["href"] or "apps.apple.com" in l["href"]]


def parse(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        c = Collector()
        c.feed(f.read())
        return c


# -- page checks ----------------------------------------------------------

def check_head(c, slug, is_guide):
    title = (c.title or "").strip()
    if not title:
        record(FAIL, "title tag", "missing")
    elif len(title) > 60:
        record(WARN, "title length", f"{len(title)} chars -- likely truncated in results (aim <=60)")
    elif len(title) < 25:
        record(WARN, "title length", f"{len(title)} chars -- unusually short")
    else:
        record(PASS, "title length", f"{len(title)} chars")

    desc = c.meta(name="description")
    if not desc:
        record(FAIL, "meta description", "missing")
    else:
        n = len(desc.strip())
        if 140 <= n <= 160:
            record(PASS, "meta description", f"{n} chars")
        else:
            record(WARN, "meta description", f"{n} chars -- target 140-160")

    if not c.canonical:
        record(FAIL, "canonical", "missing")
    elif not is_guide:
        record(PASS, "canonical", c.canonical)
    else:
        expected = f"{SITE}/guides/{slug}"
        if c.canonical == expected:
            record(PASS, "canonical", c.canonical)
        elif c.canonical.rstrip("/").replace(".html", "") == expected:
            record(FAIL, "canonical form",
                   f"{c.canonical} -- must be extensionless, no trailing slash: {expected}")
        else:
            record(FAIL, "canonical", f"{c.canonical} != {expected}")

    og_url = c.meta(property="og:url")
    if not og_url:
        record(WARN, "og:url", "missing")
    elif c.canonical and og_url != c.canonical:
        record(FAIL, "og:url vs canonical", f"{og_url} != {c.canonical}")
    else:
        record(PASS, "og:url vs canonical", "match")

    for prop in ("og:title", "og:description", "og:image", "og:type", "og:site_name"):
        if not c.meta(property=prop):
            record(WARN, f"{prop}", "missing")
    if not c.meta(name="twitter:card"):
        record(WARN, "twitter:card", "missing")


def check_headings(c):
    h1s = [t for lvl, t, _ in c.headings if lvl == 1]
    if len(h1s) == 1:
        record(PASS, "single h1", h1s[0][:70])
    elif not h1s:
        record(FAIL, "single h1", "no h1 found")
    else:
        record(FAIL, "single h1", f"{len(h1s)} h1 tags found")

    h2s = [t for lvl, t, in_art in c.headings if lvl == 2 and in_art]
    if len(h2s) < 3:
        record(WARN, "h2 count in article", f"{len(h2s)} -- thin structure for an SEO page")
    else:
        record(PASS, "h2 count in article", str(len(h2s)))

    question_like = sum(1 for t in h2s if "?" in t or re.match(
        r"^(how|what|which|why|when|is|can|do|should|where|who)\b", t.strip(), re.I))
    if h2s and question_like == 0:
        record(WARN, "question-shaped h2s",
               "none -- these are what get extracted into snippets and quoted by assistants")
    elif h2s:
        record(PASS, "question-shaped h2s", f"{question_like} of {len(h2s)}")


def has_faq_section(c):
    """FAQ detection from the article only -- the nav's 'FAQ' link is not one."""
    if any("faq" in cls.split() for cls in c.article_classes):
        return True
    return any(re.search(r"frequently asked|\bfaq\b", t, re.I)
               for lvl, t, in_art in c.headings if in_art)


def check_jsonld(c):
    if not c.ld_blocks:
        record(FAIL, "JSON-LD", "no application/ld+json block found")
        return
    types = set()
    parsed_ok = 0
    for i, block in enumerate(c.ld_blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            record(FAIL, f"JSON-LD block {i + 1} parses", str(e))
            continue
        parsed_ok += 1
        nodes = data if isinstance(data, list) else [data]
        expanded = []
        for n in nodes:
            expanded.extend(n.get("@graph", [n]) if isinstance(n, dict) else [])
        for n in expanded:
            t = n.get("@type")
            if isinstance(t, list):
                types.update(t)
            elif t:
                types.add(t)
    if parsed_ok == len(c.ld_blocks):
        record(PASS, "JSON-LD parses", f"{parsed_ok} block(s)")
    else:
        record(FAIL, "JSON-LD parses", f"only {parsed_ok} of {len(c.ld_blocks)} block(s) valid")

    if types & {"Article", "BlogPosting", "NewsArticle"}:
        record(PASS, "Article schema", "present")
    else:
        record(FAIL, "Article schema", f"not found (types present: {sorted(types) or 'none'})")

    if "BreadcrumbList" in types:
        record(PASS, "BreadcrumbList schema", "present")
    else:
        record(WARN, "BreadcrumbList schema", "missing")

    if has_faq_section(c) and "FAQPage" not in types:
        record(WARN, "FAQPage schema", "the article has an FAQ section but no FAQPage markup")
    elif "FAQPage" in types:
        record(PASS, "FAQPage schema", "present")


def check_cta(c, slug):
    store = c.store_links()
    if not store:
        record(FAIL, "App Store CTA", "no App Store link on the page")
        return

    hrefs = [l["href"] for l in store]
    untracked = [h for h in hrefs if "ct=" not in h]
    tokens = set(re.findall(r"[?&]ct=([^&\"'\s]+)", " ".join(hrefs)))

    if untracked:
        record(FAIL, "CTA tracking", f"{len(untracked)} App Store link(s) carry no ct= token")
    if "website" in tokens:
        record(FAIL, "CTA token", "uses ct=website -- a new article needs its own slug token on "
                                  "every App Store link, including nav and footer")
    elif tokens and tokens != {slug}:
        record(FAIL, "CTA token", f"token(s) {sorted(tokens)} do not match slug '{slug}'")
    elif tokens:
        record(PASS, "CTA token", f"ct={slug} on all {len(store)} link(s)")

    for t in sorted(tokens):
        if len(t) > CT_MAX_LEN:
            record(WARN, "CTA token length",
                   f"ct={t} is {len(t)} chars -- Apple caps campaign tokens at {CT_MAX_LEN}; "
                   "shorten the token and keep the slug")

    if all(PROVIDER_TOKEN in h for h in hrefs):
        record(PASS, "provider token", PROVIDER_TOKEN)
    else:
        record(WARN, "provider token", f"some App Store links are missing {PROVIDER_TOKEN}")

    in_article = [l for l in store if l["in_article"]]
    if not in_article:
        record(FAIL, "in-article CTA",
               "no App Store link inside <article> -- the contextual CTA is missing")
    elif len(in_article) > 2:
        record(WARN, "in-article CTA", f"{len(in_article)} -- one at peak conviction is the intent")
    else:
        record(PASS, "in-article CTA", str(len(in_article)))

    if len(store) > 5:
        record(WARN, "CTA count", f"{len(store)} App Store links -- 4 is the page's baseline "
                                  "(nav, article, download band, footer)")
    else:
        record(PASS, "CTA count", f"{len(store)} total")


def check_links_and_images(c, slug):
    body = [h for h in c.article_links()
            if (h.startswith("/") or SITE in h)
            and not h.startswith("#")
            and "apps.apple.com" not in h]
    unique = {h.rstrip("/") for h in body}
    unique.discard(f"/guides/{slug}")
    if len(unique) >= 3:
        record(PASS, "contextual internal links", f"{len(unique)} unique inside <article>")
    else:
        record(FAIL, "contextual internal links",
               f"{len(unique)} inside <article> -- 3+ required (nav and footer links don't count)")

    if not c.images:
        record(WARN, "images", "no images on the page")
    else:
        missing_alt = [i.get("src", "?") for i in c.images if not (i.get("alt") or "").strip()]
        if missing_alt:
            record(FAIL, "image alt text", f"{len(missing_alt)} image(s) missing alt: {missing_alt[:3]}")
        else:
            record(PASS, "image alt text", f"all {len(c.images)} images have alt text")
        if not any(i["in_article"] for i in c.images):
            record(WARN, "article screenshot", "no image inside <article> -- one screenshot is expected")


def check_body(c):
    text = c.article_text()
    words = len(text.split())
    if not words:
        record(FAIL, "article body",
               "no <article> element found -- the page structure doesn't match the site")
        return
    if words < 700:
        record(WARN, "word count", f"~{words} -- thin for a commercial-intent page")
    elif words > 3500:
        record(WARN, "word count", f"~{words} -- check for padding")
    else:
        record(PASS, "word count", f"~{words}")

    slop = ["in today's fast-paced", "in today's digital", "delve into", "it's important to note",
            "in conclusion", "look no further", "game-changing", "revolutionize",
            "in the ever-evolving", "unlock the power"]
    hits = [p for p in slop if p in text.lower()]
    if hits:
        record(WARN, "AI-slop phrases", ", ".join(hits))
    else:
        record(PASS, "AI-slop phrases", "none found")

    m = re.search(r"quick answer", text, re.I)
    if not m:
        record(WARN, "quick answer block", "missing -- this is the element assistants quote")
    else:
        position = m.start() / max(len(text), 1)
        if position > 0.35:
            record(WARN, "quick answer position",
                   f"{int(position * 100)}% into the article -- it belongs above the fold")
        else:
            record(PASS, "quick answer block", f"{int(position * 100)}% into the article")


def check_visible_date(path):
    """The byline sits in .article-hero, outside <article>, so scan that block."""
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()
    hero = re.search(r'<div class="article-hero">(.*?)</main>', html, re.S)
    scope = hero.group(1) if hero else html
    pattern = r"updated\s+\w+\s+20\d\d"
    if re.search(pattern, scope.split("<article")[0], re.I):
        record(PASS, "visible date", "present in the hero byline")
    elif re.search(pattern, html, re.I):
        record(WARN, "visible date", "present, but not in the hero byline")
    else:
        record(FAIL, "visible date", "no visible 'Updated <Month Year>' line")


# -- site wiring checks ---------------------------------------------------

def check_wiring(site_dir, slug, page_path):
    url_path = f"/guides/{slug}"
    abs_url = f"{SITE}/guides/{slug}"

    sitemap = os.path.join(site_dir, "sitemap.xml")
    if not os.path.isfile(sitemap):
        record(WARN, "sitemap.xml", f"not found at {sitemap}")
    else:
        with open(sitemap, encoding="utf-8") as f:
            content = f.read()
        if f"<loc>{abs_url}</loc>" in content:
            record(PASS, "sitemap entry", abs_url)
        else:
            record(FAIL, "sitemap entry", f"no <loc>{abs_url}</loc> in sitemap.xml")

    guides_index = os.path.join(site_dir, "guides", "index.html")
    if not os.path.isfile(guides_index):
        record(WARN, "guides index", f"not found at {guides_index}")
    else:
        with open(guides_index, encoding="utf-8") as f:
            content = f.read()
        if f'class="guide-card" href="{url_path}"' in content:
            record(PASS, "guides index card", url_path)
        else:
            record(FAIL, "guides index card", f"no guide-card linking to {url_path}")
        if abs_url in content.split("</head>")[0]:
            record(PASS, "guides index hasPart", "listed in the CollectionPage JSON-LD")
        else:
            record(FAIL, "guides index hasPart",
                   f"{abs_url} missing from the CollectionPage hasPart array")

    home = os.path.join(site_dir, "index.html")
    if os.path.isfile(home):
        with open(home, encoding="utf-8") as f:
            content = f.read()
        if f'class="guide-card" href="{url_path}"' in content:
            record(PASS, "homepage grid card", url_path)
        else:
            record(WARN, "homepage grid card",
                   f"no card for {url_path} -- the homepage grid lists every guide today")

    pages = sorted(glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True))
    missing_footer = []
    for p in pages:
        with open(p, encoding="utf-8", errors="replace") as f:
            parts = f.read().split('<footer class="site-footer">')
        if len(parts) < 2 or f'href="{url_path}"' not in parts[1]:
            missing_footer.append(os.path.relpath(p, site_dir))
    if missing_footer:
        record(FAIL, "footer guides list",
               f"{len(missing_footer)} of {len(pages)} pages missing the link: {missing_footer[:4]}")
    else:
        record(PASS, "footer guides list", f"present in all {len(pages)} pages")

    inbound = []
    for p in pages:
        rel = os.path.relpath(p, site_dir)
        if os.path.samefile(p, page_path) or os.path.basename(p) == "index.html":
            continue
        if any(h.rstrip("/") == url_path for h in parse(p).article_links()):
            inbound.append(rel)
    if inbound:
        record(PASS, "inbound body link", ", ".join(inbound[:3]))
    else:
        record(FAIL, "inbound body link",
               "no existing guide links to this page from its body -- without one the page gets "
               "almost no crawl equity")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="path to the article HTML file")
    ap.add_argument("--slug", help="expected article slug (defaults to the filename)")
    ap.add_argument("--site", help="site root (e.g. 'website') -- adds the wiring checks")
    args = ap.parse_args()

    if not os.path.isfile(args.path):
        print(f"error: {args.path} is not a file", file=sys.stderr)
        return 2

    slug = args.slug
    if not slug:
        parent = os.path.basename(os.path.dirname(os.path.abspath(args.path)))
        base = os.path.splitext(os.path.basename(args.path))[0]
        slug = parent if base == "index" else base

    is_guide = "guides" in os.path.abspath(args.path).split(os.sep)

    c = parse(args.path)

    check_head(c, slug, is_guide)
    check_headings(c)
    check_jsonld(c)
    check_cta(c, slug)
    check_links_and_images(c, slug)
    check_body(c)
    check_visible_date(args.path)
    if args.site:
        check_wiring(args.site, slug, args.path)

    width = max(len(chk) for _, chk, _ in results) + 2
    icons = {PASS: "ok  ", WARN: "warn", FAIL: "FAIL"}
    print(f"\n{os.path.basename(args.path)}  (slug: {slug})\n" + "-" * 78)
    for status, check, detail in results:
        print(f"  [{icons[status]}] {check.ljust(width)}{detail}")

    fails = sum(1 for s, _, _ in results if s == FAIL)
    warns = sum(1 for s, _, _ in results if s == WARN)
    print("-" * 78)
    print(f"  {len(results) - fails - warns} passed, {warns} warnings, {fails} failures\n")
    if fails:
        print("  Fix the failures before shipping. Warnings are judgment calls.\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
