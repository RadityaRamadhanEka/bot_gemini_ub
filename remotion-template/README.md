# Gemini Academy Remotion Template

Starter Remotion project for short vertical videos. The included composition
`KulikDataEpisode12` is a working visual sample based on the Episode 12 draft.
It uses reusable scene, character, chart, subtitle, and brand-mark components.

## Setup

From this directory, install dependencies and open Remotion Studio:

```powershell
npm install
npm run studio
```

Render the sample video:

```powershell
npm run render:episode-12
```

The output is written to `out/episode-12.mp4`.

## Replace the placeholders

- The sample character and campus setting are vector illustrations in
  `src/ShortVideo.tsx`. Keep the character design consistent when adapting the
  scene list to another draft.
- The end-card brand mark is a placeholder until the official Gemini Academy
  logo asset is supplied. Put the approved asset in `public/assets/`, then set
  `logoAsset` in `src/Root.tsx` to its path relative to `public`.
- Voiceover is optional in the sample. Put the approved male VO file in
  `public/audio/`, then set `voiceoverAsset` in `src/Root.tsx` to its path.
  Until then, the dialogue is shown as subtitles and no audio is fabricated.
- Update the `scenes` list in `src/ShortVideo.tsx` to match a new draft. Scene
  durations are in frames at 30 fps and must add up to `durationInFrames` in
  `src/Root.tsx`.

The sample uses synthetic transactions only. Verify each draft's facts,
calculations, and official brand assets before publishing.
