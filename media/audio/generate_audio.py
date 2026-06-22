#!/usr/bin/env python3
"""
Generate spoken audio overviews for the CCA-F prep kit.

Audio engine: ElevenLabs (high quality) if ELEVENLABS_API_KEY is set,
otherwise an automatic fallback to edge-tts (free, no key), then gTTS.

SWAP THE ENGINE IN ONE PLACE: edit `synth()` below — everything else
calls that single function. To use ElevenLabs, just export your key:

    export ELEVENLABS_API_KEY=sk_...        # never commit this
    python3 generate_audio.py

Outputs (in this folder):
    overview-00-intro.mp3, overview-01-agentic.mp3 ... overview-05-claude-code.mp3
    podcast-full-overview.mp3   (two alternating voices)

NOTE: secrets are read from the environment only and are never written to disk.
"""
import os, sys, subprocess, tempfile, urllib.request, json

HERE = os.path.dirname(os.path.abspath(__file__))

# ElevenLabs voice IDs (override via env if you like)
NARRATOR   = os.environ.get("EL_VOICE_NARRATOR", "EXAVITQu4vr4xnSDxMaL")  # Sarah
HOST_A     = os.environ.get("EL_VOICE_HOST_A",   "JBFqnCBsd6RMkjVDRZzb")  # George
HOST_B     = os.environ.get("EL_VOICE_HOST_B",   "EXAVITQu4vr4xnSDxMaL")  # Sarah
EL_MODEL   = os.environ.get("EL_MODEL", "eleven_multilingual_v2")

# ------------------------------------------------------------------
# THE ONE FUNCTION TO SWAP. Returns True on success, writes mp3 to out.
# ------------------------------------------------------------------
def synth(text, out_path, voice=NARRATOR):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        try:
            return _elevenlabs(text, out_path, voice, key)
        except Exception as e:
            print(f"  [ElevenLabs failed: {e}] falling back to free TTS")
    return _free_tts(text, out_path)

def _elevenlabs(text, out_path, voice, key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    body = json.dumps({
        "text": text, "model_id": EL_MODEL,
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True},
    }).encode()
    req = urllib.request.Request(url, data=body, method="POST",
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(out_path, "wb") as f:
        f.write(data)
    return True

def _free_tts(text, out_path):
    # 1) edge-tts (no key, good quality)
    try:
        import asyncio, edge_tts
        async def go():
            c = edge_tts.Communicate(text, "en-US-AriaNeural")
            await c.save(out_path)
        asyncio.run(go()); return True
    except Exception as e:
        print(f"  [edge-tts unavailable: {e}]")
    # 2) gTTS
    try:
        from gtts import gTTS
        gTTS(text=text, lang="en").save(out_path); return True
    except Exception as e:
        print(f"  [gTTS unavailable: {e}]")
    return False

def concat_mp3(parts, out_path):
    """Concatenate mp3 segments via ffmpeg (re-encode for safety)."""
    listfile = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False)
    for p in parts: listfile.write(f"file '{p}'\n")
    listfile.close()
    subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",listfile.name,
                    "-c:a","libmp3lame","-q:a","4",out_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.unlink(listfile.name)

# ------------------------------------------------------------------
# Narration scripts
# ------------------------------------------------------------------
DISCLAIMER = ("Quick note: this is unofficial, community-built prep. "
              "Anthropic has confirmed the certification exists and how to access it, "
              "but the detailed exam format and domain weights are community-reported, so verify the specifics. ")

OVERVIEWS = {
"overview-00-intro": (
"Welcome to your prep for the Claude Certified Architect, Foundations exam — Anthropic's first official Claude technical "
"certification, launched in March twenty twenty-six alongside the Claude Partner Network. " + DISCLAIMER +
"Here's the shape of it. The exam is aimed at solution architects building production applications with Claude. "
"It's delivered through Anthropic Academy on Skilljar, and at launch it's accessed through the free Claude Partner Network. "
"Community sources report about sixty scenario-based multiple-choice questions in a hundred-and-twenty-minute window, "
"with a scaled passing score around seven-twenty out of a thousand. "
"The material breaks into five domains: agentic architecture and orchestration; prompt engineering and structured output; "
"tool design and the Model Context Protocol; context and reliability; and Claude Code configuration. "
"The smartest way to study isn't to re-read these notes — it's to test yourself. Use the flashcards and quizzes constantly, "
"space your reviews over several days, and mix the domains together. Let's get into it."),

"overview-01-agentic": (
"Domain one: agentic architecture and orchestration — the biggest slice of the exam, because this is where production systems break. "
"Start with one distinction. A workflow runs language models and tools along predefined code paths that you wrote. "
"An agent lets the model dynamically direct its own process, deciding which tools to call, in a loop, until the goal is met. "
"The golden rule: use the simplest thing that works, and only add complexity when it clearly improves outcomes. "
"Many problems just need a single well-prompted call. Know the workflow patterns — prompt chaining, routing, parallelization, "
"orchestrator-workers, and evaluator-optimizer — and when each fits. "
"The agentic loop is gather context, take action, verify work, repeat — always with a stop condition so it can't run forever. "
"Default to a single agent with good tools. Reach for multi-agent only when the task is broad, open-ended, and parallelizable, "
"because it can burn many times more tokens. And remember the number one multi-agent failure: vague delegation. "
"Every subagent needs a specific objective, scope, tools, and output format. Finally: if a requirement absolutely must hold, "
"enforce it in deterministic code — a hook — not a polite line in a prompt."),

"overview-02-prompt": (
"Domain two: prompt engineering and structured output. This tests whether you can get correct, parseable, reliable outputs. "
"Climb the ladder in order: first be clear, direct, and detailed — treat Claude like a brilliant new hire who knows nothing about your context. "
"Then add examples; few-shot examples are your most powerful lever for matching a format, as long as they're relevant and diverse — "
"not all the same answer, which creates bias. Then, only for genuinely hard reasoning, let it think step by step. "
"Use XML tags to separate instructions, context, and data; put durable rules in the system prompt; and prefill the response to control its start. "
"For structured output, the most reliable trick is to define a tool whose input schema is exactly your desired output schema, force the call, "
"then validate and repair. To cut hallucinations, give the model an out like 'not found,' ground it in the provided documents, and ask it to quote its sources. "
"And never trust 'it seems better' — build an eval set and change one thing at a time."),

"overview-03-tools": (
"Domain three: tool design and the Model Context Protocol. First, the tool-use loop. You send Claude a list of tool definitions; "
"it returns a tool-use request with JSON arguments; your application executes the tool and returns the result; Claude continues. "
"The key point: the model never runs your tool — your code does. That's the security boundary. "
"What makes a good tool? A clear name, a rich description — because the description is effectively a prompt — a well-typed input schema, "
"and concise, useful results. Fewer, well-chosen tools beat many overlapping ones. "
"Now MCP: an open standard for connecting AI apps to external systems — think USB-C for AI. Learn the architecture: host, client, server. "
"And memorize the three core primitives and who controls each: tools are model-controlled, resources are application-controlled, "
"and prompts are user-controlled. Use MCP when you want to write an integration once and reuse it across many hosts. "
"For any remote server, require authentication and treat every input as untrusted."),

"overview-04-context": (
"Domain four: context and reliability. Prompt engineering writes the instruction; context engineering curates the entire set of tokens — "
"system prompt, tools, examples, history, retrieved data — so the model has the right information, in the right form, at the right time. "
"The context window is finite and scarce; piling in marginally-relevant text actually hurts, by diluting attention. So retrieve just in time and curate hard. "
"Prompt caching is a high-value topic: cache a stable prefix — system prompt, tools, fixed context — placed first and byte-identical, "
"with the variable user query last. Cache writes cost a little more; cache reads are much cheaper and faster, which is why caching dominates agent economics. "
"For long sessions, compact older turns and offload state to external memory. For reliability: validate outputs against a schema and retry, "
"use exponential backoff on rate limits, lower the temperature and use self-consistency when correctness matters, and route easy work to a smaller, faster model."),

"overview-05-claude-code": (
"Domain five: Claude Code configuration. Claude Code is a terminal-based agentic coding tool that runs the agentic loop over your codebase, "
"and it also runs headless for automation and CI. Configuration is layered: enterprise or managed policy sits at the top and can't be overridden; "
"project settings in dot-claude slash settings-dot-json are committed and shared with the team; the local settings file is your personal, gitignored override. "
"CLAUDE-dot-md is persistent memory — conventions, architecture, commands — loaded automatically; keep it lean, and never put secrets in it. "
"Hooks are shell commands that fire on lifecycle events for deterministic control — a PreToolUse hook can actually block an action, "
"and a PostToolUse hook can auto-run your linter. That's how you guarantee behavior instead of hoping the model remembers. "
"Subagents get their own context window, system prompt, and restricted toolset. Skills are folders with a SKILL-dot-md, "
"loaded only when relevant. And for headless use in CI, with no human to approve, least-privilege permissions, enforcement hooks, and logging are mandatory."),
}

PODCAST = [
("A", "Welcome in. Today we're doing a fast, friendly tour of the Claude Certified Architect, Foundations exam. "
       "Before anything else: this is unofficial prep."),
("B", "Right — Anthropic has confirmed the certification exists, who it's for, and that it's delivered through Anthropic Academy and accessed via the partner network. "
      "But the nitty-gritty format and the domain weights? Those are community-reported. Verify them."),
("A", "Good caveat. So big picture — who's this exam for?"),
("B", "Solution architects building production applications with Claude. It's not a trivia quiz; it's scenario-based. "
      "You're handed a realistic situation and asked for the best design decision, and why the others are worse."),
("A", "And it's five domains. The heavyweight is agentic architecture."),
("B", "Exactly. The mantra there is 'simplest thing that works.' Don't reach for an agent when a workflow will do, and don't reach for multi-agent "
      "unless the task is broad and parallelizable — because multi-agent can cost many times more tokens."),
("A", "The bit that trips people up is delegation."),
("B", "Every subagent needs a crisp objective, scope, tools, and output format. Vague delegation is the number one failure mode. "
      "And if something absolutely must happen, enforce it with a hook, not a sentence in a prompt."),
("A", "Domain two, prompt engineering. Give me the one-liner."),
("B", "Clarity first, then examples, then thinking. And for structured output, define a tool whose schema is your output, force it, and validate. "
      "It's the most reliable way to get clean JSON."),
("A", "Domain three is tools and MCP. The thing to memorize?"),
("B", "Three MCP primitives and who controls them: tools are model-controlled, resources are app-controlled, prompts are user-controlled. "
      "And remember your app executes tools, not the model — that's the security boundary."),
("A", "Domain four, context and reliability."),
("B", "Treat the context window as scarce. Curate it, retrieve just in time, and cache the stable prefix — static content first, byte-identical, "
      "variable query last. Reads are cheap, writes slightly pricier, which is why caching wins in agent loops."),
("A", "And domain five, Claude Code."),
("B", "Layered config, with enterprise policy on top. CLAUDE-dot-md for memory — no secrets. Hooks for deterministic guarantees. "
      "Subagents for isolation. And in CI with no human, least privilege plus hooks plus logging, every time."),
("A", "How should someone actually study all this?"),
("B", "Test yourself constantly, space it over days, and mix the domains. Don't just re-read — retrieve. That's the whole game."),
("A", "Perfect. Take the practice exams, trust the struggle, and good luck."),
]

def main():
    os.chdir(HERE)
    engine = "ElevenLabs" if os.environ.get("ELEVENLABS_API_KEY") else "free TTS (edge-tts/gTTS)"
    print(f"Engine: {engine}")
    # Per-domain overviews
    for name, text in OVERVIEWS.items():
        out = name + ".mp3"
        print(f"→ {out}")
        if not synth(text, out, NARRATOR):
            print("   FAILED — no TTS engine available.");
    # Podcast (two voices, concatenated)
    print("→ podcast-full-overview.mp3 (two voices)")
    seg_paths = []
    ok = True
    for idx, (spk, line) in enumerate(PODCAST):
        seg = os.path.join(tempfile.gettempdir(), f"pod_{idx:02d}.mp3")
        voice = HOST_A if spk == "A" else HOST_B
        if synth(line, seg, voice):
            seg_paths.append(seg)
        else:
            ok = False; break
    if ok and seg_paths:
        try:
            concat_mp3(seg_paths, "podcast-full-overview.mp3")
        except Exception as e:
            print(f"  concat failed ({e})")
    print("Done.")

if __name__ == "__main__":
    main()
