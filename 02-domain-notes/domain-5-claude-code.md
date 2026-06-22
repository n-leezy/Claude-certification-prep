# Domain 5 — Claude Code Configuration (~20%)

> Tests whether you can configure Claude Code (and agentic dev workflows) for real teams: settings, memory, permissions, hooks, subagents, skills, MCP, and automation/CI. Grounded in Anthropic's Claude Code docs. Weighting is `[COMMUNITY]`.

---

## 1. What Claude Code is
A terminal-based **agentic coding tool** that runs the agentic loop (Domain 1) against your codebase: it reads files, edits, runs commands/tests, and iterates. It's also usable **headlessly** (non-interactive) for scripting and CI. It can act as an MCP **host** (consume MCP servers) and exposes hooks, subagents, and skills.

## 2. The `.claude/` folder & configuration layers
Configuration is layered (most specific wins), typically:
- **Enterprise/managed policy** (admin-set, highest authority).
- **User settings** — `~/.claude/settings.json` (apply to you across all projects).
- **Project settings** — `.claude/settings.json` (shared with the team, committed).
- **Local project settings** — `.claude/settings.local.json` (personal, gitignored).

Common things configured: permissions/allowed tools, MCP servers, hooks, environment, model, and subagents. The `.claude/` directory in a repo is how a team standardizes Claude's behavior on that project.

## 3. Memory: `CLAUDE.md`
- **`CLAUDE.md`** files give Claude persistent project/user context (conventions, architecture, commands, do/don'ts). Claude loads them automatically.
- Hierarchy: enterprise → project (`./CLAUDE.md`, committed) → user (`~/.claude/CLAUDE.md`) → subdirectory `CLAUDE.md` files (loaded when working in that area).
- Keep it concise and high-signal (it's context — Domain 4). Use it for the things you'd otherwise repeat every session.

## 4. Permissions & security
- Claude Code asks before sensitive actions; you configure **allow/deny** rules for tools and commands (e.g., allow `Edit`, ask before `Bash`, deny network).
- **Permission modes** exist (interactive prompting vs. more autonomous modes). More autonomy = more guardrails needed.
- For automation, you can pre-approve specific tools rather than disabling all prompts blindly. Principle: **least privilege**, especially in CI where there's no human to approve.

## 5. Hooks (deterministic automation) — heavily tested
**Hooks are shell commands that run automatically at defined lifecycle events**, giving you **deterministic** control instead of relying on the model to remember (cross-ref Domain 1 hooks-vs-prompts).
- Example events: **PreToolUse** (before a tool runs — can block it), **PostToolUse** (after — e.g., auto-format/lint), **UserPromptSubmit**, **Stop/SubagentStop**, **SessionStart**, **Notification**.
- Uses: auto-run formatters/linters/tests after edits, block edits to protected paths, inject context, enforce conventions, send notifications.
- A **PreToolUse hook can deny** an action (exit code / decision), making it a hard guardrail. This is how you *guarantee* behavior.

## 6. Subagents
- **Subagents** are specialized assistants Claude Code can delegate to, each with **its own context window**, **its own system prompt**, and a **restricted toolset**.
- Defined as markdown files (e.g. in `.claude/agents/`) with a description of when to use them.
- Benefits: keep the main conversation's context clean, encapsulate expertise (e.g., a "code-reviewer" or "test-writer" agent), and parallelize. (This is the Claude Code expression of Domain 1's orchestrator/worker pattern.)

## 7. Skills
- **Agent Skills** are reusable, model-invoked capabilities: a folder with a `SKILL.md` (instructions + metadata) that Claude **auto-applies when relevant**, plus optional scripts/resources.
- They package "how we do X" so Claude applies it consistently without you re-explaining. Skills are progressively disclosed (loaded when the task matches) to save context.
- Distribute across a team by committing them; they're portable across Claude Code (and the broader Skills ecosystem).

## 8. MCP in Claude Code
- Claude Code can connect to **MCP servers** (Domain 3) to gain tools/resources/prompts — e.g., a database server, a ticketing server.
- Configured per-scope (user/project/local). MCP **prompts** can surface as slash commands; **resources** become loadable context.

## 9. Slash commands & custom commands
- Built-in slash commands manage the session (context, config, etc.).
- **Custom commands** are reusable prompt templates (markdown files) you invoke by name — standardize common workflows for the team.

## 10. Automation, headless & CI/CD
- Run Claude Code **non-interactively** (headless, e.g. `-p/--print` style invocation) to script tasks: code review on a PR, codemods, doc generation, triage.
- In **CI/CD**: pin **least-privilege permissions**, use **hooks** to enforce gates (tests must pass, no edits outside scope), and capture logs. There's no human to approve, so guardrails are mandatory.
- This maps to the reported exam scenario "integrate Claude Code into a CI/CD pipeline."

---

## Self-test (close the notes)
1. List the config layers from highest to lowest authority. Which file is committed vs. gitignored?
2. What's `CLAUDE.md` for, and why keep it concise?
3. Which hook event can **block** an action, and give two real uses for hooks.
4. What three things does a subagent get that keep it isolated from the main context?
5. What's in a Skill, and when does Claude load it?
6. You're putting Claude Code in CI with no human in the loop. Name three things you configure to keep it safe.

## Teach-it-back checklist
- [ ] I can explain hooks vs. prompts using a concrete "must always happen" example.
- [ ] I can explain how subagents and skills each manage context/expertise.
- [ ] I can describe a safe headless CI setup (permissions + hooks + logging).

## Sources
- Claude Code docs — settings, memory (`CLAUDE.md`), permissions, hooks, subagents, MCP, headless/automation: https://code.claude.com/docs and https://platform.claude.com/docs/claude-code
- Anthropic Academy — *Claude Code 101*, *Claude Code in Action*, *Introduction to Agent Skills*, *Introduction to Subagents*: https://anthropic.skilljar.com/

## Further reading (from Noah's Reader library)
- *Hooks reference* — Claude Code Docs
- *Subagents* — Claude Code Docs
- *Anatomy of the .claude/ folder* — Akshay
- *Best practices for using Claude with Claude Code* — claude.com
