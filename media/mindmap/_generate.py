#!/usr/bin/env python3
"""Generate a syllabus mind-map: SVG + PNG. Run: python3 _generate.py"""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
INK="#1f2430";MUTED="#5b6472";WHITE="#ffffff"
COL={"D1":"#d97757","D2":"#3b6fd4","D3":"#3a9b6e","D4":"#b4862f","D5":"#7a5bd0"}
TREE=[
 ("D1","Agentic Architecture",["Workflows vs agents","5 patterns (chain/route/parallel/orch/eval)","Agentic loop + stop conditions","Single vs multi-agent","Orchestrator–subagents","Hooks vs prompts"]),
 ("D2","Prompt Engineering",["Clarity ladder","Few-shot (diverse!)","Chain-of-thought","Structured output via tools","Anti-hallucination","Evals"]),
 ("D3","Tools & MCP",["Tool-use loop","Tool design = description","MCP host/client/server","3 primitives","Local vs remote","Server security"]),
 ("D4","Context & Reliability",["Context engineering","Prompt caching","Compaction + memory","Backoff + retries","Self-consistency","RAG grounding"]),
 ("D5","Claude Code",["Config layers","CLAUDE.md memory","Hooks (Pre/Post)","Subagents","Skills","Headless CI guardrails"]),
]
W,H=1100,720
def esc(s):return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
S=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">']
S.append(f'<rect width="{W}" height="{H}" fill="{WHITE}"/>')
S.append(f'<text x="40" y="40" font-size="22" font-weight="700" fill="{INK}">CCA-F Syllabus Mind-Map</text>')
S.append(f'<text x="40" y="62" font-size="12" fill="{MUTED}">Unofficial · weights community-reported · the spine of what to learn</text>')
# root
rx,ry=80,360
S.append(f'<rect x="{rx}" y="{ry-26}" width="150" height="52" rx="14" fill="{INK}"/>')
S.append(f'<text x="{rx+75}" y="{ry-2}" text-anchor="middle" font-size="15" font-weight="700" fill="{WHITE}">CCA-F</text>')
S.append(f'<text x="{rx+75}" y="{ry+16}" text-anchor="middle" font-size="11" fill="#c9cdd6">5 domains</text>')
n=len(TREE); band=H/n
for i,(tag,name,leaves) in enumerate(TREE):
    cy=band*i+band/2+20
    dx,dw=320,210
    col=COL[tag]
    # connector root->domain
    S.append(f'<path d="M{rx+150},{ry} C 250,{ry} 250,{cy} {dx},{cy}" stroke="{col}" stroke-width="2.5" fill="none"/>')
    S.append(f'<rect x="{dx}" y="{cy-20}" width="{dw}" height="40" rx="12" fill="{col}"/>')
    S.append(f'<text x="{dx+12}" y="{cy+5}" font-size="13.5" font-weight="700" fill="{WHITE}">{esc(tag+" · "+name)}</text>')
    # leaves
    lx=dx+dw+40; m=len(leaves); lb=band/m
    for j,leaf in enumerate(leaves):
        ly=band*i+lb*j+lb/2+20
        S.append(f'<path d="M{lx-40},{cy} C {lx-20},{cy} {lx-20},{ly} {lx},{ly}" stroke="{col}" stroke-width="1.5" fill="none" opacity="0.7"/>')
        S.append(f'<circle cx="{lx}" cy="{ly}" r="3" fill="{col}"/>')
        S.append(f'<text x="{lx+8}" y="{ly+4}" font-size="11.5" fill="{INK}">{esc(leaf)}</text>')
S.append("</svg>")
svg="\n".join(S)
open(os.path.join(HERE,"syllabus-mindmap.svg"),"w").write(svg)
print("wrote SVG")
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(),write_to=os.path.join(HERE,"syllabus-mindmap.png"),scale=2)
    print("wrote PNG")
except Exception as e:
    print("PNG skipped:",e)
