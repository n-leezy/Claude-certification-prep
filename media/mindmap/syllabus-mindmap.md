# CCA-F Syllabus Mind-Map

> Open this in any [markmap](https://markmap.js.org/) tool (e.g. the "Markmap" VS Code extension, or markmap.js.org) to get an interactive, collapsible mind-map. A rendered `syllabus-mindmap.png` / `.svg` is in this folder too. *Unofficial; weights are community-reported.*

## CCA-F — Claude Certified Architect, Foundations

### D1 · Agentic Architecture (~27%)
- Workflows vs agents (predefined paths vs self-directed loop)
- Five patterns: chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer
- Agentic loop: gather context → act → verify → repeat (+ stop conditions)
- Single-agent default; multi-agent only for broad/parallel work
- Orchestrator–subagents (hub & spoke); specific delegation
- Hooks vs prompts (deterministic guarantees)

### D2 · Prompt Engineering (~20%)
- Clarity ladder (clear → examples → CoT → XML → role → prefill → chain)
- Few-shot: relevant, diverse, delimited
- Chain-of-thought / extended thinking
- Structured output via forced tool schema (+ validate)
- Anti-hallucination (allow "not found", ground, cite)
- Evals (one variable at a time)

### D3 · Tools & MCP (~18%)
- Tool-use loop (your app executes the tool)
- Tool design: name, description-as-prompt, typed schema, concise results
- MCP architecture: host → client → server
- Three primitives: Tools (model), Resources (app), Prompts (user)
- Local (stdio) vs remote (HTTP/SSE)
- Server security: auth + input validation + roots

### D4 · Context & Reliability (~15%)
- Context engineering & context rot
- Prompt caching (static prefix first, identical)
- Long sessions: compaction + external memory
- Reliability: validate+retry, exponential backoff
- Self-consistency, low temperature
- RAG grounding & retrieval quality

### D5 · Claude Code (~20%)
- Config layers (enterprise → project → local)
- CLAUDE.md memory (no secrets)
- Hooks: PreToolUse (block), PostToolUse (lint)
- Subagents (own window/system prompt/tools)
- Skills (SKILL.md, progressive)
- Headless CI: least privilege + hooks + logging
