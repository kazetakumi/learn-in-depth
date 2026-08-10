#!/usr/bin/env python3
"""Regenerate index.html from syllabus.json, baking statuses into the HTML."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, "syllabus.json")))

PARTS = [
    ("Ground", "00-nothing-is-running", "03-the-contract"),
    ("Indirection", "04-pointers", "09-the-heap"),
    ("Structure", "10-structs", "13-objects"),
    ("Programs", "14-the-linker", "17-failure-is-data"),
    ("The system", "18-security", "21-threads"),
    ("Mastery", "22-performance", "25-capstone"),
]

MARK = {"done": "✓", "current": "▶", "planned": ""}


def part_of(cid):
    for name, lo, hi in PARTS:
        if lo <= cid <= hi:
            return name
    return "Other"


rows, seen = [], set()
for name, _, _ in PARTS:
    group = [c for c in S["cruxes"] if part_of(c["id"]) == name]
    if not group:
        continue
    rows.append(f'<h2 class="part">{html.escape(name)}</h2>')
    for c in group:
        seen.add(c["id"])
        st = c["status"]
        n = c["id"].split("-")[0]
        title = html.escape(c["title"])
        hook = html.escape(c["hook"])
        exists = os.path.exists(os.path.join(HERE, c["lesson"]))
        inner = (
            f'<a href="{c["lesson"]}">{title}</a>' if exists else f"<span>{title}</span>"
        )
        rows.append(
            f'<article class="rung {st}">'
            f'<div class="num">{n}<span class="mark">{MARK[st]}</span></div>'
            f'<div class="body"><h3>{inner}</h3><p>{hook}</p></div>'
            f"</article>"
        )

done = sum(1 for c in S["cruxes"] if c["status"] == "done")
cur = next((c for c in S["cruxes"] if c["status"] == "current"), None)
total = len(S["cruxes"])
where = (
    f'Rung {cur["id"].split("-")[0]} of {total - 1} — {html.escape(cur["title"])}'
    if cur
    else "Complete"
)

doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C, from zero to architect</title>
<style>
  :root {{ --paper:#fbfaf6; --ink:#2b2620; --accent:#355070; --rule:#e2ddd0; --mute:#7d746a; --code:#f3f0e8; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--paper); color:var(--ink);
    font-family:'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif;
    font-size:19px; line-height:1.65; }}
  .wrap {{ max-width:640px; margin:0 auto; padding:5rem 1.5rem 8rem; }}
  h1 {{ font-size:2.1rem; line-height:1.2; font-weight:normal; margin:0 0 .6rem; letter-spacing:-.01em; }}
  .sub {{ color:var(--mute); font-size:1rem; font-style:italic; margin:0 0 2.5rem; }}
  .status {{ border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);
    padding:1rem 0; margin:0 0 3.5rem; font-size:.95rem; color:var(--mute); }}
  .status b {{ color:var(--accent); font-weight:normal; font-style:normal; }}
  .part {{ font-size:.78rem; text-transform:uppercase; letter-spacing:.16em; font-weight:normal;
    color:var(--accent); margin:3.5rem 0 1.5rem; padding-bottom:.4rem; border-bottom:1px solid var(--rule); }}
  .part:first-of-type {{ margin-top:0; }}
  .rung {{ display:flex; gap:1.1rem; margin:0 0 1.9rem; align-items:baseline; }}
  .num {{ flex:0 0 2.6rem; text-align:right; color:var(--mute); font-size:.9rem;
    font-variant-numeric:tabular-nums; white-space:nowrap; }}
  .mark {{ display:inline-block; width:1rem; text-align:center; }}
  .rung h3 {{ margin:0 0 .25rem; font-size:1.06rem; font-weight:normal; line-height:1.35; }}
  .rung h3 a {{ color:var(--accent); text-decoration:none; border-bottom:1px solid #c3d0dd; }}
  .rung h3 a:hover {{ border-bottom-color:var(--accent); }}
  .rung p {{ margin:0; font-size:.94rem; color:var(--mute); line-height:1.55; }}
  .rung.planned {{ opacity:.5; }}
  .rung.current .num, .rung.current h3 {{ color:var(--accent); }}
  .rung.current h3 {{ font-weight:600; }}
  .rung.done .num {{ color:var(--accent); }}
  footer {{ margin-top:5rem; padding-top:1.5rem; border-top:1px solid var(--rule);
    font-size:.86rem; color:var(--mute); }}
  footer code {{ background:var(--code); padding:.1rem .3rem; border-radius:2px; font-size:.85em; }}
</style></head>
<body><div class="wrap">
<h1>C, from zero to architect</h1>
<p class="sub">{html.escape(S['goal'])}</p>
<div class="status">You are here: <b>{where}</b> &nbsp;·&nbsp; {done} of {total} done</div>
{chr(10).join(rows)}
<footer>Grounded in two video courses (28 hours), five books, and four university courses —
full inventory in <code>SOURCES.md</code>. Progress lives in <code>syllabus.json</code>.</footer>
</div></body></html>
"""

open(os.path.join(HERE, "index.html"), "w").write(doc)
missing = [c["id"] for c in S["cruxes"] if c["id"] not in seen]
print(f"wrote index.html — {total} rungs, {done} done" + (f"; UNGROUPED: {missing}" if missing else ""))
