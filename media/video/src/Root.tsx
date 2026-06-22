import React from "react";
import { Composition } from "remotion";
import { Lesson, LessonData } from "./Lesson";

const FPS = 30;

// Narration audio is reused from ../audio (copied into public/ at build time).
// durationInFrames is sized to the ElevenLabs MP3 length (+ a short tail).

export const AGENTIC: LessonData = {
  tag: "Domain 1",
  title: "Agentic Architecture & Orchestration",
  accent: "#d97757",
  audio: "overview-01-agentic.mp3",
  points: [
    { t: 2, head: "Workflow vs. Agent", body: "Workflow = predefined code paths. Agent = the model directs its own loop." },
    { t: 13, head: "Simplest thing that works", body: "Add agentic complexity only when it clearly improves outcomes." },
    { t: 24, head: "Know the 5 patterns", body: "Chaining · routing · parallelization · orchestrator–workers · evaluator–optimizer." },
    { t: 36, head: "The agentic loop", body: "Gather context → take action → verify → repeat. Always a STOP condition." },
    { t: 50, head: "Single-agent by default", body: "Multi-agent only for broad, parallelizable work — it can cost ~15× the tokens." },
    { t: 64, head: "Delegate specifically", body: "#1 failure = vague briefs. Give objective, scope, tools, output format." },
    { t: 76, head: "Guarantee with hooks", body: "Hard requirements belong in deterministic code, not a polite prompt line." },
  ],
  durationInSeconds: 86,
};

export const PROMPT: LessonData = {
  tag: "Domain 2",
  title: "Prompt Engineering & Structured Output",
  accent: "#3b6fd4",
  audio: "overview-02-prompt.mp3",
  points: [
    { t: 2, head: "Climb the ladder", body: "Clear & direct first — treat Claude like a brilliant new hire." },
    { t: 14, head: "Examples are leverage", body: "Few-shot must be relevant and diverse — not all the same answer (bias)." },
    { t: 28, head: "Think only when needed", body: "Chain-of-thought for hard reasoning; skip it for simple, fast tasks." },
    { t: 40, head: "Reliable JSON", body: "Tool whose input_schema = output schema, forced — then validate & repair." },
    { t: 54, head: "Cut hallucinations", body: "Allow 'not found', ground in the docs, quote the sources." },
    { t: 64, head: "Prove it with evals", body: "Never trust 'seems better' — change one variable, measure." },
  ],
  durationInSeconds: 74,
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="AgenticArchitecture"
        component={Lesson}
        durationInFrames={Math.round(AGENTIC.durationInSeconds * FPS)}
        fps={FPS}
        width={1280}
        height={720}
        defaultProps={{ data: AGENTIC }}
      />
      <Composition
        id="PromptEngineering"
        component={Lesson}
        durationInFrames={Math.round(PROMPT.durationInSeconds * FPS)}
        fps={FPS}
        width={1280}
        height={720}
        defaultProps={{ data: PROMPT }}
      />
    </>
  );
};
