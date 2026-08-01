---
name: videodiary-seo-article
description: Research, write, and publish SEO and AI-citation optimized marketing articles for the Video Diary app site (videodiary.io) that convert organic search traffic into App Store downloads. Use this skill whenever the user mentions writing a blog post, guide, article, roundup, comparison, or "alternatives" page for Video Diary or videodiary.io; whenever they mention SEO, keywords, organic traffic, Search Console, content marketing, or getting cited by ChatGPT/Claude for the app; and whenever they want to grow downloads through content instead of paid ads. Also use it when they want to refresh, rewrite, or improve an existing guide on the site, or when they ask what to write next.
---

# Video Diary SEO article pipeline

## What this skill is for

Video Diary makes money when someone taps the App Store link. Content is the cheapest channel to get them there, but only one kind of content actually does it: pages that reach people who are **already shopping for an app like this one**.

The trap to avoid is writing "helpful, educational" posts and calling it marketing. Those pages get impressions and no clicks — Google answers the question in the SERP, an AI assistant reads out the answer, and nobody visits. A page can rank and be commercially worthless.

So the job here is: find a query with buying intent → research it honestly → write something genuinely better than the listicle farms → structure it so both Google and AI assistants can cite it → ship it into the repo with the CTA tracked so its downloads can be attributed.

Work through the phases below in order. Don't skip Phase 1 — writing the wrong article well is the main failure mode.

## The repo

Verified layout — don't re-derive it, but do open a real page before writing:

| | |
|---|---|
| Site root | `website/` (deployed to Cloudflare Pages, no build step, no template engine) |
| New article | `website/guides/<slug>.html` — a flat file, **not** `<slug>/index.html` |
| Canonical URL | `https://videodiary.io/guides/<slug>` — no `.html`, no trailing slash |
| Facts source | `app.md` at the repo root — App Store listing, pricing, screenshots, keyword map |
| Styles | `website/css/style.css`, hand-authored; class names are listed in `references/article-templates.md` |
| Linter | `.claude/skills/videodiary-seo-article/scripts/check_article.py` |

Always mirror the most recently modified file in `website/guides/` for structure. If you are working without the repo on disk (a Claude.ai chat), produce one self-contained page in the same structure plus a paste-in checklist of the wiring edits in `references/seo-technical.md`.

## Phase 1 — Pick the target query

Never start writing from a topic. Start from a query someone types when they are close to downloading something.

**The intent test.** Before committing, answer these three:

1. *Has this person already decided they want an app?* "Best video journaling apps" — yes. "What is a video diary" — no, they want a definition, and Google will hand it to them without a click.
2. *Does answering it require a page, or a sentence?* If the complete answer fits in a featured snippet, the click never happens. Comparisons, roundups, and "how do I actually do this" walkthroughs need a page. Definitions and single facts don't.
3. *Can this site plausibly rank?* An indie app site beats content farms on specificity and first-hand experience, not on domain authority. Long-tail and honestly-opinionated beats broad and generic.

Read `references/keyword-strategy.md` for the scoring rubric, a seeded list of candidate queries for this app, and the cannibalization check against pages that already exist on videodiary.io. **Always run the cannibalization check** — the site already has eight guides and a second page targeting the same intent will split rankings rather than add them.

If the user named a topic, still run it through the intent test and say so plainly if it looks like an impressions-only page. Offer the nearest commercial-intent variant instead. If they want it anyway, write it — just make sure they chose it knowingly.

**Checkpoint.** Before drafting, show the user a five-line brief: target query, why it passes the intent test, article type, the working title, and where the file will live. Keep it short — this is a sanity check, not a proposal document. Skip the checkpoint only if the user has said to run end-to-end without stopping.

## Phase 2 — Research before writing

Content farms write from memory. That's why they're bad, and it's the gap to exploit.

- **Read `app.md` first.** It is the repo's source of truth for the App Store listing: rating and rating count, IAP prices, compatibility, languages, screenshot captions, and the keyword map. `references/product-brief.md` interprets those facts — it does not replace them. Where the two disagree, `app.md` wins.
- **Verify every competitor claim.** Search the web and check current App Store listings for any app being described. Never state a competitor's price, platform, or feature set from recall — those change, and a wrong claim is both a credibility loss and a legal irritant.
- **Verify Video Diary's own current numbers.** Rating, rating count, prices, and OS requirements drift; `app.md` was compiled 2026-07-14. Re-check anything you're about to put on the page.
- **Look at what currently ranks** for the query. Not to copy it — to find what every result is missing. Usually it's first-hand specificity: nobody has actually used the apps.
- **Collect real evidence** where the article makes a claim about journaling benefits: cite named studies or don't make the claim. Invented statistics are the single fastest way to lose both reader trust and AI-assistant citations.

## Phase 3 — Structure

Pick the template from `references/article-templates.md`:

- **Roundup** — "best X apps" queries. Multiple apps, honest scoring criteria, Video Diary as one entry.
- **Comparison / alternatives** — "X vs Y", "alternatives to X". Head-to-head on attributes that matter.
- **How-to guide** — process queries where the answer genuinely needs steps. Lower commercial intent; use these to build topical authority and internal links toward the money pages, not as traffic bets in themselves.

Placement: everything goes in `/guides/`. That is the only content section the site has — the header nav, the footer list, the homepage grid and the guides index all enumerate it. There is no `/blog/`; adding one means new nav, footer, sitemap and index wiring on every page, so don't create it as a side effect of writing an article. Propose it separately if the user wants dated, news-shaped posts.

Outline before drafting. Every H2 should be phrased close to how a person would ask it — that is what gets extracted into featured snippets and quoted by assistants.

## Phase 4 — Write

**Voice.** First person, from the developer who built the app. That is a real advantage over content farms and it should be visible: specific numbers, specific tradeoffs, opinions that could be wrong. Match the existing site register — warm, plain, unhurried, no hype. Read `references/product-brief.md` for the voice sample and vocabulary.

**Answer first.** The complete answer to the query goes above the fold, in the first paragraph or a short "Quick answer" block. No throat-clearing intro, no "in today's fast-paced world", no explaining why the topic matters. Readers who get their answer immediately stay longer, not less — and assistants quote the top of the page.

**Be honest about competitors, including where they beat Video Diary.** This is not a concession, it is the mechanism. A roundup that names five apps and says which one is better for which person is useful, so it ranks and it gets cited. A page that pretends the alternatives don't exist is an ad, and both readers and ranking systems can tell. `references/product-brief.md` lists Video Diary's genuine weaknesses — use them.

**Apply persuasion, don't fake it.** Read `references/persuasion.md`. The short version: the reader's real fear is not "is this app good", it's "will I actually keep this up" and "will I lose these years". Write to that. Use concrete specifics over superlatives, identity over feature lists, and one contextual CTA at the point of peak conviction plus one at the end. Never fabricate urgency, scarcity, review counts, or statistics.

**Avoid the AI-slop tells** — they cost rankings now that everyone recognizes them: no filler openers, no "delve", no three-item lists where two items are padding, no section that restates the previous section, no uniform sentence length, no conclusion that summarizes what was just said. Cut any sentence that would survive deletion.

Length follows the query: most roundups and comparisons land between 1,200 and 2,000 words. Don't pad to a target.

## Phase 5 — Publish

**Mirror the repo, don't invent a format.** Open the most recently modified file in `website/guides/` and copy its exact structure: doctype, head tags, header/nav, breadcrumbs, `<article class="guide">`, related aside, download band, footer. Every guide is a full standalone page — there are no partials, so the header and footer are copied verbatim into the new file.

Then work through `references/seo-technical.md`, which covers:
- head tags: title ≤60 chars, meta description 140–160, extensionless canonical, OG and Twitter cards
- JSON-LD: the site's top-level array of Article + BreadcrumbList, plus FAQPage and ItemList where the page has those sections
- the CTA links, which on a **new article** all carry `pt=121784039&ct=<article-slug>` so App Store Connect can attribute installs per article — this is how the article's actual value gets measured. Existing pages stay on `ct=website`; don't rewrite them.
- internal links: at least three outbound to related pages **and at least one inbound link added to an existing page**, which is the step most often skipped and the one that actually gets the new page crawled
- the seven wiring touch points: sitemap, guides index card, guides index JSON-LD `hasPart`, homepage grid, the footer guides list **in every page**, inbound body link, robots.txt (usually unchanged)
- image alt text

Finish by running the linter from the repo root:

```bash
python3 .claude/skills/videodiary-seo-article/scripts/check_article.py website/guides/<slug>.html --site website
```

`--site` adds the wiring checks; without it only the page itself is linted.

It checks the mechanical things — tag lengths, JSON-LD validity, tracked CTA, link counts, alt text — so review time goes to the writing instead. Fix anything it flags before handing the page over.

## Phase 6 — After publishing

Tell the user, briefly:
- that the article's App Store campaign shows **nothing at all** until it has about 24 hours and roughly 5 first-time downloads from distinct Apple IDs. An empty campaign row in week one is the expected state, not a broken link — don't report it as a failure, and don't "fix" it by changing the token.
- what to watch in Search Console: **clicks, not impressions**. A page at 4,000 impressions and 13 clicks isn't "almost there", it's targeting the wrong intent and should be re-aimed or dropped.
- that a ranking drop is an edit note, not a death sentence — rewriting the page to answer the query better beats publishing a replacement.
- that results are slow: pages written this month are the ones producing traffic three months from now. No article is judged in week one.
- that AI-assistant referrals (ChatGPT, Claude, Perplexity) show up as direct or referral traffic in most analytics defaults and get badly undercounted — check raw referrer source instead.

Offer to log the article in whatever tracking sheet the user keeps, if one exists.

## Reference files

Read these as needed rather than all upfront:

| File | Read it when |
|---|---|
| `app.md` (repo root, not part of this skill) | Phase 2 — the App Store listing itself: rating, prices, compatibility, screenshots, per-guide keyword map |
| `references/keyword-strategy.md` | Phase 1 — choosing the query, seed keyword list, cannibalization check, refresh cadence |
| `references/product-brief.md` | Phases 2 and 4 — how to use those facts: honest weaknesses, competitor list, voice sample, CTA URLs |
| `references/article-templates.md` | Phase 3 — section skeletons for each of the three article types |
| `references/persuasion.md` | Phase 4 — applied psychology, CTA placement, and the ethical limits |
| `references/seo-technical.md` | Phase 5 — head tags, JSON-LD, tracking parameters, site wiring checklist |
