# Article templates

Two parts: the page skeleton, which is this site's actual markup and should be copied literally, and three content shapes, which are skeletons to adapt. A page that reads like a template got filled in will lose to one that reads like a person wrote it.

---

## The page skeleton

Every guide is a full standalone document — header and footer are duplicated, there are no partials. Copy the newest file in `website/guides/` and replace the middle. Body order:

```
<header class="site-header">        ← verbatim, only the nav CTA's ct= token changes
<main>
  <div class="article-hero">        ← breadcrumbs, h1, byline
  <article class="guide">           ← the whole article
  <aside class="related">           ← 3 guide cards
  <section class="download-band">   ← closing CTA
</main>
<footer class="site-footer">        ← verbatim + the new guide's <li>
```

**Hero.** The only h1 on the page. Sentence case, unlike the title tag.

```html
<div class="article-hero">
  <div class="wrap">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/guides/">Guides</a> › <short label></nav>
    <h1><the h1></h1>
    <p class="meta">By Riccardo Carlotto · Updated <Month Year></p>
  </div>
</div>
```

Existing guides write the `.meta` line as a topic plus date ("Video journaling guide · Updated July 2026"). Named authorship gets cited more by assistants than an anonymous page, so new articles use the byline form above. There is no about page — the name is plain text, not a link.

**Quick answer.** The site's `.tip` block. Existing guides put it at the *bottom*; that's backwards, because it's the element Google lifts for a snippet and assistants quote. **Put it directly after the opening answer paragraph, at the top of `<article>`.** Deliberate departure, not an oversight.

```html
<div class="tip"><strong>Quick answer:</strong> <2–4 sentences that stand alone when quoted out of context.></div>
```

**Comparison table.** Wrap it — the wrapper is what keeps a five-column table from breaking the layout on a phone.

```html
<div class="table-wrap">
<table>
  <thead><tr><th>App</th><th>Best for</th><th>Price</th><th>Platforms</th></tr></thead>
  <tbody>
    <tr><td>…</td><td>…</td><td>…</td><td>…</td></tr>
  </tbody>
</table>
</div>
```

**In-context CTA.** The `.app-callout` block, placed where conviction peaks:

```html
<div class="app-callout">
<h2>…</h2>
<p>…</p>
<p><a href="https://apps.apple.com/app/apple-store/id1606008204?pt=121784039&amp;ct=<slug>&amp;mt=8">Try Video Diary free</a> …</p>
</div>
```

**Screenshot.** `<img class="shot-inline" src="/assets/screenshot-N.png" alt="…" width="1284" height="2778" loading="lazy">` — see `seo-technical.md`.

**FAQ.** Same `<details>` pattern as the homepage, inside the article. Text must match the `FAQPage` JSON-LD word for word.

```html
<h2>Frequently asked questions</h2>
<div class="faq">
  <details>
    <summary><question></summary>
    <div class="answer">
      <p><answer, 40–60 words></p>
      <a class="learn-more" href="/guides/<related-slug>">Learn more: <topic> →</a>
    </div>
  </details>
</div>
```

The `.answer` wrapper is required — the padding lives on it, not on `details`. The optional `.learn-more` link is how the homepage FAQ feeds the guides; it doubles as one of the three contextual internal links.

**Related aside** — exactly three cards, and the anchor text should differ from the card titles used in the grids so the link graph isn't three copies of the same phrase:

```html
<aside class="related">
  <h2>Keep reading</h2>
  <div class="guide-grid">
    <a class="guide-card" href="/guides/<slug>">
      <h3>…</h3><p>…</p><span class="go">Read the guide →</span>
    </a>
    …
  </div>
</aside>
```

**Download band** — copy verbatim from an existing guide, including the inline SVG badge; only the `ct=` token changes.

Available classes: `.wrap .article-hero .breadcrumbs .meta .guide .tip .app-callout .shot-inline .faq .related .guide-grid .guide-card .go .download-band .store-badge .section-alt .steps .step`. Anything else needs new CSS — say so rather than inventing a class that renders unstyled.

---

## 1. Roundup — "best X apps"

The highest-value shape. Target: someone comparing options right now.

```
H1: Best <category> apps for <platform> in <year>
Byline · Updated <Month Year>

[Direct answer, 2–4 sentences]  →  then the .tip Quick answer block
Name the top pick, name the runner-up for a different need, state the
criteria in one clause. This paragraph must stand alone if quoted.

H2: How I judged these
  4–6 criteria, each one sentence. Criteria must be things a reader
  can verify themselves, not things that happen to describe Video Diary.
  This section is what separates a real roundup from an ad.

H2: The apps
  H3: <App 1>
      Best for: <one specific person>
      2–3 paragraphs: what it does well, who it's wrong for, price.
  H3: <App 2> ... (4–7 apps total, including Video Diary in position,
      not automatically first)

H2: Comparison table          → .table-wrap
  Rows = apps, columns = the criteria from above. Real values only.
  This table is the most-quoted element on the page — assistants parse
  it, and it earns the featured snippet.

H2: Which one should you pick
  Branch by reader type: "If you want X, pick A. If you want Y, pick B."
  Video Diary appears here as the honest answer for the readers it
  genuinely fits, not as the answer for everyone.

[.app-callout CTA]

H2: Frequently asked questions   → .faq details, mirrored in FAQPage JSON-LD
  3–5 real questions, each answered in 40–60 words.

[aside.related — 3 cards]
```

Rules that make or break this shape:
- **Include apps that beat Video Diary at something.** A roundup where the author's own app wins every category is transparently an ad and will not rank or be cited.
- **Position Video Diary honestly.** If it's the best pick for "private, video-first, one-tap", say that, and say who it's not for.
- **No fake scoring.** Don't invent 8.7/10 ratings.
- Add `ItemList` JSON-LD in the apps' page order.

---

## 2. Comparison / alternatives — "X vs Y", "alternatives to X"

Target: someone using a specific app, or evaluating one, and looking for a reason to move or stay.

```
H1: <App A> vs <App B>: which <category> app should you use?
    (or) <N> <App A> alternatives worth trying in <year>

[Direct answer, 2–4 sentences]  →  then the .tip Quick answer block
Say which one wins for which reader, immediately. Withholding the verdict
to "build suspense" just sends people back to the results page.

H2: The short version
  A 4–6 row table in .table-wrap. Reader should be able to leave here
  satisfied.

H2: Where <App A> is better
  Real, specific, no hedging. If you're comparing against Video Diary,
  this section is what makes the rest believable.

H2: Where <App B> is better

H2: The thing they handle differently: <the actual decision axis>
  Usually one dimension really drives the choice — privacy model,
  clip-length constraint, text vs video, price structure. Go deep on it.
  This section is the reason the page exists and where the reader decides.

H2: Who should switch, and who shouldn't
  Explicit permission to stay with the other app. Costs a few downloads,
  earns the credibility that produces the rest.

[.app-callout CTA]
H2: Frequently asked questions
[aside.related]
```

For "alternatives to X" pages the reader arrives already dissatisfied — name the specific frustration in the opening (price change, constraint, cloud processing, discontinued feature) and the page immediately reads as written by someone who understands the problem.

---

## 3. How-to guide

Target: a process query. Lower commercial intent — use these to build topical authority and to funnel internal links toward roundups and comparisons.

```
H1: How to <do the thing>
Byline · Updated <Month Year>

[Direct answer]  →  .tip Quick answer block
The complete short answer in 3–5 sentences or a numbered list. Yes, this
means someone can leave immediately. The ones who stay are the ones who
were going to convert anyway, and this is what earns the snippet.

H2: What you need
H2: Step 1 … Step N        → the site has .steps / .step markup for these
  Each step: what to do, then why it matters, then the failure mode.
  The failure mode is the part every competing article omits.
H2: How to make it stick   ← for habit-shaped topics; this is where the
  product becomes relevant without being sold
H2: Common mistakes
[.app-callout — soft, tool-in-context, not a pitch]
H2: Frequently asked questions
[aside.related — link up to a Tier 1 roundup or comparison]
```

Keep the product mention proportionate. In a how-to, the reader hasn't asked for a recommendation, and a hard sell mid-tutorial reads as bait. One in-context mention plus the download band is enough.

---

## Elements common to all three

**Quick answer block.** The single highest-leverage element for both featured snippets and assistant citations, because it's designed to be lifted whole. Top of the article, not the bottom.

**Byline and date.** `By Riccardo Carlotto · Updated <Month Year>`. Undated content gets cited less by assistants and trusted less by readers. Keep the visible month in sync with `dateModified`.

**Screenshot with real alt text.** Reuse `/assets/screenshot-1.png` … `-4.png`; `app.md` says what each shows.

**Internal links.** Three outbound minimum in the body, inside relevant sentences. Plus at least one *inbound* link added to an existing page — see `seo-technical.md`.

**Two article CTAs.** One `.app-callout` where conviction peaks, one `.download-band` at the end. The nav and footer links are chrome and don't count against that — but all four carry the article's `ct=` token. See `persuasion.md` for placement.

---

## Opening lines: what works and what doesn't

Bad — throat-clearing, delays the answer, could be about any app:
> In today's fast-paced digital world, keeping a journal has never been more important. With so many apps available, choosing the right one can feel overwhelming. In this comprehensive guide, we'll explore the best options.

Good — answers immediately, specific, has a point of view:
> If you want a video journal you'll still be using in six months, the deciding factor isn't features — it's how many taps stand between opening the app and recording. Five apps here get that right in different ways. One of them is mine, and I'll tell you where it loses.

The second one also does something the first can't: it's quotable out of context, which is how a page gets cited.
