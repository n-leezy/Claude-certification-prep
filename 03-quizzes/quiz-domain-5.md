# Quiz — Domain 5: Claude Code Configuration

10 questions, answer from memory, then check the key.

---

1. Which Claude Code config file is meant to be **committed and shared with the team**?
   - A. `~/.claude/settings.json`
   - B. `.claude/settings.json` (project)
   - C. `.claude/settings.local.json`
   - D. None should be committed

2. What is `CLAUDE.md` for?
   - A. Storing secrets
   - B. Persistent project/user context (conventions, architecture, commands) auto-loaded into Claude's context
   - C. Defining MCP transports
   - D. A changelog

3. You must guarantee the linter runs after **every** file edit. Best mechanism?
   - A. Ask Claude in `CLAUDE.md` to remember to lint
   - B. A **PostToolUse hook** that runs the linter automatically
   - C. A few-shot example
   - D. A custom slash command you hope to remember to call

4. Which hook event can **block** a tool action before it happens?
   - A. PostToolUse
   - B. Stop
   - C. PreToolUse
   - D. SessionStart

5. What three things does a Claude Code **subagent** get that isolate it from the main conversation?
   - A. Its own billing, region, and API key
   - B. Its own context window, system prompt, and restricted toolset
   - C. A bigger model, more tokens, and admin rights
   - D. Nothing; it shares everything

6. An **Agent Skill** consists of:
   - A. A binary plugin only
   - B. A folder with `SKILL.md` (instructions + metadata) plus optional scripts/resources, auto-applied when relevant
   - C. A single JSON config
   - D. A Docker image

7. You're running Claude Code **headless in CI** with no human to approve prompts. What's mandatory?
   - A. Full unrestricted permissions for speed
   - B. Least-privilege permissions + hooks to enforce gates + logging
   - C. Disable all tools
   - D. Run only on the main branch

8. In Claude Code, MCP **prompts** from a connected server typically surface as:
   - A. Background daemons
   - B. Slash commands the user can invoke
   - C. Environment variables
   - D. Git hooks

9. Configuration precedence (highest authority first) is roughly:
   - A. Local project > project > user > enterprise
   - B. Enterprise/managed policy > user > project > local — *(careful: see explanation)*
   - C. User > everything
   - D. Random

10. Why keep `CLAUDE.md` concise and high-signal?
   - A. GitHub file size limits
   - B. It's loaded into the context window — bloated memory wastes the model's limited attention (Domain 4)
   - C. Markdown can't be long
   - D. It speeds up git

---

## Answer key & explanations

1. **B.** **`.claude/settings.json`** (project scope) is the shared, committed team config. `settings.local.json` is personal/gitignored; `~/.claude/...` is your user-global config.

2. **B.** `CLAUDE.md` is **persistent memory/context** — conventions, architecture, key commands — auto-loaded. Never put secrets in it.

3. **B.** A hard "always" requirement → a **PostToolUse hook** (deterministic), not a prompt/memory request. This is the hooks-vs-prompts rule applied in Claude Code.

4. **C.** **PreToolUse** runs before the tool and can deny it. PostToolUse runs after; Stop/SessionStart are different lifecycle points.

5. **B.** A subagent has its **own context window, its own system prompt, and a restricted toolset** — the Claude Code expression of orchestrator/worker isolation.

6. **B.** A Skill = a **`SKILL.md` folder** (instructions + metadata, optional scripts), progressively loaded when the task matches.

7. **B.** No human in the loop → **least privilege + enforcement hooks + logging** are mandatory guardrails.

8. **B.** MCP **prompts** show up as **slash commands**; resources become loadable context; tools become callable tools.

9. **B.** Enterprise/managed policy is the **highest** authority (admins can't be overridden by users). Among the rest, more-specific generally refines less-specific; the key exam point is that **managed/enterprise policy wins**. (Don't overthink user-vs-project ordering for specific keys — know enterprise is top and `local` is your personal override that's gitignored.)

10. **B.** It's **context** — keep it lean so it doesn't dilute attention or waste tokens.

**Score:** ___/10
