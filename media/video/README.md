# Video Lessons (Remotion)

Short animated, **narrated** lesson videos for the CCA-F domains. The narration tracks are the same ElevenLabs MP3s used elsewhere in the kit (copied into `public/`), and the on-screen key points animate in sync.

Two compositions are defined (proving the pipeline):

- **AgenticArchitecture** → `out/agentic-architecture.mp4` (~86s)
- **PromptEngineering** → `out/prompt-engineering.mp4` (~74s)

## Render it yourself

Remotion renders via headless Chromium, so rendering needs a machine that can run it (a normal laptop is fine; some sandboxes can't).

```bash
cd media/video
npm install                 # one time
npx remotion studio         # optional: live preview/edit in the browser
npm run render:all          # renders both MP4s into out/
# or individually:
npx remotion render AgenticArchitecture out/agentic-architecture.mp4
npx remotion render PromptEngineering   out/prompt-engineering.mp4
```

Pre-rendered MP4s (if present) live in `out/`. If `out/` is empty, run the commands above — everything needed (source + audio in `public/`) is committed.

## Add more lessons

1. Add a new `LessonData` object in `src/Root.tsx` (tag, title, accent, `audio` filename in `public/`, timed `points`, and `durationInSeconds` ≈ the audio length).
2. Add a `<Composition>` for it.
3. Drop the matching narration MP3 into `public/` (generate one with `../audio/generate_audio.py`).
4. `npx remotion render <Id> out/<name>.mp4`.

## Notes

- The video is just a thin animation layer over the audio script, so regenerating the audio (e.g. with different ElevenLabs voices) and re-rendering keeps them in sync.
- All content is **unofficial** community prep; exam-format details are community-reported.
