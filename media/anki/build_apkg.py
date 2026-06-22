#!/usr/bin/env python3
"""
Build an Anki deck (.apkg) from ../../06-flashcards/flashcards.csv.
Requires: pip install genanki
Run:      python3 build_apkg.py
Output:   cca-foundations.apkg   (double-click to import into Anki)

Cards are tagged by domain so you can study subsets in Anki.
"""
import csv, os, genanki

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "..", "06-flashcards", "flashcards.csv")

MODEL = genanki.Model(
    1607390210, "CCA-F Basic",
    fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Domain"}],
    templates=[{
        "name": "Card 1",
        "qfmt": '<div class="dom">{{Domain}}</div><div class="q">{{Question}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Answer}}</div>',
    }],
    css="""
.card{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:19px;color:#1f2430;
      background:#faf8f4;text-align:center;padding:24px}
.dom{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#d97757;margin-bottom:10px}
.q{font-weight:600}
.a{margin-top:8px;color:#2a3140}
hr#answer{border:none;border-top:1px solid #d8d2c8;margin:16px 0}
""")

DOMAIN_NAMES = {"General":"General / Exam Facts","D1":"Agentic Architecture","D2":"Prompt Engineering",
                "D3":"Tools & MCP","D4":"Context & Reliability","D5":"Claude Code"}

def main():
    deck = genanki.Deck(2059400110, "Claude Certified Architect – Foundations (CCA-F)")
    n = 0
    with open(CSV, newline="") as f:
        for row in csv.DictReader(f):
            dom = row["domain"].strip()
            tag = DOMAIN_NAMES.get(dom, dom).replace(" ", "_").replace("&", "and").replace("/", "_")
            note = genanki.Note(model=MODEL,
                fields=[row["question"], row["answer"], DOMAIN_NAMES.get(dom, dom)],
                tags=[f"CCAF::{tag}"])
            deck.add_note(note); n += 1
    genanki.Package(deck).write_to_file(os.path.join(HERE, "cca-foundations.apkg"))
    print(f"Wrote cca-foundations.apkg with {n} cards")

if __name__ == "__main__":
    main()
