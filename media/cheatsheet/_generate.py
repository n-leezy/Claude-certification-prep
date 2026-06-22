#!/usr/bin/env python3
"""Generate a one-page printable CCA-F cheat sheet: SVG -> PDF + PNG.
Run: python3 _generate.py   (needs `pip install cairosvg`)"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 794, 1123  # A4 portrait @ ~96dpi
INK="#1f2430"; MUTED="#5b6472"; ACCENT="#d97757"; BLUE="#3b6fd4"; GREEN="#3a9b6e"
PANEL="#f4f1ec"; LINE="#d8d2c8"; WHITE="#ffffff"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
S=[]
def rect(x,y,w,h,fill,stroke="none",rx=8): S.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>')
def text(x,y,t,size=11,fill=INK,weight="400",anchor="start"):
    S.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(t)}</text>')
def bullets(x,y,items,size=10.3,lh=15,fill=INK,maxw=44):
    cy=y
    for it in items:
        # simple wrap
        words=it.split(); line=""; first=True
        for w in words:
            if len(line)+len(w)+1>maxw:
                text(x+(0 if first else 9), cy, ("• " if first else "")+line, size, fill, "600" if first and it.endswith(":") else "400")
                first=False; cy+=lh; line=w
            else:
                line=(line+" "+w).strip()
        text(x+(0 if first else 9), cy, ("• " if first else "")+line, size, fill)
        cy+=lh
    return cy

S.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">')
rect(0,0,W,H,WHITE)
# header
rect(0,0,W,64,ACCENT,rx=0)
text(28,30,"Claude Certified Architect — Foundations (CCA-F)",19,WHITE,"700")
text(28,50,"One-page cheat sheet · UNOFFICIAL community prep · verify against anthropic.com",10.5,"#ffe9e0")

COLW=366; LX=28; RX=400; top=84

# --- Exam facts box (full width) ---
rect(LX,top,W-56,72,PANEL,LINE)
text(LX+12,top+18,"EXAM SNAPSHOT",10,ACCENT,"700")
text(LX+12,top+36,"OFFICIAL: CCA-F = Anthropic's 1st Claude cert · for solution architects · on Anthropic Academy/Skilljar · access via free Partner Network",8.8,INK)
text(LX+12,top+50,"COMMUNITY (verify): ~60 scenario MCQs · 120 min · scaled 100–1000, pass ~720 · ~$99/attempt · ~2-yr validity",8.8,MUTED)
text(LX+12,top+64,"Theme across all domains: least complexity that works · enforce hard rules in code (hooks) · curate context · test yourself to study",8.8,BLUE)

y=top+92
def domain_box(x,y,w,h,tag,title,color,items):
    rect(x,y,w,h,WHITE,LINE)
    rect(x,y,w,22,color,rx=8); rect(x,y+14,w,8,color,rx=0)
    text(x+10,y+15,tag+" · "+title,10.5,WHITE,"700")
    bullets(x+10,y+38,items,9.6,13.5,INK,52)

# D1
domain_box(LX,y,COLW,196,"D1","Agentic Architecture (~27%)",ACCENT,[
 "Workflow = predefined code paths; Agent = LLM directs its own loop",
 "Patterns: chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer",
 "Agentic loop: gather context > act (tools) > verify > repeat; always a STOP condition",
 "Default single-agent; multi-agent only for broad/parallel work (~15x tokens)",
 "#1 multi-agent failure: vague delegation; give subagents objective+scope+tools+format",
 "Workers return condensed summaries; persist state externally for long runs",
 "Hard requirement? Use a deterministic hook, not a prompt line",
])
# D2
domain_box(RX,y,COLW,196,"D2","Prompt Engineering (~20%)",BLUE,[
 "Ladder: clear+direct > examples > chain-of-thought > XML tags > role > prefill > chain",
 "Few-shot examples: relevant, diverse, delimited (avoid one-answer bias)",
 "Reliable JSON: tool whose input_schema = output schema, force it, then validate+repair",
 "Prefill assistant with { to force JSON / skip preamble",
 "Cut hallucination: allow 'not found', answer only from docs, quote/cite",
 "Durable rules in system prompt (also helps caching)",
 "Evaluate prompts with an eval set; change one variable at a time",
])
y2=y+208
# D3
domain_box(LX,y2,COLW,196,"D3","Tools & MCP (~18%)",GREEN,[
 "Loop: send tool defs > model emits tool_use > YOUR app runs it > return tool_result",
 "Your app executes tools (not the model) = the security boundary",
 "Good tool: clear name, rich description (=a prompt), typed schema, concise results",
 "MCP = open standard, 'USB-C for AI'. Host > Client (1:1) > Server",
 "3 primitives: Tools (model), Resources (app), Prompts (user)",
 "Use MCP to write once, reuse across hosts; local=stdio, remote=HTTP/SSE",
 "Remote server security: require auth, validate/scope inputs (roots)",
])
# D4
domain_box(RX,y2,COLW,196,"D4","Context & Reliability (~15%)",ACCENT,[
 "Context engineering = curate the whole token set; window is scarce ('context rot')",
 "Prompt caching: static prefix FIRST, byte-identical, variable query LAST",
 "Cache writes slightly pricier; reads much cheaper+faster (wins in agent loops)",
 "Long sessions: compact/summarize old turns + external memory",
 "Reliability: validate+retry, exponential backoff, self-consistency, evals",
 "Cost/latency: Batches API, prompt caching, model routing, streaming",
 "RAG quality is bounded by retrieval quality + grounding",
])
y3=y2+208
# D5
domain_box(LX,y3,COLW,196,"D5","Claude Code (~20%)",BLUE,[
 "Terminal agentic coding tool; also runs headless for CI/automation",
 "Config layers: enterprise/managed (top) > project (committed) > local (gitignored)",
 "CLAUDE.md = persistent auto-loaded memory; keep lean; NEVER secrets",
 "Hooks = deterministic lifecycle commands; PreToolUse can BLOCK; PostToolUse auto-lint",
 "Subagents: own context window + system prompt + restricted tools",
 "Skills = SKILL.md folder, loaded progressively when relevant",
 "Headless CI (no human): least privilege + hooks + logging are mandatory",
])
# Study method box
rect(RX,y3,COLW,196,PANEL,LINE)
text(RX+10,y3+18,"HOW TO STUDY (evidence-based)",10.5,GREEN,"700")
bullets(RX+10,y3+38,[
 "Retrieve, don't re-read: testing beats rereading (~50% more retained)",
 "Space reviews over days (flashcards 'due' pile each session)",
 "Interleave domains (quiz mixed mode, full exams)",
 "Explain it back (Feynman) using each note's teach-it-back list",
 "Simulate: 2 timed 60-Q exams; remediate every miss",
 "Readiness: >=80% per-domain quiz, >=45/60 on a fresh exam",
],9.6,13.5,INK,52)

# footer
text(W/2,H-22,"MIT-licensed · 'Claude' & 'Claude Certified Architect' are trademarks of Anthropic PBC · Open the study hub (index.html) for interactive flashcards & quizzes",7.6,MUTED,"400","middle")
S.append("</svg>")

svg="\n".join(S)
open(os.path.join(HERE,"cca-f-cheatsheet.svg"),"w").write(svg)
print("wrote SVG")
try:
    import cairosvg
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=os.path.join(HERE,"cca-f-cheatsheet.pdf"))
    cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(HERE,"cca-f-cheatsheet.png"), scale=2)
    print("wrote PDF + PNG")
except Exception as e:
    print("export skipped:",e)
