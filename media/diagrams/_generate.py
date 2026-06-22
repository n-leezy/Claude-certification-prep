#!/usr/bin/env python3
"""
Generate the CCA-F concept diagrams in three formats from one spec:
  - <name>.excalidraw  (editable scene; open at excalidraw.com)
  - <name>.svg         (embeddable export)
  - <name>.png         (embeddable export; needs `pip install cairosvg`)

Run:  python3 _generate.py
Re-run any time you tweak a diagram spec below.
"""
import json, random, math, os

random.seed(7)
OUT = os.path.dirname(os.path.abspath(__file__))

# ---- palette (light theme, prints well) ----
INK   = "#1f2430"
MUTED = "#5b6472"
LINE  = "#9aa3af"
ACCENT= "#d97757"
BLUE  = "#3b6fd4"
GREEN = "#3a9b6e"
PANEL = "#f4f1ec"
WHITE = "#ffffff"

def _nonce(): return random.randint(1, 2**31)

# ---------- Excalidraw element builders ----------
def el_rect(eid, x, y, w, h, bg=PANEL, stroke=INK, rounded=True):
    return {
        "id": eid, "type": "rectangle", "x": x, "y": y, "width": w, "height": h,
        "angle": 0, "strokeColor": stroke, "backgroundColor": bg, "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "solid", "roughness": 1, "opacity": 100,
        "groupIds": [], "frameId": None, "roundness": {"type": 3} if rounded else None,
        "seed": _nonce(), "versionNonce": _nonce(), "version": 1, "isDeleted": False,
        "boundElements": [], "updated": 1, "link": None, "locked": False,
    }

def el_ellipse(eid, x, y, w, h, bg=ACCENT, stroke=ACCENT):
    e = el_rect(eid, x, y, w, h, bg, stroke); e["type"] = "ellipse"; e["roundness"] = None
    return e

def el_text(eid, x, y, text, size=16, color=INK, w=None, align="center"):
    lines = text.split("\n")
    w = w if w else max(len(l) for l in lines) * size * 0.6
    return {
        "id": eid, "type": "text", "x": x, "y": y, "width": w, "height": len(lines)*(size+6),
        "angle": 0, "strokeColor": color, "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 1, "opacity": 100, "groupIds": [],
        "frameId": None, "roundness": None, "seed": _nonce(), "versionNonce": _nonce(), "version": 1,
        "isDeleted": False, "boundElements": [], "updated": 1, "link": None, "locked": False,
        "text": text, "fontSize": size, "fontFamily": 2, "textAlign": align, "verticalAlign": "top",
        "containerId": None, "originalText": text, "lineHeight": 1.25,
    }

def el_arrow(eid, x1, y1, x2, y2, color=MUTED, dashed=False):
    return {
        "id": eid, "type": "arrow", "x": x1, "y": y1, "width": abs(x2-x1), "height": abs(y2-y1),
        "angle": 0, "strokeColor": color, "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed" if dashed else "solid", "roughness": 1, "opacity": 100,
        "groupIds": [], "frameId": None, "roundness": {"type": 2}, "seed": _nonce(),
        "versionNonce": _nonce(), "version": 1, "isDeleted": False, "boundElements": [], "updated": 1,
        "link": None, "locked": False, "points": [[0, 0], [x2-x1, y2-y1]], "lastCommittedPoint": None,
        "startBinding": None, "endBinding": None, "startArrowhead": None, "endArrowhead": "arrow",
    }

def write_excalidraw(name, elements):
    doc = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
           "elements": elements, "appState": {"viewBackgroundColor": WHITE, "gridSize": None}, "files": {}}
    with open(os.path.join(OUT, name + ".excalidraw"), "w") as f:
        json.dump(doc, f, indent=1)

# ---------- tiny SVG renderer from the same node/edge spec ----------
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def render_svg(name, W, H, boxes, arrows, title, ellipses=None):
    ellipses = ellipses or []
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">']
    out.append(f'<rect width="{W}" height="{H}" fill="{WHITE}"/>')
    out.append('<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">'
               f'<path d="M0,0 L8,3 L0,6 Z" fill="{MUTED}"/></marker></defs>')
    out.append(f'<text x="{W/2}" y="34" text-anchor="middle" font-size="22" font-weight="700" fill="{INK}">{esc(title)}</text>')
    for a in arrows:
        x1,y1,x2,y2 = a["p"]; dash = ' stroke-dasharray="6 5"' if a.get("dash") else ''
        col = a.get("color", MUTED)
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2"{dash} marker-end="url(#ah)"/>')
        if a.get("label"):
            mx,my=(x1+x2)/2,(y1+y2)/2
            out.append(f'<rect x="{mx-len(a["label"])*3.4-4}" y="{my-12}" width="{len(a["label"])*6.8+8}" height="18" rx="4" fill="{WHITE}"/>')
            out.append(f'<text x="{mx}" y="{my+1}" text-anchor="middle" font-size="11" fill="{MUTED}">{esc(a["label"])}</text>')
    for e in ellipses:
        x,y,w,h = e["r"]; out.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{e.get("bg",ACCENT)}" stroke="{e.get("st",ACCENT)}" stroke-width="2"/>')
        _svg_text(out, e["t"], x+w/2, y+h/2, e.get("fs",15), e.get("tc",WHITE))
    for b in boxes:
        x,y,w,h = b["r"]
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{b.get("bg",PANEL)}" stroke="{b.get("st",INK)}" stroke-width="2"/>')
        _svg_text(out, b["t"], x+w/2, y+h/2, b.get("fs",15), b.get("tc",INK))
    out.append('</svg>')
    with open(os.path.join(OUT, name + ".svg"), "w") as f:
        f.write("\n".join(out))

def _svg_text(out, text, cx, cy, fs, color):
    lines = text.split("\n"); total=len(lines)
    for i,ln in enumerate(lines):
        dy = cy - (total-1)*(fs+3)/2 + i*(fs+3) + fs*0.35
        weight = "700" if (i==0 and total>1) else "400"
        out.append(f'<text x="{cx}" y="{dy}" text-anchor="middle" font-size="{fs}" font-weight="{weight}" fill="{color}">{esc(ln)}</text>')

# ============================================================
# DIAGRAM 1 — Agentic loop + orchestrator/subagents
# ============================================================
def diagram_agent_loop():
    boxes=[
        {"r":[40,70,150,60],"t":"Goal","bg":WHITE},
        {"r":[330,70,200,60],"t":"Gather context\n(retrieve / read)","bg":PANEL},
        {"r":[600,70,200,60],"t":"Take action\n(call tools)","bg":PANEL},
        {"r":[600,200,200,60],"t":"Verify work\n(tests / critic)","bg":PANEL},
        {"r":[330,200,200,60],"t":"Stop condition?\nmax iters / budget / done","bg":"#fbeae3","st":ACCENT},
        {"r":[40,200,150,60],"t":"Done ✓","bg":"#e7f3ec","st":GREEN},
        # orchestrator cluster
        {"r":[300,330,230,55],"t":"Orchestrator (lead agent)\nplans • decomposes • synthesizes","bg":"#e8eefb","st":BLUE},
        {"r":[120,420,170,50],"t":"Subagent A\nown context","bg":WHITE,"st":BLUE},
        {"r":[330,420,170,50],"t":"Subagent B\nown context","bg":WHITE,"st":BLUE},
        {"r":[540,420,170,50],"t":"Subagent C\nown context","bg":WHITE,"st":BLUE},
    ]
    arrows=[
        {"p":[190,100,330,100]},
        {"p":[530,100,600,100],"label":"loop"},
        {"p":[700,130,700,200]},
        {"p":[600,230,530,230],"label":"feedback"},
        {"p":[430,200,430,130],"label":"repeat","color":ACCENT},
        {"p":[330,230,190,230],"label":"yes"},
        {"p":[415,385,300,420],"color":BLUE,"label":"delegate"},
        {"p":[415,385,415,420],"color":BLUE},
        {"p":[415,385,625,420],"color":BLUE,"label":"brief"},
        {"p":[205,470,300,385],"color":GREEN,"dash":True,"label":"summary"},
        {"p":[625,470,530,385],"color":GREEN,"dash":True,"label":"summary"},
    ]
    title="The Agentic Loop  +  Orchestrator / Subagents (hub-and-spoke)"
    render_svg("agent-orchestration-loop",840,500,boxes,arrows,title)
    # excalidraw
    els=[]; i=0
    for b in boxes:
        x,y,w,h=b["r"]; rid=f"r{i}"; els.append(el_rect(rid,x,y,w,h,b.get("bg",PANEL),b.get("st",INK)))
        els.append(el_text(f"t{i}",x+10,y+h/2-14,b["t"],14,b.get("tc",INK),w-20)); i+=1
    for j,a in enumerate(arrows):
        x1,y1,x2,y2=a["p"]; els.append(el_arrow(f"a{j}",x1,y1,x2,y2,a.get("color",MUTED),a.get("dash",False)))
    els.append(el_text("title","250","20",title,20,INK,500))
    write_excalidraw("agent-orchestration-loop",els)

# ============================================================
# DIAGRAM 2 — Tool use loop + MCP architecture
# ============================================================
def diagram_tool_mcp():
    boxes=[
        {"r":[40,80,150,55],"t":"Your App","bg":PANEL},
        {"r":[330,80,170,55],"t":"Claude (model)","bg":"#fbeae3","st":ACCENT},
        {"r":[330,180,170,55],"t":"tool_use\nname + JSON input","bg":WHITE,"st":ACCENT},
        {"r":[40,180,150,55],"t":"App executes tool\n(the security boundary)","bg":WHITE},
        {"r":[40,280,150,55],"t":"tool_result\n(by tool_use_id)","bg":WHITE},
        {"r":[330,280,170,55],"t":"Claude → answer","bg":"#e7f3ec","st":GREEN},
        # MCP cluster
        {"r":[560,90,250,46],"t":"MCP Host  (the AI app)","bg":"#e8eefb","st":BLUE},
        {"r":[560,150,250,40],"t":"MCP Client  (1:1 connector)","bg":WHITE,"st":BLUE},
        {"r":[560,210,250,46],"t":"MCP Server  (your integration)","bg":WHITE,"st":BLUE},
        {"r":[560,275,78,52],"t":"Tools\n(model)","bg":PANEL,"fs":12},
        {"r":[646,275,78,52],"t":"Resources\n(app)","bg":PANEL,"fs":12},
        {"r":[732,275,78,52],"t":"Prompts\n(user)","bg":PANEL,"fs":12},
    ]
    arrows=[
        {"p":[190,107,330,107],"label":"request + tools"},
        {"p":[415,135,415,180]},
        {"p":[330,207,190,207],"label":"execute"},
        {"p":[115,235,115,280]},
        {"p":[190,307,330,307],"label":"result"},
        {"p":[685,136,685,150],"color":BLUE},
        {"p":[685,190,685,210],"color":BLUE},
        {"p":[599,256,599,275],"color":BLUE,"dash":True},
        {"p":[685,256,685,275],"color":BLUE,"dash":True},
        {"p":[771,256,771,275],"color":BLUE,"dash":True},
    ]
    title="Tool-Use Loop (left)  •  Model Context Protocol architecture (right)"
    render_svg("tool-mcp-flow",840,360,boxes,arrows,title)
    els=[]; i=0
    for b in boxes:
        x,y,w,h=b["r"]; els.append(el_rect(f"r{i}",x,y,w,h,b.get("bg",PANEL),b.get("st",INK)))
        els.append(el_text(f"t{i}",x+8,y+h/2-12,b["t"],b.get("fs",13),INK,w-16)); i+=1
    for j,a in enumerate(arrows):
        x1,y1,x2,y2=a["p"]; els.append(el_arrow(f"a{j}",x1,y1,x2,y2,a.get("color",MUTED),a.get("dash",False)))
    els.append(el_text("title","220","18",title,18,INK,520))
    write_excalidraw("tool-mcp-flow",els)

# ============================================================
# DIAGRAM 3 — Context window + prompt caching + reliability
# ============================================================
def diagram_context():
    boxes=[
        {"r":[40,80,360,46],"t":"System prompt  (durable role / rules)","bg":"#e8eefb","st":BLUE},
        {"r":[40,132,360,40],"t":"Tool definitions","bg":"#e8eefb","st":BLUE},
        {"r":[40,178,360,40],"t":"Fixed context / docs / few-shot","bg":"#e8eefb","st":BLUE},
        {"r":[40,236,360,40],"t":"Variable: the user's query / latest turn","bg":"#fbeae3","st":ACCENT},
        {"r":[440,80,360,90],"t":"⟵ CACHE this stable prefix\n(static first, byte-identical).\nReads cheap & fast; writes slightly pricier.","bg":PANEL,"fs":13},
        {"r":[440,236,360,40],"t":"⟵ Keep variable content LAST","bg":PANEL,"fs":13},
        {"r":[40,320,235,70],"t":"Too long?\nCompact / summarize old turns","bg":WHITE},
        {"r":[300,320,235,70],"t":"Offload state to\nexternal memory (files/DB)","bg":WHITE},
        {"r":[560,320,240,70],"t":"Reliability:\nvalidate+retry • backoff •\nself-consistency • evals","bg":"#e7f3ec","st":GREEN,"fs":13},
    ]
    arrows=[
        {"p":[420,103,440,103],"color":BLUE},
        {"p":[420,256,440,256],"color":ACCENT},
        {"p":[157,276,157,320],"label":"context rot? trim"},
        {"p":[275,355,300,355]},
    ]
    title="Context Window: Caching, Curation & Reliability"
    render_svg("context-reliability-model",840,420,boxes,arrows,title)
    # cache bracket visual handled by labels
    els=[]; i=0
    for b in boxes:
        x,y,w,h=b["r"]; els.append(el_rect(f"r{i}",x,y,w,h,b.get("bg",PANEL),b.get("st",INK)))
        els.append(el_text(f"t{i}",x+8,y+h/2-12,b["t"],b.get("fs",13),INK,w-16)); i+=1
    for j,a in enumerate(arrows):
        x1,y1,x2,y2=a["p"]; els.append(el_arrow(f"a{j}",x1,y1,x2,y2,a.get("color",MUTED),a.get("dash",False)))
    els.append(el_text("title","240","20",title,20,INK,420))
    write_excalidraw("context-reliability-model",els)

# ============================================================
# DIAGRAM 4 — 5-domain syllabus map (hub & spoke)
# ============================================================
def diagram_syllabus():
    title="CCA-F Syllabus Map — 5 Domains (weights are COMMUNITY-reported)"
    ell=[{"r":[360,200,120,120],"t":"CCA-F\n5 domains","bg":ACCENT,"st":ACCENT,"tc":WHITE,"fs":16}]
    boxes=[
        {"r":[40,60,250,66],"t":"D1 · Agentic Architecture  ~27%\nagents vs workflows, orchestration","bg":PANEL,"fs":13},
        {"r":[560,60,250,66],"t":"D2 · Prompt Engineering  ~20%\nclarity, examples, JSON output","bg":PANEL,"fs":13},
        {"r":[20,400,250,66],"t":"D3 · Tools & MCP  ~18%\ntool schemas, MCP primitives","bg":PANEL,"fs":13},
        {"r":[580,400,250,66],"t":"D4 · Context & Reliability  ~15%\ncaching, context, robustness","bg":PANEL,"fs":13},
        {"r":[300,470,250,60],"t":"D5 · Claude Code  ~20%\nsettings, hooks, subagents, CI","bg":PANEL,"fs":13},
    ]
    arrows=[
        {"p":[300,300,165,126]},{"p":[540,300,685,126]},
        {"p":[330,300,145,400]},{"p":[510,300,705,400]},
        {"p":[420,320,420,470]},
    ]
    render_svg("syllabus-map",840,560,boxes,arrows,title,ellipses=ell)
    els=[]; i=0
    els.append(el_ellipse("hub",360,200,120,120))
    els.append(el_text("hubt",385,245,"CCA-F\n5 domains",16,WHITE,90))
    for b in boxes:
        x,y,w,h=b["r"]; els.append(el_rect(f"r{i}",x,y,w,h,b.get("bg",PANEL),INK))
        els.append(el_text(f"t{i}",x+8,y+h/2-14,b["t"],13,INK,w-16)); i+=1
    for j,a in enumerate(arrows):
        x1,y1,x2,y2=a["p"]; els.append(el_arrow(f"a{j}",x1,y1,x2,y2,LINE))
    els.append(el_text("title","180","20",title,18,INK,520))
    write_excalidraw("syllabus-map",els)

if __name__ == "__main__":
    diagram_agent_loop(); diagram_tool_mcp(); diagram_context(); diagram_syllabus()
    print("Wrote .excalidraw + .svg for 4 diagrams")
    # PNG export
    try:
        import cairosvg
        for n in ["agent-orchestration-loop","tool-mcp-flow","context-reliability-model","syllabus-map"]:
            cairosvg.svg2png(url=os.path.join(OUT,n+".svg"), write_to=os.path.join(OUT,n+".png"), scale=2)
        print("Wrote .png exports")
    except Exception as e:
        print("PNG export skipped:", e)
