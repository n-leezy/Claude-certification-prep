# Domain 2 — Prompt Engineering & Structured Output (~20%)

> Tests whether you can get **correct, reliable, parseable** outputs from Claude in production. Grounded in Anthropic's prompt-engineering docs. Blueprint weighting is `[COMMUNITY]`.

---

## 1. The prompt-engineering hierarchy (try in this order)

Anthropic recommends escalating complexity only as needed:
1. **Be clear, direct, and detailed.** Treat Claude like a brilliant new hire who knows nothing about your context. Spell out the goal, audience, format, and what *not* to do. Vague prompts are the #1 cause of bad outputs.
2. **Use examples (multishot).** Show 3–5 diverse, relevant examples of input→output. Examples are the single most powerful lever for matching a format or style. Wrap them in tags (e.g. `<example>`).
3. **Let Claude think (chain of thought).** For complex reasoning, tell it to think step by step (optionally inside `<thinking>` tags). Improves accuracy on multi-step problems. With **extended thinking** models, give high-level direction and let it reason; don't over-prescribe steps.
4. **Use XML tags** to structure the prompt — separate instructions, context, examples, and input (e.g. `<instructions>`, `<document>`, `<example>`). Reduces the model mixing up parts of the prompt.
5. **Assign a role via the system prompt.** Setting a role ("You are a senior tax accountant…") tunes tone and expertise.
6. **Prefill Claude's response** to control format/start (e.g., prefill `{` to force JSON, or prefill a tag to skip preamble).
7. **Chain prompts** for complex multi-stage tasks (hand off to Domain 1 workflows).

## 2. Clear & direct — the specifics
- State the **task, context, audience, tone, length, and format** explicitly.
- Use **sequential steps** (numbered) when order matters.
- Tell it what **to do** rather than only what not to do ("respond in Spanish" beats "don't use English").
- Provide the **why**: explaining the purpose helps Claude make better judgment calls on edge cases.

## 3. Examples (multishot prompting)
- **Relevant** (mirror your real inputs), **diverse** (cover edge cases, avoid unintended patterns), and **clearly delimited**.
- More examples → better adherence, especially for format. 3–5 is a common sweet spot; complex tasks benefit from more.
- Watch for **bias**: if all your examples have the same answer, the model may parrot it.

## 4. Chain of thought (CoT) & extended thinking
- CoT helps on math, logic, multi-constraint, and analysis tasks. Costs latency/tokens; skip it for simple tasks.
- **Structured CoT:** ask for reasoning in `<thinking>` and the answer in `<answer>` so you can parse/discard the reasoning.
- **Extended thinking** (a model capability): the model produces internal reasoning before answering. Best practice — give it the *goal* and room to think, rather than micro-managing each step. Don't put words in its "thinking."

## 5. System prompts & role prompting
- The **system prompt** sets persistent behavior, role, rules, and guardrails; the **user turn** carries the task/data.
- Put durable instructions (role, policies, output contract) in the system prompt; put per-request data in the user message. This also maximizes prompt-cache hits (Domain 4).

## 6. Structured output — getting reliable JSON
This is heavily tested because it's where production breaks.
- **Specify the exact schema** in the prompt (field names, types, allowed values) and give an example object.
- **Prefill `{`** (or the opening of your structure) to force the model straight into JSON with no prose preamble.
- **Tool use / "JSON mode" via tools:** define a tool whose `input_schema` *is* your desired output schema, and force the model to call it. The API then returns arguments matching the schema — the most reliable way to get structured data. (This connects to Domain 3.)
- **Stop sequences** to cut off generation after the structure closes.
- **Validate** the result against your schema and **retry/repair** on failure — never assume valid JSON.
- Keep schemas as **flat and simple** as the task allows; deeply nested/ambiguous schemas raise error rates.

## 7. Reducing hallucinations & boosting accuracy
- **Give an out:** allow "I don't know" / "not found in the document" so the model isn't forced to invent.
- **Ground in provided context:** instruct it to answer *only* from the supplied documents, and to **quote** supporting text first (then answer) for document Q&A.
- **Ask for citations** to source spans.
- **Lower stakes of guessing:** verification steps, evaluator prompts, and self-consistency (sample multiple times, take the majority) for high-stakes outputs.

## 8. Prompt templates & variables
- Separate the **fixed template** (instructions) from **variable inputs** (user data), typically with XML tags. Improves consistency, makes caching effective, and lets you test the template independently.

## 9. Evaluating prompts
- Build an **eval set** of representative inputs with known-good outputs.
- Define **graders** (exact match, schema-valid, LLM-as-judge against a rubric).
- Change one thing at a time; measure. "It looks better" is not an eval.

---

## Self-test (close the notes)
1. List the prompt-engineering escalation ladder in order.
2. What three properties should your few-shot examples have?
3. Give two reliable techniques to force valid JSON, and say which is most robust.
4. How do you cut hallucinations in document Q&A? Name three tactics.
5. Where do role/policy instructions go vs. per-request data, and why does that also help caching?
6. When should you NOT use chain of thought?

## Teach-it-back checklist
- [ ] I can explain why "tool with input_schema = output schema" is the most reliable structured-output method.
- [ ] I can explain the "brilliant new hire" framing for clarity.
- [ ] I can describe an eval setup that would tell me prompt A beats prompt B.

## Sources
- Anthropic docs — *Prompt engineering overview* and sub-pages (be clear & direct, multishot, chain of thought, system prompts, prefilling, use XML tags, reduce hallucinations): https://platform.claude.com/docs (Build with Claude → Prompt engineering)
- Anthropic docs — *Increase output consistency / JSON*: https://platform.claude.com/docs
- Anthropic — *Claude 4 prompt engineering best practices* (extended thinking guidance): https://www.anthropic.com/engineering
