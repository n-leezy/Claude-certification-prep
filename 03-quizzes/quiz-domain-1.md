# Quiz — Domain 1: Agentic Architecture & Orchestration

10 questions. Mostly scenario-based. **Answer from memory**, then check the key. Read every explanation, including why the wrong options are wrong.

---

1. A team can fully enumerate the steps to process an invoice (extract fields → validate → post to ledger → notify). What should they build?
   - A. A single autonomous agent with broad tool access
   - B. A multi-agent system with an orchestrator
   - C. A fixed **workflow** (prompt chaining with validation gates)
   - D. An evaluator–optimizer loop

2. Which is the strongest signal that you genuinely need an **agent** rather than a workflow?
   - A. The task is high-volume
   - B. The path can't be predicted in advance and the model must adapt its own steps
   - C. The output must be JSON
   - D. You want lower latency

3. You run the same drafting task 5 times and take the best/most-consistent result. Which pattern is this?
   - A. Routing
   - B. Orchestrator–workers
   - C. Parallelization (voting)
   - D. Prompt chaining

4. A multi-agent research system spawns subagents that keep duplicating each other's work and drifting off-task. What's the most likely root cause?
   - A. The model is too small
   - B. Subagents share one context window
   - C. Vague delegation — subagents lack specific objectives, scope, and output format
   - D. Prompt caching is disabled

5. When is paying ~15× the tokens for a multi-agent system most justified?
   - A. A linear, sequential task with shared state
   - B. A broad, open-ended, parallelizable task (e.g., research across many independent directions)
   - C. A simple classification task
   - D. Any task where you want it to finish faster

6. An agent occasionally loops forever on hard inputs. What did the designer most likely omit?
   - A. A system prompt
   - B. Stop conditions (max iterations / budget / explicit done)
   - C. Few-shot examples
   - D. Prompt caching

7. You must **guarantee** an agent never writes files outside a sandbox directory. Best mechanism?
   - A. Add "please don't write outside /sandbox" to the system prompt
   - B. A few-shot example showing it staying in /sandbox
   - C. A deterministic hook/permission rule that blocks writes outside /sandbox
   - D. Lower the temperature

8. In the orchestrator–workers pattern, how should worker results return to the lead agent?
   - A. As raw, full tool dumps appended to the lead's context
   - B. As condensed, structured summaries
   - C. Not at all; workers write the final answer directly
   - D. As a single token "done"

9. A long-running agent loses all progress whenever its context window fills and resets. Best fix?
   - A. Use a bigger model
   - B. Persist plan/state to external storage and reload just-in-time; support session resumption
   - C. Increase temperature
   - D. Add more tools

10. Which describes the agentic loop's three core capabilities?
   - A. Encode, store, retrieve
   - B. Gather context → take action → verify work (repeat)
   - C. Plan, prompt, print
   - D. Route, cache, stream

---

## Answer key & explanations

1. **C.** Known, fixed steps → a workflow (prompt chaining) with programmatic validation gates is simpler, cheaper, and more predictable than any agent. *Simplest thing that works.* A/B add unneeded autonomy and cost; D fits iterative quality refinement, not a fixed pipeline.

2. **B.** The defining reason to use an agent is an **unpredictable path** requiring dynamic, model-directed steps. Volume (A) and low latency (D) actually argue *against* agents; JSON output (C) is a prompt/tool-design concern.

3. **C — parallelization, voting flavor.** Running the same task multiple times for confidence/diversity is "voting." Routing (A) sends *different* inputs to *different* prompts; orchestrator–workers (B) dynamically decomposes; chaining (D) is sequential.

4. **C.** The #1 multi-agent failure is **vague delegation**. Each subagent needs a specific objective, scope boundaries, tools, and output format. (B is false — subagents have *separate* windows, which is the point.)

5. **B.** Multi-agent earns its token cost on **broad, open-ended, parallelizable** work. Sequential/shared-state (A) and simple tasks (C) are worse with multi-agent; "finish faster" (D) isn't guaranteed and ignores coordination overhead.

6. **B.** Without **stop conditions**, an agent can loop indefinitely. Always cap iterations/budget or provide an explicit completion signal.

7. **C.** A hard requirement must be enforced **deterministically** (hook/permission), not requested in a prompt. Prompts/examples (A/B) are soft; temperature (D) is irrelevant. This is the hooks-vs-prompts rule.

8. **B.** Return **condensed, structured summaries** to keep the orchestrator's context clean. Raw dumps (A) blow up context; workers writing the final answer (C) defeats synthesis.

9. **B.** Persist state **externally** and reload just-in-time, with session resumption. Bigger models/more tools/temperature don't solve durable state.

10. **B.** Gather context → take action → verify work, looping until done — the Agent SDK framing.

**Score:** ___/10 (aim ≥8 before the exam)
