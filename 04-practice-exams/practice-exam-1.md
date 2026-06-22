# Practice Exam 1 — Claude Certified Architect, Foundations (CCA-F)

**Unofficial.** Modeled on the `[COMMUNITY]`-reported format: 60 scenario-weighted multiple-choice questions, **120 minutes**, mixed across all five domains (interleaved on purpose). Target ≈ **45/60** (~720 scaled equivalent) to feel ready.

> Rules: no notes, set a 120-min timer, answer everything (no penalty for guessing), then score with the key at the bottom and **log every miss**.

Domain tags: **[D1]** Agentic Architecture · **[D2]** Prompt Eng · **[D3]** Tools/MCP · **[D4]** Context/Reliability · **[D5]** Claude Code.

---

1. **[D1]** A bank can fully specify the steps to triage a support ticket. Best design?
   A. Autonomous agent  B. Fixed workflow with gates  C. Multi-agent swarm  D. Evaluator–optimizer

2. **[D3]** Who executes a tool after Claude returns a `tool_use` block?
   A. The model  B. Your application  C. Anthropic  D. The MCP server automatically

3. **[D2]** Most reliable way to force schema-valid JSON?
   A. "Return JSON" instruction  B. Tool with `input_schema` = output schema, forced  C. temperature 0  D. Prefill a sentence

4. **[D4]** Prompt-cache prefix must be:
   A. Variable first  B. Static first, identical, variable last  C. Any order  D. User-only

5. **[D5]** Which file is the shared, committed team config?
   A. `settings.local.json`  B. `~/.claude/settings.json`  C. `.claude/settings.json`  D. `CHANGELOG.md`

6. **[D1]** Strongest reason to choose an agent over a workflow?
   A. High volume  B. Unpredictable path needing dynamic adaptation  C. JSON output  D. Lower latency

7. **[D3]** MCP's three core primitives?
   A. Tools, Resources, Prompts  B. Host, Client, Server  C. Read, Write, Exec  D. Tools, Memory, Cache

8. **[D2]** First step on the prompt-engineering ladder?
   A. Fine-tune  B. Multi-agent  C. Be clear, direct, detailed  D. Chain-of-thought

9. **[D4]** Adding lots of marginally-relevant context usually:
   A. Helps always  B. Degrades via attention dilution  C. No effect  D. Cuts cost

10. **[D5]** A PreToolUse hook can:
   A. Only log  B. Block an action before it runs  C. Only format code  D. Resume sessions

11. **[D1]** Subagents duplicating work and drifting most likely means:
   A. Model too small  B. Vague delegation (no clear objective/scope/format)  C. Caching off  D. Shared window (impossible)

12. **[D3]** Top cause of a model misusing a well-built tool?
   A. Strict schema  B. Under-specified description  C. Long name  D. Small result

13. **[D2]** Your few-shot examples all end "approved." Risk?
   A. Cost only  B. Bias toward "approved"  C. None  D. Examples ignored

14. **[D4]** Prompt caching is most worth it when:
   A. Every prompt differs  B. A big stable prefix is reused across many calls  C. One call only  D. Deterministic outputs needed

15. **[D5]** `CLAUDE.md` is for:
   A. Secrets  B. Persistent auto-loaded project/user context  C. MCP transport  D. A changelog

16. **[D1]** Running the same task 5× and taking the best is which pattern?
   A. Routing  B. Orchestrator–workers  C. Parallelization (voting)  D. Chaining

17. **[D2]** To make Claude start output with `{` and skip preamble:
   A. Stop sequence  B. Prefill assistant with `{`  C. Raise max_tokens  D. Add example

18. **[D3]** Which MCP primitive is model-controlled?
   A. Resources  B. Prompts  C. Tools  D. Roots

19. **[D4]** Best handling when a chat exceeds the window mid-session?
   A. Crash  B. Compact/summarize + external memory  C. Drop system prompt  D. Shrink model

20. **[D1]** The agentic loop's three capabilities:
   A. Encode/store/retrieve  B. Gather context / take action / verify  C. Plan/prompt/print  D. Route/cache/stream

21. **[D5]** No-human-in-loop CI with Claude Code requires:
   A. Unrestricted perms  B. Least privilege + enforcement hooks + logging  C. No tools  D. Main branch only

22. **[D2]** When is chain-of-thought the wrong choice?
   A. Multi-step math  B. Simple classification where latency matters  C. Complex analysis  D. Logic puzzle

23. **[D3]** Reason to use MCP over hardcoded tools for a reused DB integration?
   A. Always cheaper  B. Write once, reuse across any MCP host  C. Removes auth  D. Ends hallucination

24. **[D4]** Cost model of prompt caching?
   A. Reads > writes  B. Writes slightly > normal; reads much cheaper  C. Both free  D. Doubles cost

25. **[D1]** To keep an agent from looping forever you need:
   A. A system prompt  B. Stop conditions  C. Few-shot  D. Caching

26. **[D5]** A subagent gets which isolation?
   A. Own billing/region/key  B. Own context window, system prompt, restricted tools  C. Bigger model + admin  D. Nothing

27. **[D2]** Best anti-hallucination combo for document Q&A?
   A. Higher temp + longer  B. Allow "not found," answer only from doc, quote support  C. Remove system prompt  D. Force a tool

28. **[D3]** Host vs client vs server: the **client** is:
   A. The DB  B. The 1:1 connector inside the host  C. The model  D. The user

29. **[D4]** Huge latency-insensitive extraction job — two best levers?
   A. High temp + streaming  B. Batches API + prompt caching of fixed prefix  C. Multi-agent + bigger model  D. More examples + Opus everywhere

30. **[D1]** When is multi-agent's ~15× token cost justified?
   A. Sequential shared-state task  B. Broad, open-ended, parallelizable task  C. Simple classification  D. Just to finish faster

31. **[D5]** MCP prompts from a server usually appear in Claude Code as:
   A. Daemons  B. Slash commands  C. Env vars  D. Git hooks

32. **[D2]** Why wrap prompt parts in XML tags?
   A. Zero cost  B. Prevent the model confusing instructions vs data  C. API requires it  D. Disables hallucination

33. **[D4]** Best practice for rate-limit/transient errors?
   A. Infinite immediate retries  B. Exponential backoff + idempotency  C. Ignore  D. max_tokens=1

34. **[D3]** Tool returns a 50KB blob each call, agent degrades. Fix?
   A. Return only needed data; paginate; hand back IDs  B. Always return all  C. Raise max_tokens  D. Disable cache

35. **[D1]** In orchestrator–workers, results should return as:
   A. Raw full dumps  B. Condensed structured summaries  C. Not at all  D. One token

36. **[D5]** Highest-authority Claude Code config layer?
   A. Local project  B. Enterprise/managed policy  C. User global  D. Random

37. **[D2]** With an extended-thinking model on a hard task:
   A. Prescribe each step  B. Give the goal + room to think  C. Forbid reasoning  D. Always prefill thinking

38. **[D4]** "Context engineering" means:
   A. One clever line  B. Curating the whole token set for relevance/timing  C. Bigger window  D. Fine-tuning

39. **[D3]** Two security practices for a remote MCP server?
   A. Trust inputs; expose secrets  B. Require auth; validate/scope inputs (roots)  C. Run as root, no logs  D. Disable TLS

40. **[D1]** A long-running agent loses progress on context reset. Fix?
   A. Bigger model  B. External state + session resumption  C. Higher temp  D. More tools

41. **[D2]** You changed 3 prompt things and it "seems better." Problem?
   A. None  B. No eval + multiple changes = can't attribute  C. Needs emojis  D. Temp too low

42. **[D5]** You must guarantee tests pass before commit in an agent dev flow. Use:
   A. A polite `CLAUDE.md` note  B. A hook gating the commit  C. A new example  D. Higher temperature

43. **[D3]** A user-invoked reusable template (slash command) is which primitive?
   A. Tool  B. Resource  C. Prompt  D. Sampling

44. **[D4]** Correctness-over-cost consistency — best two?
   A. High temp, 1 sample  B. Low temp + self-consistency voting  C. Remove validation  D. No system prompt

45. **[D1]** Routing pattern is best when:
   A. Steps are fixed and sequential  B. Distinct input categories are handled better by specialized prompts/models  C. You want voting  D. Path is unpredictable

46. **[D2]** Few-shot examples should be:
   A. Many identical  B. Relevant, diverse, clearly delimited  C. As long as possible  D. Always the same answer

47. **[D3]** `tool_choice: "any"` does what?
   A. Forbids tools  B. Forces the model to use some tool  C. Picks randomly  D. Streams

48. **[D4]** Biggest reliability risk in a RAG system?
   A. XML tags  B. Poor retrieval (garbage in/out)  C. Caching the system prompt  D. Streaming

49. **[D5]** An Agent Skill is loaded:
   A. Always, fully, up front  B. Progressively, when the task matches  C. Never automatically  D. Only via Docker

50. **[D1]** "Simplest thing that works" implies you should:
   A. Always build agents  B. Prefer a single LLM call/workflow until complexity is justified  C. Always use multi-agent  D. Avoid tools

51. **[D2]** Best place for durable role/policy instructions?
   A. Each user message  B. System prompt (also aids caching)  C. Tool results  D. Assistant prefill

52. **[D3]** Orchestrator–workers vs parallelization differ because:
   A. Same thing  B. Orchestrator dynamically decides subtasks; parallelization uses predefined ones  C. Parallelization is sequential  D. Orchestrator can't synthesize

53. **[D4]** Just-in-time retrieval means:
   A. Load everything up front  B. Fetch information when needed rather than pre-stuffing context  C. Never retrieve  D. Cache all docs forever

54. **[D5]** `.claude/settings.local.json` is:
   A. Committed team config  B. Your personal, gitignored overrides  C. Enterprise policy  D. The memory file

55. **[D1]** Evaluator–optimizer pattern fits when:
   A. Steps are fixed  B. Clear eval criteria exist and iteration measurably improves output  C. You need routing  D. Single call suffices

56. **[D2]** Giving the model an "I don't know" option primarily:
   A. Raises cost  B. Reduces forced hallucination  C. Slows output  D. Breaks JSON

57. **[D3]** Parallel tool calls work best when tools are:
   A. Interdependent  B. Independent  C. Destructive  D. Undocumented

58. **[D4]** Picking a small fast model for routing/classification and a strong model for hard reasoning is:
   A. Wasteful  B. Sensible model selection / routing  C. Impossible  D. Only for cost, never quality

59. **[D5]** Where should subagents be defined in a project?
   A. In `CLAUDE.md` only  B. As markdown files (e.g. `.claude/agents/`) with when-to-use descriptions  C. In secrets  D. They can't be defined

60. **[D1]** A destructive tool action in an agent should be:
   A. Run freely  B. Gated behind confirmation / human-in-the-loop  C. Hidden from logs  D. Retried infinitely

---

## Answer key (with one-line rationale)

1. **B** — known fixed steps → workflow.
2. **B** — your app executes; model only emits intent.
3. **B** — forced tool schema = most reliable JSON.
4. **B** — static-first, identical prefix, variable last.
5. **C** — project `.claude/settings.json` is shared/committed.
6. **B** — unpredictable, adaptive path = agent.
7. **A** — Tools, Resources, Prompts.
8. **C** — clarity first on the ladder.
9. **B** — context rot / attention dilution.
10. **B** — PreToolUse can block.
11. **B** — vague delegation is the #1 multi-agent failure.
12. **B** — description is a prompt; under-specified = misuse.
13. **B** — non-diverse examples bias output.
14. **B** — reuse of a large stable prefix.
15. **B** — persistent auto-loaded context.
16. **C** — voting (parallelization).
17. **B** — prefill assistant with `{`.
18. **C** — Tools are model-controlled.
19. **B** — compact/summarize + external memory.
20. **B** — gather/act/verify.
21. **B** — least privilege + hooks + logging.
22. **B** — skip CoT on simple latency-sensitive tasks.
23. **B** — write once, reuse across hosts.
24. **B** — writes slightly pricier, reads much cheaper.
25. **B** — stop conditions.
26. **B** — own window/system prompt/restricted tools.
27. **B** — allow "not found," ground, quote.
28. **B** — client = 1:1 connector inside host.
29. **B** — Batches + caching.
30. **B** — broad/open-ended/parallelizable.
31. **B** — surface as slash commands.
32. **B** — separate instructions from data.
33. **B** — exponential backoff + idempotency.
34. **A** — return only needed data; paginate; IDs.
35. **B** — condensed structured summaries.
36. **B** — enterprise/managed policy is top.
37. **B** — goal + room to think.
38. **B** — curate the whole token set.
39. **B** — auth + validate/scope (roots).
40. **B** — external state + session resumption.
41. **B** — no eval + multiple changes.
42. **B** — hook gates the commit.
43. **C** — Prompt primitive.
44. **B** — low temp + self-consistency.
45. **B** — distinct categories → specialized handling.
46. **B** — relevant, diverse, delimited.
47. **B** — forces some tool use.
48. **B** — retrieval quality dominates.
49. **B** — progressive disclosure on match.
50. **B** — escalate complexity only when justified.
51. **B** — system prompt (and helps caching).
52. **B** — orchestrator decides subtasks dynamically.
53. **B** — fetch when needed.
54. **B** — personal gitignored overrides.
55. **B** — clear criteria + iteration helps.
56. **B** — reduces forced hallucination.
57. **B** — independent tools parallelize cleanly.
58. **B** — sensible routing/model selection.
59. **B** — markdown agent files with descriptions.
60. **B** — gate destructive actions with a human.

**Score: ___/60.** Log every miss → re-study that domain note → re-quiz. Below ~45? Don't book the exam yet.
