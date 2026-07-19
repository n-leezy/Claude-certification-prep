# Study Guide Overview & Study Plan

The map of what's on the exam, what to study, and a schedule that applies the learning method from [`how-to-use-this-folder.md`](how-to-use-this-folder.md).

> Exam blueprint below is the **`[COMMUNITY]`** 5-domain consensus (see [`exam-facts.md`](exam-facts.md)). It aligns with Anthropic's documented best practices, so it's a solid scaffold regardless.

## The five domains at a glance

| #   | Domain                                     | Weight | Core question it tests                                | Notes file                                                         |
| --- | ------------------------------------------ |:------:| ----------------------------------------------------- | ------------------------------------------------------------------ |
| 1   | **Agentic Architecture & Orchestration**   | ~27%   | "Design a reliable agent / multi-agent system"        | [domain-1](../02-domain-notes/domain-1-agentic-architecture.md)    |
| 2   | **Prompt Engineering & Structured Output** | ~20%   | "Get correct, parseable, reliable outputs"            | [domain-2](../02-domain-notes/domain-2-prompt-engineering.md)      |
| 3   | **Tool Design & MCP Integration**          | ~18%   | "Design tools/MCP so the model uses them well"        | [domain-3](../02-domain-notes/domain-3-tool-design-and-mcp.md)     |
| 4   | **Context & Reliability**                  | ~15%   | "Manage the context window; make it production-grade" | [domain-4](../02-domain-notes/domain-4-context-and-reliability.md) |
| 5   | **Claude Code Configuration**              | ~20%   | "Configure Claude Code + agents for dev workflows"    | [domain-5](../02-domain-notes/domain-5-claude-code.md)             |

## Each domain, across every medium

Study a domain in whatever form fits the moment — then test yourself on it.

| Domain                   | Read                                                                                                     | Watch                                           | Hear                                                | See                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| D1 Agentic               | [notes](../02-domain-notes/domain-1-agentic-architecture.md) · [quiz](../03-quizzes/quiz-domain-1.md)    | [video](../media/video/) (Agentic Architecture) | [audio](../media/audio/overview-01-agentic.mp3)     | [diagram](../media/diagrams/agent-orchestration-loop.png)  |
| D2 Prompt Eng            | [notes](../02-domain-notes/domain-2-prompt-engineering.md) · [quiz](../03-quizzes/quiz-domain-2.md)      | [video](../media/video/) (Prompt Engineering)   | [audio](../media/audio/overview-02-prompt.mp3)      | —                                                          |
| D3 Tools & MCP           | [notes](../02-domain-notes/domain-3-tool-design-and-mcp.md) · [quiz](../03-quizzes/quiz-domain-3.md)     | render via Remotion                             | [audio](../media/audio/overview-03-tools.mp3)       | [diagram](../media/diagrams/tool-mcp-flow.png)             |
| D4 Context & Reliability | [notes](../02-domain-notes/domain-4-context-and-reliability.md) · [quiz](../03-quizzes/quiz-domain-4.md) | render via Remotion                             | [audio](../media/audio/overview-04-context.mp3)     | [diagram](../media/diagrams/context-reliability-model.png) |
| D5 Claude Code           | [notes](../02-domain-notes/domain-5-claude-code.md) · [quiz](../03-quizzes/quiz-domain-5.md)             | render via Remotion                             | [audio](../media/audio/overview-05-claude-code.mp3) | [mind-map](../media/mindmap/syllabus-mindmap.png)          |

Plus: a [whole-cert podcast](../media/audio/podcast-full-overview.mp3) (two voices), a [one-page cheat sheet](../media/cheatsheet/cca-f-cheatsheet.pdf), an [Anki deck](../media/anki/cca-foundations.apkg), and the interactive [study hub](../05-html-instructionals/index.html) (flashcards · quiz engine · scenario simulator).

## What "scenario-based" means for your prep

Community reports say most questions are scenarios, not trivia. So the exam rewards **judgment**, not memorization: given a described enterprise situation, pick the *best* architecture/prompt/tool decision and know *why the others are worse*. That's why every quiz answer here explains the distractors too. When you study, always ask: "In what situation would the wrong answer actually be right?"

Reported scenario archetypes to be fluent in `[COMMUNITY]`:

- A **customer-support resolution agent** (tool use, guardrails, escalation, latency/cost).
- A **multi-agent research system** (orchestrator + subagents, context isolation, synthesis).
- **Claude Code in a CI/CD pipeline** (headless/automation, permissions, hooks).
- A **structured data extraction** system (schemas, JSON reliability, validation).

## Prerequisites / assumed knowledge

You should be comfortable with: REST APIs and JSON, basic Python or TypeScript, the idea of an LLM context window and tokens, and what "an API call to a chat model" looks like. If not, do **Claude Platform 101** and **Building with the Claude API** on Anthropic Academy first.

---

## The plans

Pick the one that matches your timeline. All of them front-load *learning* and back-load *full-exam simulation*, and all interleave domains rather than finishing one before starting the next.

### Plan A — 2-week sprint (~1–1.5 hrs/day)

| Day | Focus               | Do                                                                                                                          |
| --- | ------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | Orient              | Read this guide + `how-to-use-this-folder.md`; skim `exam-facts.md`. Start Anthropic Academy *Claude 101* / *Platform 101*. |
| 2   | Domain 1 (part 1)   | Read D1 §1–§3 → Quiz D1 Q1–8 → make cards.                                                                                  |
| 3   | Domain 2 (part 1)   | Read D2 §1–§3 → Quiz D2 Q1–8 → cards. **Review D1 cards.**                                                                  |
| 4   | Domain 3 (part 1)   | Read D3 §1–§3 → Quiz D3 Q1–8 → cards. **Review D1–2 cards.**                                                                |
| 5   | Domain 1 (part 2)   | Finish D1 → rest of Quiz D1. **Review due cards.**                                                                          |
| 6   | Domain 4            | Read D4 → Quiz D4. **Review due cards.**                                                                                    |
| 7   | Domain 5            | Read D5 → Quiz D5. **Review due cards.**                                                                                    |
| 8   | Domain 2 (part 2)   | Finish D2 → rest of Quiz D2. **Review due cards.**                                                                          |
| 9   | Domain 3 (part 2)   | Finish D3 → rest of Quiz D3. **Review due cards.**                                                                          |
| 10  | **Practice Exam 1** | Timed, 120 min, no notes. Score it. Log every miss.                                                                         |
| 11  | Remediate           | Re-study only the topics you missed. Re-quiz those. Heavy flashcards.                                                       |
| 12  | Weak spots          | Redo the quiz questions you got wrong on day 10–11. Teach-it-back on your 3 weakest topics.                                 |
| 13  | **Practice Exam 2** | Timed. Should be ≥ pass line. Log misses.                                                                                   |
| 14  | Final pass          | Flashcard blitz of all "still-missing" cards; light review; rest.                                                           |

### Plan B — 4-week steady (~45 min/day)

Same sequence, half the daily load: spread each "read + quiz" across two days, add an extra full review day at the end of each week, and take Practice Exam 1 at the end of week 3 and Exam 2 mid-week 4. The extra calendar time means **wider spacing**, which is better for retention — Plan B usually produces a higher real score than Plan A for the same effort.

### Plan C — 1-week cram (only if you must)

Days 1–2: read all five domain notes once, fast, doing the quiz immediately after each (retrieval while reading). Day 3: Practice Exam 1. Days 4–5: remediate misses + flashcards. Day 6: Practice Exam 2. Day 7: flashcard blitz. Cramming sacrifices long-term retention — fine if the exam is in 7 days, bad if it's a skill you want to keep.

---

## Readiness checklist (you're ready when…)

- [ ] You can score **≥ 80%** on each per-domain quiz **from memory**.
- [ ] You've taken **both** full practice exams timed and scored **≥ 720-equivalent** (≈45/60) on the most recent one.
- [ ] You can **explain out loud** (Feynman) the agentic loop, when to use multi-agent vs. single-agent, how prompt caching works, what makes a good tool schema, and what MCP primitives exist — without notes.
- [ ] Your flashcard deck has **no cards stuck in box 1** (i.e., nothing you keep missing).
- [ ] You've completed the core Anthropic Academy courses listed in the README.

## Tracking your scores

| Attempt         | Date | Score | Weakest domain | Action |
| --------------- | ---- | ----- | -------------- | ------ |
| Quiz D1         |      | /10   |                |        |
| Quiz D2         |      | /10   |                |        |
| Quiz D3         |      | /10   |                |        |
| Quiz D4         |      | /10   |                |        |
| Quiz D5         |      | /10   |                |        |
| Practice Exam 1 |      | /60   |                |        |
| Practice Exam 2 |      | /60   |                |        |
