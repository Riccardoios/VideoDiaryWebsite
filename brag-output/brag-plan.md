# Brag Plan: Video Diary

## What is this app?
Video Diary is an iPhone video-journaling app with a hand-drawn, cream-paper look: open it,
tap REC, say what's on your mind, and every entry lands on a calendar you can turn into a
montage. Its whole identity is what it *refuses* to do — no AI companion, no filters, no feed.

## The angle
Every journaling app in 2026 opens with an AI assistant asking how you're feeling.
This one opens with a camera. The video makes that the joke and the pitch at once:
a slick AI chat bubble types its inevitable question, a red marker scribbles straight
through it, and the rest of the film is the warm, hand-drawn app that never asked.

Specific to this project because the scribble *is* the brand — the app's icon, calendar
grid and REC button are all marker-on-paper doodles, and the App Store copy literally
says "no AI filters or chatbots — just you and your story."

## Hook (first 2-3 seconds)
A clean white AI-assistant card on cream paper types out "How are you feeling today? ✦".
It holds just long enough to feel familiar. Then a hand-drawn red marker stroke slashes
across it and the card crumples away. One line lands: **"No thanks."**

## Key moments (the middle)
- The real record screen: a tap on the fat red hand-drawn REC button, ripple, recording
  ring, timer ticking 0:01 → 0:03. "Open. Tap REC. Done."
- The real calendar screen: empty periwinkle marker cells fill in one by one with actual
  video thumbnails, on the beat, like a month assembling itself.
- The real gallery: "Create Montage" gets tapped and the tile counts 0% → 100%, then flips
  to a finished montage with a play glyph.

## Outro / punchline
Icon, wordmark, and the site's own closing line: "Your life, one video at a time."
Then the App Store badge and "Free · 4.5 ★". No claim bigger than the product.

## User flow worth showing
Entry → key action → result, taken straight from the app's three real screens:
1. **Record** — open on the camera, tap REC, add a prompt answer and a mood.
2. **Calendar** — the entry lands on its day; months of days carry thumbnails.
3. **Montage** — Gallery → Create Montage → progress → one movie of your memories.

Scenes 3, 4 and 5 are this flow, shown on cropped real App Store screenshots inside an
HTML phone frame, with animated overlays (tap ripple, cell reveals, progress counter).

## Tone
- Preset: `default`
- Creative direction: a quiet anti-AI ad for a hand-drawn diary app — dry opening joke, warm product payoff
- Interpretation: one gag up front, delivered flat and fast, then the energy relaxes into
  warm, confident product demonstration. Comfortable holds, no shouting, no ALL CAPS.
  Marker strokes and paper texture carry the personality so the copy doesn't have to.

## Format: landscape — 1920x1080
## Duration: 22.7 seconds

## Visual identity (from the project)
- Background: `#f6f4ec` (--paper), deeper paper `#ddd9cf`
- Accent: `#8894e3` (--periwinkle), deep `#5f6cc9`; record red `#e8271b`
- Text: `#191919` (--ink), soft `#444036`; warm brown `#8b5e3c` for calendar numerals
- Display font: Patrick Hand (Google Fonts, already used site-wide)
- Body font: system sans (-apple-system / Helvetica stack), as on the site
- Strongest visual element: the marker-drawn calendar grid — periwinkle hand-inked cells
  with brown numerals and photo thumbnails, on cream paper

## Share copy (draft)
Every journaling app now opens with an AI asking how you feel. Video Diary opens with a camera.

## Audio direction
- Role: warm bed with sparse, motion-matched accents
- Music: `happy-beats-business-moves-vol-9-by-ende-dot-app.mp3` (114.84 BPM, mid-energy, laid-back)
- Music treatment: starts at 0 under the hook at 0.30, rises to 0.34 from the reveal,
  fades out over the last 1.0s under the App Store badge. Never above 0.36.
- Music cue guidance: bundled preset read from
  `assets/music/cues/happy-beats-business-moves-vol-9-by-ende-dot-app.music-cues.json`.
  - Strong-cue locks (3): **4.23s** wordmark reveal · **8.44s** REC tap · **20.53s** App Store badge.
  - Secondary strong beats available at 2.65 (scribble payoff) and 14.76 (gallery cut).
  - Beat-grid window for the calendar thumbnail sequence: 11.60 / 12.12 / 12.65 / 13.18 / 13.70
    (non-text image reveals, so every-beat spacing is fine here).
- Audio-reactive treatment: subtle; use music RMS to let the paper-grain vignette and the
  phone's drop shadow breathe, and give the wordmark a faint warm glow on stronger bars.
  No waveform, equalizer, or particle visuals.
- SFX posture: sparse-to-moderate, motion-matched. Typing ticks for the AI line, one dry
  impact on the scribble, one click on each simulated tap, soft card sounds on three of the
  five calendar reveals, one bell on the finished montage.
- Audio-coupled moments: typed AI question (per-character key ticks); marker scribble;
  REC tap; calendar cells arriving on the beat; montage completion payoff; badge landing.
- Restraint rule: no sound on the closing tagline — let the bed carry it and fade.
  Never score all five calendar cells; accent the 1st, 3rd and 5th only.

## Storyboard

### Scene 1 — "How are you feeling today?" — 4.23s (0.00 → 4.23)
Cream paper. A sleek white AI-assistant card (lavender gradient avatar, sparkle, system
font — deliberately *not* this brand) slides in at 0.15. From 0.45 it types
"How are you feeling today? ✦" over ~1.1s, then holds. At 2.12 a red marker stroke draws
across the card in 0.25s; the card desaturates, tilts and drops away. At 2.65 the words
**"No thanks."** land in big Patrick Hand ink, held to 4.23.
Sequential/interaction: yes — per-character typing of the AI question, then a drawn-on
marker slash (SVG stroke-dashoffset) over the card.
Audio intent: familiar, slightly sterile, then one dry physical thud that ends it.
Audio-coupled idea: randomized `keyboard/keypress-*` per character; one `impactSoft_medium`
on the scribble; nothing on "No thanks." — the silence is the punchline.
Music: laid-back bed at 0.30.
Transition mood: hard cut → Scene 2

### Scene 2 — The reveal — 3.17s (4.23 → 7.40)
// beat-locked: 4.23s. App icon (`icon-1024.png`) pops in with a slight overshoot next to
the "Video Diary" wordmark in Patrick Hand ink. At 5.28 the subline lands verbatim from the
App Store screenshot: **"Journaling with videos. Nothing else."** Held to 7.40.
Sequential/interaction: none — one confident two-part reveal.
Audio intent: the warm turn; the bed opens up.
Audio-coupled idea: one `interface/drop_002` on the icon pop.
Music: bed rises to 0.34.
Transition mood: clean slide → Scene 3

### Scene 3 — Record — 3.66s (7.40 → 11.06)
Split frame: copy left, phone right. The phone slides up from the bottom showing the **real
record screen** (cropped from `screenshot-2.png`): selfie camera, the prompt
"What brings you comfort today?", the mood chip, and the red hand-drawn REC button.
At 7.92 the left copy reads **"Open. Tap REC. Done."** (held to 11.06).
// beat-locked: 8.44s — a finger/cursor taps REC: ripple ring, button dips to 0.9 and back,
a red recording ring traces the screen edge, and a timer badge ticks 0:01 → 0:03.
Sequential/interaction: yes — simulated tap on the REC button plus a counting timer.
Audio intent: one crisp, satisfying confirmation. Nothing else.
Audio-coupled idea: `interface/click_001` exactly on the tap frame.
Music: steady bed.
Transition mood: clean slide (screen swaps, phone stays) → Scene 4

### Scene 4 — Calendar — 3.70s (11.06 → 14.76)
The phone holds position; its screen crossfades to the **real calendar screen** (cropped from
`screenshot-1.png`) with five day-cells masked by blank cream cards so the month starts
mostly empty. Left copy swaps to **"Every day lands on your calendar."**
// beat-grid: cells reveal at 11.60, 12.12, 12.65, 13.18, 13.70 — each mask lifts and scales
away to expose the real video thumbnail underneath. Slow push-in on the phone from 14.22.
Sequential/interaction: yes — five thumbnails arriving one by one on the beat.
Audio intent: a gentle accumulating rhythm, not a drum fill.
Audio-coupled idea: `casino/card-place-*` on the 1st, 3rd and 5th reveals only.
Music: steady bed.
Transition mood: clean slide → Scene 5

### Scene 5 — Montage — 3.68s (14.76 → 18.44)
Screen swaps to the **real gallery** (cropped from `screenshot-3.png`). Left copy:
**"One tap turns them into a movie."** At 15.28 a cursor taps "Create Montage" in the nav.
The montage tile's percentage is masked and replaced by our own counter running
0% → 100% under the label "Creating Montage". At 17.38 it hits 100%, the tile flips to a
finished montage thumbnail with a play glyph and a hand-drawn tick.
Sequential/interaction: yes — simulated tap on "Create Montage", then a running counter.
Audio intent: build, then one clean payoff.
Audio-coupled idea: `interface/click_002` on the tap; `chips-stack` ticks thinned under the
counter; `impact/impactBell_heavy_000` exactly on 100%.
Music: steady bed.
Transition mood: soft crossfade → Scene 6

### Scene 6 — Outro — 4.26s (18.44 → 22.70)
Full-bleed cream paper. The app icon and the "Video Diary" wordmark settle centre at 18.50.
At 18.96 the site's closing line lands: **"Your life, one video at a time."** (held to 22.70).
// beat-locked: 20.53s — the App Store badge slides up with **"Free · 4.5 ★"** beside it.
Hold on the full lockup to 22.70, music fading over the final 1.0s.
Sequential/interaction: none — a settled, postable end card.
Audio intent: resolve and exhale.
Audio-coupled idea: one soft `interface/drop_001` as the badge lands; nothing after.
Music: bed fades to 0 across 21.70 → 22.70.
Transition mood: end

**Music mood for this video:** upbeat but laid-back — warm, unhurried, never corporate-peppy.
**Audio summary:** sterile typing gives way to one dry thud, then a warm bed carries three
motion-matched interaction cues and a single bell payoff before fading under the badge.

## Sensitive-content note
The four App Store screenshots are already-published public marketing assets for this app,
and the faces and photos in them are the developer's own. Nothing private, no keys, no URLs
beyond the public App Store link and `videodiary.io`, and no third-party personal data
enters the composition.
