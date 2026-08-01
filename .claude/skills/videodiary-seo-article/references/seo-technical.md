# Technical SEO and site wiring

Everything here is verified against `website/` as it actually is. Copy, don't improvise.

## Contents
- Head block
- JSON-LD
- CTA tracking
- Internal linking (including the inbound step)
- The seven wiring touch points
- Images
- Pre-ship checklist

---

## Head block

Copy the head of the most recent file in `website/guides/` and change the values. The shape, in order:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>…</title>
<meta name="description" content="…">
<link rel="canonical" href="https://videodiary.io/guides/<slug>">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Video Diary">
<meta property="og:title" content="…">
<meta property="og:description" content="…">
<meta property="og:url" content="https://videodiary.io/guides/<slug>">
<meta property="og:image" content="https://videodiary.io/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="…">
<meta name="twitter:description" content="…">
<meta name="twitter:image" content="https://videodiary.io/assets/og-image.png">
```

| Tag | Rule |
|---|---|
| `<title>` | ≤ 60 characters. Lead with the target phrase, phrased the way people search it. |
| `<meta name="description">` | 140–160 characters. Ad copy, not a summary. Include the target phrase naturally. |
| `<link rel="canonical">` | **`https://videodiary.io/guides/<slug>` — no `.html`, no trailing slash.** Cloudflare Pages serves the flat `<slug>.html` file at the extensionless URL; a canonical with `.html` points at a URL the site doesn't advertise anywhere else. |
| `og:url` | Byte-identical to the canonical. |
| `og:title` / `og:description` | May differ from the title tag; write for a shared link. |
| `og:image` / `twitter:image` | `https://videodiary.io/assets/og-image.png` unless a page-specific image exists. |

Title formulas that fit this site's shapes:
- `Best <category> Apps for iPhone (<Year>)`
- `<App A> vs <App B>: Which <category> App Wins?`
- `<N> <App> Alternatives That Actually <benefit>`
- `How to <do thing>: A <adjective> Guide`

## JSON-LD

The site uses **one `<script type="application/ld+json">` block containing a top-level array**, `Article` first and `BreadcrumbList` second. Keep that shape — the guides index uses `CollectionPage` and the homepage uses `SoftwareApplication` + `FAQPage`, so array-of-nodes is the house style, not `@graph`.

Always present:

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "…",
    "description": "…",
    "image": "https://videodiary.io/assets/og-image.png",
    "author":    { "@type": "Person", "name": "Riccardo Carlotto" },
    "publisher": { "@type": "Person", "name": "Riccardo Carlotto" },
    "datePublished": "2026-07-31",
    "dateModified": "2026-07-31",
    "mainEntityOfPage": "https://videodiary.io/guides/<slug>"
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home",   "item": "https://videodiary.io/" },
      { "@type": "ListItem", "position": 2, "name": "Guides", "item": "https://videodiary.io/guides/" },
      { "@type": "ListItem", "position": 3, "name": "<breadcrumb label>", "item": "https://videodiary.io/guides/<slug>" }
    ]
  }
]
```

The position-3 `name` must match the visible breadcrumb text exactly.

Add further array entries when the page has the matching section:
- **`FAQPage`** whenever there's an FAQ. Question and answer text must match the visible `<details>` content word for word — mismatched markup is a manual-action risk, not a clever trick.
- **`ItemList`** on roundups, listing the apps in the order they appear on the page.
- **`SoftwareApplication`** where the page is substantially about Video Diary. Include `aggregateRating` only if the rating is verified current *and* visible on the page — and remember it rests on 24 ratings.

Dates are `YYYY-MM-DD`. `datePublished` never changes after publication; bump `dateModified` only when the content actually changed.

## CTA tracking

```
https://apps.apple.com/app/apple-store/id1606008204?pt=121784039&ct=<article-slug>&mt=8
```

In HTML, with escaped ampersands, exactly as every existing page writes it:

```html
href="https://apps.apple.com/app/apple-store/id1606008204?pt=121784039&amp;ct=my-slug&amp;mt=8"
```

**On a new article, all four App Store links carry that article's token** — the nav "Get the app" button, the in-body CTA, the download band, and the footer download link. The page is the traffic source whichever link the reader taps, so one token per page keeps the App Store Connect report readable.

The homepage and the existing guides use `ct=website`. **Leave them alone** — rewriting them resets their campaign history for no gain.

Tokens are short, lowercase, hyphenated, identical to the slug, and stable forever: this is the identifier in analytics. Record the token/article pairing wherever the user tracks content.

**Two things about how `ct` actually behaves:**

- **30-character limit.** Apple caps the campaign token. Most slugs fit — `best-video-journaling-apps` is 26 — but a long one won't: `video-journaling-for-mental-health` is 34. When the slug is too long, shorten the token (`video-journaling-mental-health`) and keep the slug intact. Once chosen it can never change, so pick it deliberately. The linter warns above 30.
- **No App Store Connect setup is needed.** `pt=121784039` is the account's provider token and never changes; the `ct` is just a string. App Store Connect creates the campaign row on its own once a link accumulates roughly **5 first-time downloads from distinct Apple IDs**, after about 24 hours. Apple's help page documents only the create-it-in-App-Store-Connect flow, so this is relied-upon behaviour rather than a guarantee — pre-creating the campaign under App Analytics → Acquisition → Campaigns is optional insurance and doesn't change the URL you ship.

## Internal linking

**Outbound (from the new page):** at least three links to related guides, inside sentences where they're genuinely useful — `<a href="/guides/private-video-diary">keeping a private video diary</a>`, never "click here". They must be in the article body; the footer's eight guide links don't count, and the linter ignores them.

**Inbound (to the new page):** at least one contextual body link added to an existing, topically related guide. This is the step that actually matters — a page with no inbound links gets almost no share of the site's authority — and it's the step that gets skipped.

## The seven wiring touch points

A new guide is not one file edit. All seven, in the same change:

| # | File | Edit |
|---|---|---|
| 1 | `website/guides/<slug>.html` | the new page |
| 2 | `website/sitemap.xml` | new `<url>` block before `</urlset>`: `<loc>https://videodiary.io/guides/<slug></loc>`, `<lastmod>` today, `<changefreq>monthly</changefreq>`, `<priority>0.8</priority>` for Tier 1 / `0.7` otherwise. Two-space indent, matching the existing entries. |
| 3 | `website/guides/index.html` | an `<a class="guide-card">` in the `.guide-grid` |
| 4 | `website/guides/index.html` | **also** an entry in the `CollectionPage` `hasPart` array in the head — easy to miss |
| 5 | `website/index.html` | a matching `.guide-card` in the homepage `.guide-grid` (it currently lists all eight guides) |
| 6 | **every** HTML file under `website/` | one `<li>` in the footer `<h3>Guides</h3>` list. There are no partials — the footer is duplicated in `index.html`, `guides/index.html` and all eight guides, so this is ten files. |
| 7 | one existing guide | the inbound contextual body link |

`robots.txt` needs no change. There is no RSS feed and no `llms.txt`.

Card markup, identical in both grids:

```html
<a class="guide-card" href="/guides/<slug>">
  <h3><card title></h3>
  <p><one sentence, roughly twelve words></p>
  <span class="go">Read the guide →</span>
</a>
```

`hasPart` entry:

```json
{ "@type": "Article", "headline": "<card title>", "url": "https://videodiary.io/guides/<slug>" }
```

## Images

- Reuse the existing screenshots — `/assets/screenshot-1.png` … `-4.png`, all 1284×2778. `app.md` lists what each one shows; pick the one that matches the section it sits in.
- Markup: `<img class="shot-inline" src="/assets/screenshot-N.png" alt="…" width="1284" height="2778" loading="lazy">`. Explicit dimensions prevent layout shift; `loading="lazy"` is right for anything below the fold, which in practice is every in-article image.
- Alt text describes what is actually visible, in plain language, with the target phrase only where it fits naturally. Keyword-stuffed alt text is a negative signal and it's user-hostile.

## Pre-ship checklist

Run the linter from the repo root:

```bash
python3 .claude/skills/videodiary-seo-article/scripts/check_article.py website/guides/<slug>.html --site website
```

Then eyeball what it can't judge:

- [ ] The complete answer to the target query is above the fold
- [ ] At least one competitor is credited with beating Video Diary at something real
- [ ] No fabricated numbers, quotes, or study citations anywhere
- [ ] Any Premium-only feature is labelled as Premium
- [ ] Every competitor fact was verified today, not recalled
- [ ] The article reads like a person with an opinion wrote it
- [ ] No section could be deleted without loss
- [ ] `ct=` token is the article slug and is recorded somewhere
- [ ] Renders correctly at 390px — most of this traffic is on a phone
