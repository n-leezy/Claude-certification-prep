# Quiz — Domain 4: Context & Reliability

10 questions, answer from memory, then check the key.

---

1. "Context engineering" is best described as:
   - A. Writing one clever instruction line
   - B. Curating the whole set of tokens (system, tools, examples, history, retrieved data) so the model has the right info at the right time
   - C. Increasing the context window size
   - D. Fine-tuning the model

2. Adding lots of marginally-relevant text to the prompt tends to:
   - A. Always improve answers
   - B. Degrade performance by diluting attention ("context rot")
   - C. Have no effect
   - D. Reduce token cost

3. For prompt caching to hit, the cached prefix must be placed and formed how?
   - A. Variable content first, static last
   - B. Static content first (system, tools, fixed context), variable content last, prefix byte-identical
   - C. Order doesn't matter
   - D. Only user messages can be cached

4. Prompt caching is **most** clearly worth it when:
   - A. Every request has a totally different prompt
   - B. A large stable prefix (system + tools + docs) is reused across many calls, e.g., an agent loop
   - C. You only ever make one call
   - D. Outputs must be deterministic

5. Roughly how does prompt caching's cost model work?
   - A. Reads cost more than writes
   - B. Cache writes cost slightly more than normal tokens; cache reads are much cheaper
   - C. Both are free
   - D. Caching doubles total cost

6. A chat agent's conversation grows past the window mid-session. Best handling?
   - A. Crash
   - B. Compact/summarize older turns (keep decisions/open tasks) and continue; offload to external memory
   - C. Drop the system prompt
   - D. Switch to a smaller model

7. You have a huge, latency-insensitive extraction job over millions of docs. Two best cost levers?
   - A. Higher temperature + streaming
   - B. Message Batches API + prompt caching of the stable instruction/schema prefix
   - C. Multi-agent + bigger model
   - D. More few-shot examples + Opus everywhere

8. Best practice for handling rate limits / transient API errors?
   - A. Immediate infinite retries
   - B. Retries with exponential backoff (and idempotency on side-effecting tools)
   - C. Ignore and continue
   - D. Lower max_tokens to 1

9. You need consistent outputs where correctness matters more than cost. Which two help most?
   - A. Raise temperature; single sample
   - B. Lower temperature; self-consistency (sample N, take the majority)
   - C. Remove validation
   - D. Disable the system prompt

10. For a RAG bot, the biggest reliability risk is:
   - A. Using XML tags
   - B. Poor retrieval — garbage chunks in → garbage answers out (so invest in retrieval quality + grounding/citations)
   - C. Caching the system prompt
   - D. Streaming the response

---

## Answer key & explanations

1. **B.** Context engineering = curating the **entire** token set for relevance and form. Bigger windows (C) and fine-tuning (D) are different things.

2. **B.** Irrelevant context **dilutes attention** and degrades quality. More is not better.

3. **B.** **Static first, variable last, prefix identical.** Anything before the breakpoint must match byte-for-byte to hit.

4. **B.** Caching pays off when a **large stable prefix is reused** repeatedly (classic in agent loops/chat/doc Q&A). Useless if every prompt differs or you call once.

5. **B.** **Writes slightly pricier, reads much cheaper** (and faster) — worth it with enough reuse before the TTL expires.

6. **B.** **Compact/summarize** older turns and offload to external memory; preserve decisions and open tasks. Don't drop the system prompt.

7. **B.** **Batches API** (big discount, latency-insensitive) + **prompt caching** of the fixed instruction/schema prefix. Opus-everywhere and multi-agent raise cost.

8. **B.** **Exponential backoff** retries; ensure idempotency for side effects. Infinite immediate retries worsen rate limiting.

9. **B.** **Lower temperature** + **self-consistency** (sample several, vote) maximize correctness when cost is secondary.

10. **B.** RAG lives or dies on **retrieval quality**; pair good retrieval with grounding + citations.

**Score:** ___/10
