# Claude Certified Architect – Foundations (CCA-F): Community Prep

A self-contained, evidence-based study kit for Anthropic's **Claude Certified Architect – Foundations (CCA-F)** exam — the first official Claude technical certification, launched alongside the Claude Partner Network in March 2026.

> **⚠️ Unofficial.** This is community-built study material. It is **not** affiliated with, endorsed by, or produced by Anthropic. Anthropic has published the *existence*, *delivery platform*, and *prep courses* for this certification, but has **not** publicly published a detailed exam blueprint. Everything in this kit is clearly tagged **`[OFFICIAL]`** (confirmed by Anthropic) or **`[COMMUNITY]`** (reported by third-party prep sites / reverse-engineered from Anthropic's documented best practices). Verify all details against [Anthropic's own pages](https://www.anthropic.com/learn) before relying on them.

---

## What this certification is

| | |
|---|---|
| **Name** | Claude Certified Architect – Foundations (CCA-F) `[OFFICIAL]` |
| **Who it's for** | Solution architects building production applications with Claude `[OFFICIAL]` |
| **Delivered on** | Anthropic Academy / Skilljar (`anthropic.skilljar.com`) `[OFFICIAL]` |
| **Access** | Gated behind the (free) Claude Partner Network at launch; broader access expected later in 2026 `[OFFICIAL]` |
| **Format** | ~60 scenario-based multiple-choice questions, 120 minutes `[COMMUNITY]` |
| **Scoring** | Scaled 100–1000; pass ≈ **720** `[COMMUNITY]` |
| **Cost** | ~$99 / attempt (waived for first 5,000 partner employees) `[COMMUNITY]` |
| **Validity** | ~2 years `[COMMUNITY]` |

See [`01-study-guide/exam-facts.md`](01-study-guide/exam-facts.md) for the full official-vs-community breakdown with citations.

---

## What's inside

```
Claude-certification-prep/
├── README.md                      ← you are here
├── LICENSE                        ← MIT
├── 01-study-guide/
│   ├── study-guide-overview.md    ← exam-domain map + week-by-week study plan
│   ├── how-to-use-this-folder.md  ← the learning method (active recall, spacing, interleaving) + citations
│   └── exam-facts.md              ← official vs. community-reported facts, fully sourced
├── 02-domain-notes/               ← deep notes for all 5 domains
│   ├── domain-1-agentic-architecture.md
│   ├── domain-2-prompt-engineering.md
│   ├── domain-3-tool-design-and-mcp.md
│   ├── domain-4-context-and-reliability.md
│   └── domain-5-claude-code.md
├── 03-quizzes/                    ← per-domain quizzes w/ answer keys + explanations
│   ├── quiz-domain-1.md … quiz-domain-5.md
├── 04-practice-exams/             ← two full-length 60-Q practice exams w/ keys
│   ├── practice-exam-1.md
│   └── practice-exam-2.md
├── 05-html-instructionals/        ← open these in any browser (no internet needed)
│   ├── index.html                 ← interactive study hub / guide
│   ├── flashcards.html            ← spaced-repetition flashcard app (Leitner)
│   └── quiz.html                  ← active-recall quiz engine
├── 06-flashcards/
│   └── flashcards.csv             ← Anki-importable deck (CSV)
└── media/                         ← multi-modal study material (see below)
    ├── diagrams/                  ← .excalidraw + .svg + .png concept diagrams
    ├── audio/                     ← narrated MP3 overviews + 2-voice podcast (+ generator)
    ├── video/                     ← Remotion project for animated narrated lessons
    ├── cheatsheet/                ← one-page printable cheat sheet (PDF/PNG/SVG)
    ├── anki/                      ← real Anki .apkg deck (+ builder)
    └── mindmap/                   ← syllabus mind-map (PNG/SVG + markmap outline)
```

## Multi-modal media — learn the way that sticks

Same content, multiple senses (dual-coding + spaced retrieval). Pick what fits the moment:

| Medium | Where | What |
|--------|-------|------|
| 🖼️ **Diagrams** | `media/diagrams/` | Agent loop, tool/MCP flow, context/reliability model, syllabus map — as editable `.excalidraw` **and** `.svg`/`.png`. Regenerate with `python3 media/diagrams/_generate.py`. |
| 🔊 **Audio overviews** | `media/audio/` | A ~1-minute narrated MP3 per domain **+ a ~3-min two-voice podcast** overview of the whole cert. Great for commutes/walks. |
| 🎬 **Video lessons** | `media/video/` | A **Remotion** project that renders animated, narrated lessons (Agentic Architecture + Prompt Engineering) synced to the audio. Run `npm install && npm run render:all`. |
| 🃏 **Anki deck** | `media/anki/cca-foundations.apkg` | Import into Anki for real spaced repetition on any device. Rebuild with `python3 media/anki/build_apkg.py`. |
| 📄 **Cheat sheet** | `media/cheatsheet/cca-f-cheatsheet.pdf` | Everything on one printable page. |
| 🧠 **Mind-map** | `media/mindmap/` | The whole syllabus as a branch map (PNG/SVG) + a `markmap` outline. |
| 🕹️ **Scenario simulator** | `05-html-instructionals/scenario-sim.html` | "Design the system" branching drills for the reported exam scenario archetypes. |

### Secrets & API keys (audio/video generation)

The audio generator reads its key from an **environment variable** and never stores it:

```bash
export ELEVENLABS_API_KEY=sk_...      # your own key; never commit it
python3 media/audio/generate_audio.py
```

If `ELEVENLABS_API_KEY` is unset, the script **automatically falls back to free, no-key TTS** (`edge-tts`, then `gTTS`). Swapping the engine is a one-function change (`synth()` in `generate_audio.py`). No keys are stored anywhere in this repo.

## How to use it (the 60-second version)

1. **Read** [`01-study-guide/how-to-use-this-folder.md`](01-study-guide/how-to-use-this-folder.md) first — it explains *why* this kit is structured around testing yourself rather than re-reading.
2. **Follow** the plan in [`study-guide-overview.md`](01-study-guide/study-guide-overview.md).
3. **Study actively**: skim a domain note once, then immediately hit the matching quiz and the flashcard app. Don't re-read passively.
4. **Open the HTML files** (`05-html-instructionals/index.html`) in your browser for interactive flashcards + quizzes.
5. **Simulate** with the two full practice exams near the end.

## Official prep resources (do these too)

All free on **[Anthropic Academy](https://anthropic.skilljar.com/)** `[OFFICIAL]`:
Claude 101 · Claude Platform 101 · Building with the Claude API · Claude Code 101 · Claude Code in Action · Introduction to MCP (+ Advanced Topics) · Introduction to Agent Skills · Introduction to Subagents · AI Fluency.
Plus the developer docs at **[platform.claude.com/docs](https://platform.claude.com/docs)**.

## Contributing / sharing

This is meant to be shared. Corrections welcome — especially anything that moves a `[COMMUNITY]` fact to `[OFFICIAL]` with a citation. Open an issue or PR.

## License

[MIT](LICENSE). Use it, fork it, share it.
