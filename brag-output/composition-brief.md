# Hyperframes Composition Brief: Video Diary

## Objective
Create a short launch-style brag video for Video Diary — the hand-drawn, private,
deliberately AI-free video journaling app for iPhone.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080 @ 30fps
- Duration: 22.7 seconds

## Source Material
- Project root: `/Users/riccardocarlotto/Dev/AppBusiness/VideoDiaryWebsite`
- Primary files read: `website/index.html`, `website/css/style.css`, `app.md`,
  `website/assets/screenshot-{1,2,3}.png`, `website/assets/icon-1024.png`
- Product name: Video Diary (App Store: "Video Journal: Video Diary")
- Tagline / strongest claim: "Journaling with videos. Nothing else."
- Key UI to recreate: none recreated — the **real app screens** are used directly.
  `screenshot-1/2/3.png` were cropped to their screen content (992x1950 each, bezel
  and App Store caption removed) and are composited inside an HTML phone frame:
  - `assets/img/screen-record.png` — camera, daily prompt, mood chip, red REC button
  - `assets/img/screen-calendar.png` — marker-drawn month grid with video thumbnails
  - `assets/img/screen-gallery.png` — video grid + the "Creating Montage" tile
  Animated overlays (tap ripple, recording badge, day-cell masks, montage counter) are
  drawn in HTML on top, colour-matched to the screen background `#dddace`.
- Copy that must appear verbatim:
  - "How are you feeling today?" (the AI-assistant line being rejected)
  - "No thanks."
  - "Journaling with videos. Nothing else."
  - "Open. Tap REC. Done."
  - "Every day lands on your calendar."
  - "One tap turns them into a movie."
  - "Your life, one video at a time."
  - "Free · 4.5 ★ on the App Store"

## Creative Direction
- Tone preset: `default`
- Creative direction: a quiet anti-AI ad for a hand-drawn diary app — dry opening joke, warm product payoff
- Interpretation: one gag delivered flat and fast, then the energy settles into warm,
  confident product demonstration. Comfortable holds, no ALL CAPS, no shouting. The marker
  strokes and paper grain carry the personality so the copy doesn't have to.
- Angle: Every journaling app in 2026 opens with an AI assistant asking how you're feeling.
  This one opens with a camera. A slick AI chat card types the inevitable question, a red
  marker scribbles straight through it, and the rest of the film is the warm, hand-drawn app
  that never asked. The scribble *is* the brand — the icon, the calendar grid and the REC
  button are all marker-on-paper doodles.
- Hook: the AI card types "How are you feeling today? ✦", holds, gets slashed by a red
  marker stroke, and "No thanks." lands.
- Outro / punchline: "Your life, one video at a time." + App Store badge + "Free · 4.5 ★".
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign — the cream/periwinkle/ink palette is fixed
  - Any waveform, equalizer or particle visual

## Visual Identity
- Background: `#f6f4ec` (paper), deeper `#ddd9cf`; app screen background `#dddace`
- Text: `#191919` (ink), soft `#444036`
- Accent: `#8894e3` (periwinkle), deep `#5f6cc9`; record red `#e8271b`; warm brown `#8b5e3c`
- Display font: Patrick Hand — shipped locally at `assets/fonts/PatrickHand-Regular.woff2`
- Body font: Inter — shipped locally at `assets/fonts/Inter-Variable.woff2`
- Visual references from the project: hand-inked calendar grid, red doodle REC button,
  cloud-shaped day badges, sketchy `--radius-sketch` border treatment, paper grain

## Storyboard
Use the storyboard in `brag-output/brag-plan.md` as the creative contract.

Scene summary (all on one persistent paper background, so scene changes are content
transitions, not hard frame cuts):
1. Hook — 0.00 → 4.23 — AI card types its question, red marker slashes it, "No thanks."
2. Reveal — 4.23 → 7.40 — app icon + "Video Diary" + "Journaling with videos. Nothing else."
3. Record — 7.40 → 11.06 — phone right / copy left; REC tapped, recording badge counts up
4. Calendar — 11.06 → 14.76 — five day cells fill with real video thumbnails on the beat
5. Montage — 14.76 → 18.44 — "Create Montage" tapped; tile counts 0% → 100%, ink tick draws
6. Outro — 18.44 → 22.70 — icon, wordmark, tagline, App Store badge, "Free · 4.5 ★"

## Audio
- Audio role: warm bed with sparse, motion-matched accents
- Audio arc: sterile typing → one dry thud that ends the AI → warm bed opens on the reveal →
  three interaction cues and one bell payoff across the flow → fade under the badge
- Music: `assets/music/happy-beats-business-moves-vol-9-by-ende-dot-app.mp3`
- Music treatment: from t=0, `data-volume` 0.34, volume automation fading 0 → 0.30 over the
  first 0.5s and 0.34 → 0 across 21.70 → 22.70. Never above 0.36.
- Music cue guidance: bundled preset copied to
  `assets/music/cues/happy-beats-business-moves-vol-9-by-ende-dot-app.music-cues.json`
  (114.84 BPM). Strong-cue locks: **4.23s** wordmark, **8.44s** REC tap, **20.53s** badge.
  Beat grid for the calendar sequence: 11.60 / 12.12 / 12.65 / 13.18 / 13.70.
- Audio-reactive treatment: subtle. Per-frame data extracted with the hyperframes-creative
  `extract-audio-data.py` helper (30fps, 16 bands), trimmed to 690 frames and inlined as
  normalised `AUDIO_BASS` / `AUDIO_RMS` arrays. Bass drives the phone's drop-shadow depth
  and the paper vignette warmth; RMS drives a faint glow on the wordmark. 3-6% swings only.
- Audio-coupled moments:
  - Scene 1 typing — randomised `keyboard/keypress-*` per character
  - Scene 1 scribble — `impact/impactSoft_medium_001` on the stroke's first frame
  - Scene 2 wordmark — `impact/impactSoft_medium_000`, soft
  - Scene 4 cells — `casino/card-slide-{1,2,4}`
  - Scene 3 REC tap — `interface/click_001` exactly on the press frame (the 10ms
    `click_00{2,3,5}` ticks were inaudible under the bed)
  - Scene 4 cells 1, 3, 5 — `casino/card-slide-*` (never all five)
  - Scene 5 Create Montage tap — `ui/click2`; 100% — `impact/impactBell_heavy_000`
  - Scene 6 badge — `impact/impactSoft_medium_002`, soft; nothing after
- SFX selection guidance: match the gesture, not the beat. Clicks only where a tap is
  visible. Card sounds only where a card-like thing arrives.
- SFX analysis guidance: `<skill-dir>/assets/sfx/sfx-analysis.md` — all picks are low or
  medium high-frequency risk; the one medium-risk bell is used exactly once.
- Exact SFX choice: chosen after the animation existed, per the picks above.
- Audio files: copied into `brag-output/composition/assets/{music,sfx}/`

## Hyperframes Instructions
Built against `hyperframes-core` (composition contract, `data-*` timing),
`hyperframes-animation` (motion), `hyperframes-creative` (audio-reactive, palette),
`hyperframes-keyframes` (punch-in), `hyperframes-cli` (check / render).

Requirements:
- Show real UI from the source project — three real app screens are used directly. ✔
- Keep all text readable in the final render; `check`'s layout + contrast passes gate it.
- Keep the video within 15-25 seconds. ✔ 22.7s
- Include the planned music/SFX layer. ✔
- 3 strong-cue locks, 1 beat-grid sequence; ignore any cue that hurts readability.
- Use only local assets; no absolute paths, no network fetches at render time.
- Run `npx hyperframes check` before render — brag's single gate.

## Delivered

- `brag-output/brag.mp4` — 1920x1080, 30fps, 22.70s, 681 frames, H.264 + AAC stereo,
  peak -2.6 dBFS, mean -25.3 dBFS (no clipping; bed fades to silence over the last second).
- `brag-output/brag.jpg` — poster pulled at **14.20s** (the filled-calendar payoff: copy
  settled, every day thumbnail revealed, phone at full punch-in) and baked as frame 0 so
  every platform's thumbnail grabber lands on it.
- `npx hyperframes check`: **0 errors, 0 warnings**; contrast 29/29 WCAG AA. The three
  remaining info-level `content_overlap` notes at t=2.74s are the intended crossfade of the
  dying AI card under "No thanks."
- Two contrast fixes were needed and applied: the AI pill lavender went `#6f7fe0` →
  `#5f6cc9` (white text, 4.69:1), and the recreated in-app brown text went `#8b5e3c` →
  `#805637` over the app's own `#dddace` (4.54:1). The second is a ~4/255 shift, invisible
  beside the real numerals it sits next to.
