# Quiz — Domain 3: Tool Design & MCP Integration

10 questions, answer from memory, then check the key.

---

1. In the tool-use loop, who actually executes the tool when Claude emits a `tool_use` block?
   - A. The Claude model runs it internally
   - B. Your application executes it and returns a `tool_result`
   - C. The MCP registry
   - D. Anthropic's servers

2. Your agent keeps picking the wrong tool between `search_orders` and `lookup_order`. Best fix?
   - A. Raise temperature
   - B. Consolidate/clarify the tools and write descriptions that say exactly when to use each
   - C. Add five more tools
   - D. Force `tool_choice: none`

3. The single most common reason a model misuses a well-built function is:
   - A. The JSON Schema is too strict
   - B. An under-specified tool **description** (the description is effectively a prompt)
   - C. Too few tokens in the result
   - D. The tool name is too long

4. MCP's three core primitives are:
   - A. Tools, Resources, Prompts
   - B. Hosts, Clients, Servers
   - C. Tools, Memory, Cache
   - D. Read, Write, Execute

5. Which MCP primitive is **model-controlled** (the model decides to invoke it to take an action)?
   - A. Resources
   - B. Prompts
   - C. Tools
   - D. Roots

6. A reusable prompt template a **user** explicitly invokes (e.g., a slash command) is which MCP primitive?
   - A. Tool
   - B. Resource
   - C. Prompt
   - D. Sampling

7. Why choose MCP over hardcoded tool definitions for a database integration you'll reuse across Claude Desktop, Claude Code, and your API app?
   - A. MCP is always cheaper per token
   - B. Write the server once; any MCP-compatible host can use it (interoperability/reuse)
   - C. MCP removes the need for auth
   - D. MCP eliminates hallucination

8. Define the MCP host vs. client vs. server.
   - A. Host = your server code; client = the DB; server = the model
   - B. Host = the AI app the user uses; client = connector inside the host (1:1 to a server); server = the program exposing tools/resources/prompts
   - C. They're interchangeable terms
   - D. Host = Anthropic; client = you; server = the user

9. A tool returns a 50KB JSON blob every call and the agent degrades over a long session. Best practice?
   - A. Return only what the model needs (filter/paginate); return IDs it can drill into
   - B. Always return everything for completeness
   - C. Increase max_tokens
   - D. Disable caching

10. Two solid security practices for a **remote** MCP server:
   - A. Trust all inputs; expose secrets for convenience
   - B. Require auth and validate/scope inputs (treat tool inputs as untrusted; use roots to limit filesystem)
   - C. Run as root with no logging
   - D. Disable TLS to reduce latency

---

## Answer key & explanations

1. **B.** **Your app** executes tools and returns `tool_result`. The model only emits intent — this is the security boundary.

2. **B.** Overlapping/ambiguous tools cause wrong picks; **consolidate and clarify** with usage-guidance in descriptions. More tools (C) makes it worse.

3. **B.** The **description is a prompt** — under-specified descriptions are the top cause of misuse. Explain when/when-not, units, side effects.

4. **A.** Tools, Resources, Prompts. (B lists the *architecture* components, not primitives.)

5. **C.** **Tools** are model-controlled. Resources are application-controlled; Prompts are user-controlled.

6. **C.** A user-invoked reusable template is a **Prompt** primitive (often surfaced as a slash command).

7. **B.** MCP's value is **write-once, reuse across hosts** (interoperability + separation of concerns). It doesn't remove auth (C) or eliminate hallucination (D), and isn't inherently cheaper (A).

8. **B.** Host = the AI app; client = the 1:1 connector inside it; server = the capability provider.

9. **A.** Return **concise, relevant** results (filter/paginate; hand back IDs to drill into). Verbose results burn context and degrade performance (Domain 4 link).

10. **B.** **Require auth, validate and scope inputs**, treat inputs as untrusted, use roots to limit filesystem reach. Never expose secrets.

**Score:** ___/10
