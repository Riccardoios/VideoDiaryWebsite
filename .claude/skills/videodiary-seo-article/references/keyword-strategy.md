# Keyword strategy

## Contents
- The funnel model
- Scoring rubric
- Seed queries for Video Diary
- Cannibalization check
- Refreshing existing pages
- Where AI-assistant traffic comes from

---

## The funnel model

Three tiers, in descending order of how much you should care:

**Tier 1 — Commercial investigation.** The person has decided they want an app and is choosing between options. `best video journaling apps`, `1 second everyday alternatives`, `day one vs video diary`, `journaling app without AI`. These are the pages that produce downloads. Most of the writing time goes here.

**Tier 2 — Problem-aware, solution-shaped.** The person has a goal that an app solves, but hasn't started shopping. `how to turn daily videos into a movie`, `how to keep a video diary`. Moderate conversion, decent traffic, and they make natural internal-link feeders into Tier 1 pages.

**Tier 3 — Informational.** `what is a video diary`, `benefits of journaling`, `video journal prompts`. These rank and produce almost nothing, because the answer is extractable. They are not worthless — they build topical authority and occasionally get quoted by assistants — but they are not traffic bets. The site already has plenty. Do not add more unless there is a specific reason.

If a candidate query is Tier 3, say so before writing it.

## Scoring rubric

Score each candidate 1–5 on four axes. Anything under 12 total is probably not worth a page.

| Axis | 1 | 5 |
|---|---|---|
| **Buying intent** | Wants a definition | Comparing specific apps to download |
| **Click viability** | Fully answerable in a snippet or AI summary | Needs a table, several options, or real judgment |
| **Winnability** | Dominated by App Store, Reddit, and major publishers | Long-tail, thin existing results, or nobody has actually used the apps |
| **Product fit** | Video Diary is a stretch answer | Video Diary genuinely wins on the criteria that matter to this searcher |

The **product fit** axis is the one people fudge. If Video Diary is not a good answer for this searcher, the article will either be dishonest or useless. Pick a different query.

## Seed queries for Video Diary

Starting points, roughly ordered by expected value. Verify current search demand and competition before committing — these are hypotheses, not data.

**Tier 1 — write these first**
- best video journaling apps (iPhone / free / 2026 variants)
- 1 Second Everyday alternatives
- Day One vs a video-first journal
- best journaling apps with no AI / private journaling apps
- video diary app for iPhone free
- apps that turn daily clips into a movie
- best video journal app without a subscription
- Apple Journal app alternatives for video
- best mood tracking apps with video

**Tier 2**
- how to turn a year of daily videos into a film
- how to start a video diary and actually keep it up
- how to back up a video journal privately
- video diary vs written journal: which sticks

**Tier 3 — already covered, avoid duplicating**
The site's existing eight guides sit almost entirely here — see the guide/keyword table in `app.md`. Check it before writing anything in this tier. Note that `best-video-diary-app-iphone` is already a Tier 1 page: a new roundup has to target a genuinely different query ("best video journaling apps", "free", "no subscription", "no AI") and should link to it rather than compete with it.

**Angles unique to this app that competitors cannot copy**
- The no-AI position. Every journaling app is racing to add AI transcription and summaries. A significant group of people specifically don't want their most private thoughts processed in someone else's cloud, and almost nobody is writing for them. This is the strongest differentiated angle the site has.
- Apple Vision Pro and Mac support — small audience, near-zero competition, very cheap to rank for.
- Localized-market queries. The app ships in seven languages and the user base skews US then Germany; German-language equivalents of Tier 1 queries face far less competition than English ones. Only pursue if the site can serve localized pages properly.

## Cannibalization check

`app.md` (repo root) has the authoritative map under **"Long-tail → guide pages"**: one target keyword per existing guide, plus the secondary terms each one already claims, plus the SERP competitors observed for this niche (memovi.app, 1se.co, uly.app, okorca.com, calmsage.com, psychologytoday.com). Read that table before choosing a query — it is what the site is already ranking for, and it is the fastest way to spot an overlap.

Then ask: **does an existing page target the same intent?**

- If yes and the existing page is weak → improve the existing page instead of creating a new one. Consolidating beats splitting almost every time.
- If yes and the existing page is strong → pick a genuinely different intent, or write a narrower page and link it up to the strong one.
- If no → proceed, and plan which existing pages will link into the new one.

Two pages targeting `best video diary app` will compete with each other, halve each other's authority, and confuse the crawler about which to rank. This is a self-inflicted wound and it is common.

## Refreshing existing pages

Refreshing usually beats publishing. When a page's position slides or its clicks are flat against decent impressions:

1. Re-read the query the page is supposed to answer and check whether the page actually answers it in the first screen.
2. Tighten the title to match how people phrase the search, not how you'd phrase it.
3. Cut any intro that pushes the answer below the fold.
4. Add whatever the top-ranking results have that this page lacks — usually a table, a specific comparison, or a real recommendation.
5. Update the `Updated <Month Year>` line only if the content genuinely changed.

## Where AI-assistant traffic comes from

Assistants cite pages that are unambiguous, structured, and attributable. In practice that means:

- A one-paragraph direct answer near the top that stands alone when quoted out of context.
- Clear entity statements: "Video Diary is a video journaling app for iPhone that stores entries on-device with no AI processing." An assistant needs to be able to lift that sentence and have it be true and complete.
- Comparison tables with real attribute values, which get parsed and re-presented.
- Named authorship and a date. Anonymous content-farm pages get cited less.
- Honest coverage of alternatives — a page that recommends a competitor where the competitor is better reads as a trustworthy source, and that is precisely the kind of page an assistant reaches for when someone asks "what's the best app for X".

There is no ad slot inside an assistant's answer. Being genuinely the most useful page is the only entry.
