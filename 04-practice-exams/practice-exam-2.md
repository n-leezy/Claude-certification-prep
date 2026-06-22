# Practice Exam 2 — Claude Certified Architect, Foundations (CCA-F)

**Unofficial.** 60 questions, **120 minutes**, all five domains interleaved. Fresh questions (no overlap with Exam 1). Target ≈ **45/60**. Take this one *after* you've remediated Exam 1 misses.

Domain tags: **[D1]** Agentic · **[D2]** Prompt Eng · **[D3]** Tools/MCP · **[D4]** Context/Reliability · **[D5]** Claude Code.

---

1. **[D2]** A summarizer ignores your length limit. First fix?
   A. Fine-tune  B. State the exact constraint clearly + show an example  C. Multi-agent  D. Raise temperature

2. **[D1]** Which is a *workflow* pattern, not an agent?
   A. Dynamic self-directed tool loop  B. Prompt chaining with gates  C. Open-ended research agent  D. Autonomous coding agent

3. **[D3]** A tool's `description` field functions as:
   A. Dead metadata  B. A prompt that tells the model when/how to use it  C. Only docs for humans  D. A rate limit

4. **[D4]** "Context rot" refers to:
   A. Stale caches  B. Quality dropping as irrelevant/excess tokens dilute attention  C. Token billing  D. Model drift over training

5. **[D5]** To auto-format code after every edit in Claude Code, use:
   A. A PostToolUse hook  B. A note in CLAUDE.md  C. A new model  D. A slash command you call manually

6. **[D1]** Orchestrator–workers is preferable to plain parallelization when:
   A. Subtasks are fixed in advance  B. The lead must dynamically decide subtasks then synthesize  C. You only need one call  D. Latency must be minimal

7. **[D2]** Best way to extract structured fields reliably from messy text?
   A. Hope  B. Define a tool with a typed schema and force the call; validate output  C. Ask for prose  D. Raise max_tokens

8. **[D3]** Which MCP primitive is application-controlled (read-only context the app loads)?
   A. Tools  B. Resources  C. Prompts  D. Sampling

9. **[D4]** A breakpoint for prompt caching should be placed:
   A. Before the system prompt  B. After the stable prefix (system/tools/fixed context)  C. After the user's unique query  D. Nowhere

10. **[D5]** Enterprise/managed policy in Claude Code config is:
   A. Easily overridden by users  B. The highest authority layer  C. The same as local settings  D. Deprecated

11. **[D1]** A task is mostly sequential with shared state. Multi-agent is:
   A. Ideal  B. A poor fit (coordination overhead, no parallel benefit)  C. Required  D. Cheaper

12. **[D2]** Chain-of-thought primarily improves:
   A. Simple lookups  B. Multi-step reasoning accuracy  C. Token cost  D. Latency

13. **[D3]** `tool_choice: "none"` means:
   A. Force a tool  B. The model won't call tools this turn  C. Random tool  D. Stream only

14. **[D4]** To cut perceived latency for users you should:
   A. Disable caching  B. Stream the response  C. Use a bigger model always  D. Add examples

15. **[D5]** A subagent's restricted toolset exists to:
   A. Save money only  B. Limit scope and keep the main context clean/safe  C. Slow it down  D. Nothing

16. **[D1]** Best stop-condition design for an agent?
   A. None; let it run  B. Max iterations + budget cap + explicit done signal  C. Only a timeout you never set  D. Restart on every error forever

17. **[D2]** A good few-shot set avoids:
   A. Diversity  B. A single repeated answer pattern (bias)  C. Delimiters  D. Relevance

18. **[D3]** Local vs remote MCP servers typically use which transports?
   A. stdio (local) vs HTTP/SSE (remote)  B. Email vs FTP  C. Both only stdio  D. Both only HTTP

19. **[D4]** Self-consistency means:
   A. One deterministic sample  B. Sample multiple times and take the majority answer  C. Lower max_tokens  D. Cache the prompt

20. **[D5]** `CLAUDE.md` should NOT contain:
   A. Build commands  B. Architecture notes  C. API keys/secrets  D. Coding conventions

21. **[D1]** "Find the simplest solution that works" mainly warns against:
   A. Using any tools  B. Unnecessary agent complexity (cost/latency/unpredictability)  C. Writing prompts  D. Caching

22. **[D2]** Prefilling the assistant turn is used to:
   A. End generation  B. Control the start/format (e.g., force JSON, skip preamble)  C. Add tools  D. Cache

23. **[D3]** Symptom of too many overlapping tools:
   A. Faster responses  B. The model picks the wrong tool  C. Lower cost  D. Better schemas

24. **[D4]** Message Batches API is best when:
   A. You need instant responses  B. Large volume, latency-insensitive, cost-sensitive  C. Interactive chat  D. Real-time agents

25. **[D5]** Headless Claude Code is used for:
   A. Only interactive chat  B. Scripted/non-interactive automation (CI, codemods, review)  C. Nothing useful  D. Disabling tools

26. **[D1]** A subagent should receive from the orchestrator:
   A. "Do something useful"  B. A specific objective, scope, tools, and output format  C. The full chat history verbatim  D. Nothing

27. **[D2]** To reduce hallucination, allow the model to:
   A. Be more creative  B. Say "I don't know / not in the document"  C. Skip the system prompt  D. Raise temperature

28. **[D3]** The MCP **host** is:
   A. Your server code  B. The AI application the user interacts with  C. The database  D. The model weights

29. **[D4]** Which most directly lowers per-call cost in a repetitive agent loop?
   A. Bigger model  B. Caching the stable system/tool prefix  C. More few-shot  D. Higher temperature

30. **[D5]** A PreToolUse hook returning a "deny" decision will:
   A. Format code  B. Block that tool call  C. Resume a session  D. Log only

31. **[D1]** Evaluator–optimizer needs primarily:
   A. Fixed steps  B. Clear evaluation criteria + value from iteration  C. Routing  D. One call

32. **[D2]** XML tags in prompts mainly help by:
   A. Cutting cost to zero  B. Separating instructions, context, examples, and input  C. Forcing tools  D. Disabling CoT

33. **[D3]** Returning IDs the model can drill into (vs full payloads) is good because:
   A. It's mandatory  B. It conserves context tokens and keeps results concise  C. It hides data  D. It disables caching

34. **[D4]** Approaching the context limit, you should NOT:
   A. Summarize old turns  B. Offload to external memory  C. Drop the system prompt/guardrails  D. Use subagents for big subtasks

35. **[D5]** Custom slash commands in Claude Code are:
   A. Binaries  B. Reusable prompt templates (markdown) invoked by name  C. Env vars  D. Git tags

36. **[D1]** Parallelization "sectioning" means:
   A. Same task many times for voting  B. Splitting into independent subtasks run at once  C. Sequential steps  D. Routing

37. **[D2]** Putting the task's *purpose* in the prompt helps because:
   A. It wastes tokens  B. It improves the model's judgment on edge cases  C. It forces JSON  D. It caches

38. **[D3]** MCP "sampling" lets a server:
   A. Read files  B. Request the host's LLM to generate something  C. Define slash commands  D. Cache prompts

39. **[D4]** Lowering temperature tends to:
   A. Increase randomness  B. Increase output consistency/determinism  C. Add tools  D. Cut context

40. **[D5]** Least-privilege permissions matter most:
   A. In local interactive use with a human approving  B. In autonomous/CI runs with no human in the loop  C. Never  D. Only on weekends

41. **[D1]** Hooks vs prompts: a *hard* requirement should be:
   A. A prompt line  B. A deterministic hook/code rule  C. A few-shot example  D. A higher temperature

42. **[D2]** "Give Claude an out" is a tactic for:
   A. Faster output  B. Reducing forced hallucination  C. Cheaper tokens  D. Routing

43. **[D3]** Most tool-use failures trace back to:
   A. Network  B. Weak descriptions/ambiguous tools  C. Caching  D. Temperature

44. **[D4]** RAG answer quality is bounded mostly by:
   A. Font  B. Retrieval quality and grounding  C. Streaming  D. XML tags

45. **[D1]** Single agent + good tools should be the default because:
   A. It's always best  B. It's simpler/cheaper; reach for multi-agent only when parallel breadth/separation truly helps  C. Multi-agent is banned  D. Tools are free

46. **[D2]** For complex reasoning you can structure output as:
   A. Only prose  B. `<thinking>` reasoning + `<answer>` you parse  C. Random  D. No structure

47. **[D3]** MCP "roots" are used to:
   A. Increase tokens  B. Scope/limit filesystem access  C. Force tools  D. Cache

48. **[D4]** Prompt cache entries typically:
   A. Last forever  B. Expire after a short TTL (refreshed on use)  C. Never expire within a day  D. Are permanent across accounts

49. **[D5]** Skills differ from a giant `CLAUDE.md` because they:
   A. Can't be shared  B. Are progressively loaded only when relevant (saving context)  C. Are secrets  D. Require Docker

50. **[D1]** A "verify work" step in an agent could be:
   A. Ignoring errors  B. Running tests / schema validation / a critic step  C. Raising temperature  D. Removing tools

51. **[D2]** Routing to a cheaper model for easy queries is:
   A. Always wrong  B. A valid cost/quality optimization  C. Impossible  D. Only for latency

52. **[D3]** Forcing a specific tool via `tool_choice` is useful for:
   A. Free-form chat  B. Guaranteeing structured extraction / a required action  C. Disabling tools  D. Caching

53. **[D4]** The best response to occasional invalid JSON from the model:
   A. Trust it blindly  B. Validate against the schema and retry/repair  C. Ignore errors  D. Increase temperature

54. **[D5]** `.claude/settings.json` vs `settings.local.json`:
   A. Both committed  B. Project (committed/shared) vs personal (gitignored)  C. Both gitignored  D. Identical

55. **[D1]** The multi-agent research system's main benefit is:
   A. Fewer tokens  B. Parallel exploration with isolated context windows, then synthesis  C. Determinism  D. Lower latency always

56. **[D2]** More examples generally help most with:
   A. Reducing cost  B. Matching a desired format/style  C. Lowering latency  D. Disabling tools

57. **[D3]** A `tool_result` you send back must reference:
   A. Nothing  B. The matching `tool_use_id`  C. The user's name  D. The cache key

58. **[D4]** Just-in-time context loading beats pre-stuffing because:
   A. It's slower  B. It keeps the window lean and relevant, preserving attention  C. It removes tools  D. It disables caching

59. **[D5]** Putting Claude Code into a PR-review CI job is an example of:
   A. Interactive use  B. Headless automation with guardrails (the reported CI scenario)  C. A workflow with no model  D. Fine-tuning

60. **[D1]** Across all domains, the recurring architectural theme is:
   A. Maximize complexity  B. Use the least complexity that meets the goal, enforce hard requirements deterministically, and curate context  C. Always multi-agent  D. Avoid evals

---

## Answer key (one-line rationale)

1. **B** — clarity + example first.
2. **B** — prompt chaining is a workflow.
3. **B** — description is a prompt.
4. **B** — excess tokens dilute attention.
5. **A** — PostToolUse hook for deterministic formatting.
6. **B** — orchestrator dynamically decides + synthesizes.
7. **B** — typed forced tool + validation.
8. **B** — Resources are app-controlled.
9. **B** — after the stable prefix.
10. **B** — managed policy is highest authority.
11. **B** — multi-agent poor fit for sequential/shared-state.
12. **B** — CoT helps multi-step reasoning.
13. **B** — "none" suppresses tool calls.
14. **B** — streaming improves perceived latency.
15. **B** — limit scope, protect context.
16. **B** — iterations + budget + done signal.
17. **B** — avoid biased single-answer sets.
18. **A** — stdio local, HTTP/SSE remote.
19. **B** — sample many, take majority.
20. **C** — never put secrets in CLAUDE.md.
21. **B** — avoid needless agent complexity.
22. **B** — prefill controls start/format.
23. **B** — overlap causes wrong tool choice.
24. **B** — batch = high-volume, latency-insensitive.
25. **B** — headless = scripted automation.
26. **B** — specific objective/scope/tools/format.
27. **B** — allow "I don't know."
28. **B** — host = the AI app.
29. **B** — cache the stable prefix.
30. **B** — PreToolUse deny blocks the call.
31. **B** — needs eval criteria + iteration value.
32. **B** — separates prompt parts.
33. **B** — conserves context, concise results.
34. **C** — never drop guardrails/system prompt.
35. **B** — reusable markdown prompt templates.
36. **B** — sectioning = independent parallel subtasks.
37. **B** — purpose improves edge-case judgment.
38. **B** — sampling asks host LLM to generate.
39. **B** — lower temp = more consistent.
40. **B** — least privilege critical in autonomous/CI.
41. **B** — hard requirement → deterministic hook.
42. **B** — reduces forced hallucination.
43. **B** — weak descriptions/ambiguous tools.
44. **B** — retrieval quality + grounding.
45. **B** — single agent default; multi-agent only when justified.
46. **B** — `<thinking>`/`<answer>` structure.
47. **B** — roots scope filesystem.
48. **B** — short TTL, refreshed on use.
49. **B** — progressive disclosure saves context.
50. **B** — tests/validation/critic.
51. **B** — valid cost/quality routing.
52. **B** — guarantee extraction/required action.
53. **B** — validate + retry/repair.
54. **B** — project committed vs personal gitignored.
55. **B** — parallel isolated exploration + synthesis.
56. **B** — examples nail format/style.
57. **B** — reference the `tool_use_id`.
58. **B** — keeps window lean/relevant.
59. **B** — headless automation w/ guardrails.
60. **B** — least complexity + deterministic guarantees + context curation.

**Score: ___/60.** Compare to Exam 1. Trending up and ≥45? You're in good shape (subject to the `[COMMUNITY]` caveats about the real exam).
