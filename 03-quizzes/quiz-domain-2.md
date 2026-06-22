# Quiz — Domain 2: Prompt Engineering & Structured Output

10 questions, answer from memory, then check the key.

---

1. You need Claude to reliably return data matching a strict JSON schema for a pipeline. Most robust method?
   - A. Ask politely for JSON in the system prompt
   - B. Define a tool whose `input_schema` is your output schema and force `tool_choice`
   - C. Lower the temperature to 0
   - D. Add "return only JSON" at the end

2. Outputs are inconsistent. According to the prompt-engineering ladder, what should you try **first**?
   - A. Fine-tune a model
   - B. Build a multi-agent system
   - C. Make the prompt clearer, more direct, and more detailed
   - D. Add chain-of-thought

3. Your few-shot examples all happen to end with the answer "approved." What's the risk?
   - A. Higher cost only
   - B. The model learns a bias and over-predicts "approved"
   - C. Nothing; more examples are always better
   - D. The model ignores examples

4. For a document Q&A bot that must not invent facts, which combination best reduces hallucination?
   - A. Higher temperature + longer outputs
   - B. Allow "not found," instruct it to answer only from the document, and ask it to quote supporting text
   - C. Remove the system prompt
   - D. Force a tool call

5. Where should durable role/policy instructions live, and why does it also help caching?
   - A. In each user message; it doesn't affect caching
   - B. In the system prompt; a stable prefix maximizes prompt-cache hits
   - C. In the tool results
   - D. In the assistant prefilled text

6. You want Claude to skip preamble and start a response with `{`. Best technique?
   - A. Stop sequence
   - B. Prefill the assistant turn with `{`
   - C. Raise max_tokens
   - D. Add another example

7. When is chain-of-thought the *wrong* choice?
   - A. Multi-step math
   - B. A simple, single-step classification where latency/cost matter
   - C. Complex analysis
   - D. Logic puzzles

8. Why wrap instructions, context, and examples in distinct XML tags?
   - A. It reduces token cost to zero
   - B. It helps the model not confuse the different parts of the prompt
   - C. It's required by the API
   - D. It disables hallucination

9. With an extended-thinking model on a hard problem, the best prompting approach is to:
   - A. Prescribe each reasoning step in detail
   - B. Give the goal and room to think, rather than micromanaging steps
   - C. Forbid any reasoning
   - D. Always prefill the thinking

10. You changed three things in a prompt and it "seems better." What's the methodological problem?
   - A. None
   - B. No eval set + multiple simultaneous changes means you can't attribute the effect
   - C. You should have used more emojis
   - D. Temperature was too low

---

## Answer key & explanations

1. **B.** A forced tool call whose schema *is* the output schema is the most reliable structured-output method — the API returns schema-matching arguments. A/D are soft; temperature (C) helps consistency but doesn't guarantee schema validity. Always validate + repair regardless.

2. **C.** The ladder starts with **clear, direct, detailed** prompts. Fine-tuning and multi-agent are heavy last resorts; CoT comes later and only for reasoning-heavy tasks.

3. **B.** Non-diverse examples induce **bias**; the model parrots the pattern. Examples must be diverse and representative.

4. **B.** Give it an out ("not found"), ground it in the document, and have it quote support — the canonical anti-hallucination combo. Higher temperature (A) worsens it.

5. **B.** Durable instructions go in the **system prompt**; keeping the stable content first/identical maximizes cache hits (Domain 4 link).

6. **B.** **Prefilling** the assistant turn forces the format and skips preamble. Stop sequences end generation; they don't control the start.

7. **B.** Skip CoT for **simple single-step tasks** where it just adds latency/cost. It helps on A/C/D.

8. **B.** XML tags **delineate parts** so the model doesn't mix instructions with data. They don't zero out cost or disable hallucination, and aren't strictly required.

9. **B.** With extended thinking, give **direction and space**, don't over-prescribe or script the internal reasoning.

10. **B.** Without an **eval set** and with **multiple changes at once**, you can't tell what helped. Change one variable; measure against known-good outputs.

**Score:** ___/10
