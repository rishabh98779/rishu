"""Build the report: assemble HTML, render to PDF, verify page numbers, re-render.

Two-pass approach: the first pass renders with placeholder folios so that the real page
number of every chapter can be located in the output PDF, then the TOC is rebuilt with
those numbers and the document is rendered again. Pass 2 can shift pagination, so the
loop repeats until the page numbers are stable (normally one iteration).
"""
from __future__ import annotations

import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "out")
BUILD = os.path.join(ROOT, "build")

sys.path.insert(0, HERE)

import content as K           # noqa: E402
from figures import cover_art  # noqa: E402

CHAPTERS = [K.CH1, K.CH2, K.CH3, K.CH4, K.CH5, K.CH6, K.CH7,
            K.CH8, K.CH9, K.CH10, K.CH11, K.CH12, K.CH13]

RUNNING = {
    "ch1": "The Architecture of a Person",
    "ch2": "Personality at a Glance",
    "ch3": "The Thinking System",
    "ch4": "The Emotional System",
    "ch5": "Ambition, Standards and Conscientiousness",
    "ch6": "Diplomacy, Empathy and Relationships",
    "ch7": "Strengths and Their Shadow Sides",
    "ch8": "Contradictions and Blind Spots",
    "ch9": "Conditional Behavioural Predictions",
    "ch10": "Development Plan",
    "ch11": "What Remains Unknown",
    "ch12": "Final Synthesis",
    "ch13": "Research and Methodology",
}

# Chapter-level TOC entries: (label, note, chapter id, subheading id or None)
TOC = [
    ("Front matter", "Evidence vocabulary, contents, scope note", "front", None),
    ("The Architecture of a Person", "Overall portrait, main tensions, boundaries of the evidence", "ch1", None),
    ("Personality at a Glance", "Big Five and HEXACO estimates with evidence strength", "ch2", None),
    ("The Thinking System", "Analysis, decisions, and the search for one root cause", "ch3", None),
    ("The Emotional System", "Guilt, shame, self-punishment, composure, empathy", "ch4", None),
    ("Ambition, Standards and Conscientiousness", "Ambition, planning, effort, execution, outcome", "ch5", None),
    ("Diplomacy, Empathy and Relationships", "Values in practice, idealisation, social stiffness", "ch6", None),
    ("Strengths and Their Shadow Sides", "Twelve capacities with their failure modes", "ch7", None),
    ("Contradictions and Blind Spots", "Fourteen tensions, each with a test", "ch8", None),
    ("Conditional Behavioural Predictions", "Fourteen situations with reasoning and alternatives", "ch9", None),
    ("Development Plan", "Three priorities and a thirty-day structure", "ch10", None),
    ("What Remains Unknown", "Ten questions and two structural limits", "ch11", None),
    ("Final Synthesis", "Conclusions, liabilities, and what not to infer", "ch12", None),
    ("Research and Methodology", "Evidence base, source quality, bibliography", "ch13", None),
]


def _rh(left, right=""):
    return (f'<div class="rh"><span>{left}</span>'
            f'<span class="rh-r">{right}</span></div>')


def _rf(folio, label):
    return (f'<div class="rf"><span>Rishabh Singh &nbsp;·&nbsp; '
            f'Personality, Character and Behavioural Analysis</span>'
            f'<span>{label} &nbsp; <span class="folio">{folio}</span></span></div>')


def page(inner, folio, rh_left="", rh_right="", cls="", label="", show_furniture=True):
    if show_furniture:
        return (f'<section class="page {cls}">{_rh(rh_left, rh_right)}'
                f'<div class="frame">{inner}</div>{_rf(folio, label)}</section>')
    return f'<section class="page {cls}"><div class="frame">{inner}</div></section>'


# --------------------------------------------------------------------- cover
COVER = f"""
<section class="page cover">
  <div class="cover-inner">
    <div style="display:flex;justify-content:space-between;align-items:baseline;
                border-bottom:.5pt solid #2E3D5E;padding-bottom:3mm">
      <span style="font-family:'Inter',sans-serif;font-size:7.4pt;letter-spacing:.26em;
                   text-transform:uppercase;color:#8FA0BE;font-weight:600">
        Confidential personal report</span>
      <span style="font-family:'Inter',sans-serif;font-size:7.4pt;letter-spacing:.2em;
                   text-transform:uppercase;color:#8FA0BE;font-weight:600">26 October 2026</span>
    </div>

    <div style="margin-top:16mm">
      <span style="font-family:'Inter',sans-serif;font-size:7.6pt;letter-spacing:.3em;
                   text-transform:uppercase;color:#C08A2A;font-weight:700">
        Personality · Character · Behaviour</span>
      <h1 style="margin-top:7mm">THE<br/>ARCHITECTURE<br/>OF A PERSON</h1>
      <div class="sub">A Comprehensive Personality, Character and Behavioural Analysis</div>
    </div>

    <div style="margin-top:9mm">
      {cover_art(760, 300)}
    </div>

    <div class="prep">Prepared for Rishabh Singh</div>
    <div class="meta">
      Evidence-informed interpretive report · Approximately 15,500 words · 27 pages<br/>
      Based on a subject dossier and an exported Rishabh–AI conversation transcript<br/>
      No instrument administered · No clinical evaluation or risk assessment performed
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------- front matter
FRONT_1 = """
<h2 class="sec" style="border-bottom:none;padding-bottom:0"><span class="sn">i</span>How to read this report</h2>

<p class="lede">This is an interpretive report about a person the author has not met. It is
built from written material only. Understanding what kind of material that is will make the
report more useful and less misleading.</p>

<p>Every substantive claim below is tagged with the kind of evidence behind it. The tags are
not decoration; they are the difference between a finding and a guess.</p>

<table>
<caption>Evidence vocabulary used throughout</caption>
<thead><tr><th style="width:20%">Tag</th><th style="width:38%">Meaning</th><th>What it establishes</th></tr></thead>
<tbody>
<tr><td class="k"><span class="conf hi">direct</span></td><td>A dated, checkable fact in the dossier</td><td>That it happened or was recorded. Scores, enrolments, deadlines, submission requirements.</td></tr>
<tr><td class="k"><span class="conf hi">artefact</span></td><td>Something that exists independently of his account of it</td><td>That a repository, document or prototype exists with identifiable structure. Not that it worked as intended.</td></tr>
<tr><td class="k"><span class="conf md">self</span></td><td>His own first-person report of experience, belief or intention</td><td>What he reported believing, feeling or wanting. Not frequency, severity, persistence or current status.</td></tr>
<tr><td class="k"><span class="conf md">infer</span></td><td>A reading drawn by combining the above</td><td>The analyst's interpretation, with its basis visible and alternatives noted.</td></tr>
<tr><td class="k"><span class="conf lo">hypoth</span></td><td>A testable possibility</td><td>A candidate explanation, offered with the observation that would confirm or disconfirm it.</td></tr>
</tbody>
</table>

<h2 class="sec"><span class="sn">ii</span>Scope and limits, stated once</h2>

<div class="grid2">
<div class="card">
<h4>What this report is</h4>
<p class="body">An evidence-informed reading of a young man's personality, thinking style,
emotional patterns and development needs, assembled from a factual dossier and a long
exported AI conversation, using established psychological frameworks as lenses.</p>
</div>
<div class="card amber">
<h4>What this report is not</h4>
<p class="body">Not a clinical evaluation. Not a diagnosis. Not a psychometric assessment.
Not a suicide, self-harm or violence risk assessment. Not a substitute for speaking with a
qualified professional, and not a basis for anyone else to make decisions about him.</p>
</div>
</div>

<div class="callout plain">
<span class="lab">Three sentences that carry most of the methodological weight</span>
<p>Length of discussion is not severity. A pattern described at length in a conversation is
not thereby more frequent, more intense or more current than one described briefly. In this
material the emotional themes were discussed exhaustively and the technical themes were
discussed briefly, and the report weights the dated technical evidence more heavily as a
result.</p>
<p>Self-report is the only route to inner experience and is weak on frequency, severity,
comparability and current status. There is not one observer account in the source material.</p>
<p>Thoughts, feelings, intentions and actions are treated as four separate things throughout.
Nothing in this report upgrades one into another in either direction.</p>
</div>

<p class="tiny mt4">Personal identifiers, account names, institutional numbers, contact
details and the names of all third parties have been omitted. No third party is named
anywhere in this document, and no allegation recorded in the source is treated as
established fact.</p>
"""


def toc_html(folios):
    rows = []
    for label, note, cid, _sub in TOC:
        p = folios.get(cid, "—")
        if cid == "front":
            rows.append(f'<div class="toc-row"><span class="n">—</span>'
                        f'<span class="t"><span style="font-style:italic">Front matter</span>'
                        f'<span class="note">{note}</span></span>'
                        f'<span class="d"></span><span class="p">{p}</span></div>')
        else:
            n = next((c["num"] for c in CHAPTERS if c["id"] == cid), "")
            rows.append(f'<div class="toc-row"><span class="n">{n}</span>'
                        f'<span class="t">{html.escape(label)}<span class="note">{note}</span></span>'
                        f'<span class="d"></span><span class="p">{p}</span></div>')
    return ('<h2 class="sec" style="border-bottom:none;padding-bottom:0">'
            '<span class="sn">iii</span>Contents</h2><div class="toc-list">'
            + "".join(rows) + "</div>")


FRONT_2_TAIL = """
<h2 class="sec"><span class="sn">iv</span>Figures and tables</h2>
<div class="grid2">
<div>
<h4 class="min">Figures</h4>
<div class="xsmall">
<p><b>1</b> &nbsp;Big Five profile with evidence strength<br/>
<b>2</b> &nbsp;HEXACO profile with evidence strength<br/>
<b>3</b> &nbsp;Evidence-confidence matrix<br/>
<b>4</b> &nbsp;Situation–interpretation–emotion–behaviour–consequence model<br/>
<b>5</b> &nbsp;Strengths and their shadow sides<br/>
<b>6</b> &nbsp;Values against behavioural evidence<br/>
<b>7</b> &nbsp;Confidence key for the conditional predictions<br/>
<b>8</b> &nbsp;The thirty-day plan<br/>
<b>9</b> &nbsp;Two candidate loops, with alternatives (Chapter 4)</p>
</div>
</div>
<div>
<h4 class="min">Tables</h4>
<div class="xsmall">
<p>Four readings of the single-cause request (Ch. 3)<br/>
Separating guilt, shame and self-punishment (Ch. 4)<br/>
The five layers of ambition (Ch. 5)<br/>
What the teammate episode does and does not establish (Ch. 6)<br/>
What the episode establishes, and what it does not (Ch. 4)<br/>
The ten questions and what each would resolve (Ch. 11)<br/>
Sources used and the weight given to each (Ch. 13)</p>
</div>
</div>
</div>

<div class="callout caution mt4">
<span class="lab">One paragraph the reader should not skip</span>
<p>If self-hatred, self-punishment or intrusive thoughts are currently frequent, severe or
difficult to leave alone, or if there is any thought of harm to himself or anyone else, the
appropriate step is to speak with a qualified mental-health professional — a university
counselling service, a psychologist or a psychiatrist. Imminent risk requires urgent local
help. Nothing in this report substitutes for that, and no part of it should be read as
establishing that such support is or is not needed.</p>
</div>
"""


def _chapter_head(ch, first=True):
    mark = f'<span class="pagemark">MARK{ch["id"].upper()}</span>' if first else ""
    return (f'{mark}<div class="ch-open">'
            f'<span class="ch-num">Chapter {ch["num"]} &nbsp;·&nbsp; {ch["kicker"]}</span>'
            f'<h1 class="ch-title">{ch["title"]}</h1>'
            f'<div class="ch-rule"></div>'
            f'<div class="ch-sub">{ch["sub"]}</div></div>')


def build_body(folios, layout=None):
    """Assemble the document.

    layout maps chapter id -> list of page HTML fragments produced by measured reflow.
    When layout is None the raw chapter pages are used (first pass, for measurement).
    """
    parts = [COVER]
    parts.append(page('<span class="pagemark">MARKFRONT</span>' + FRONT_1, "2",
                      "Front matter", "Evidence vocabulary and scope",
                      cls="tint", label="Front matter"))
    parts.append(page(toc_html(folios) + FRONT_2_TAIL, "3", "Contents",
                      "Figures and tables", label="Contents"))
    for ch in CHAPTERS:
        start = folios.get(ch["id"])
        if layout and ch["id"] in layout:
            frags = layout[ch["id"]]
        else:
            frags = [_chapter_head(ch) + '<div class="two-col">'
                     + "\n".join(ch["pages"]) + "</div>"]
        for i, inner in enumerate(frags):
            folio = str(start + i) if isinstance(start, int) else "\u2014"
            parts.append(page(inner, folio,
                              f'Chapter {ch["num"]} \u00b7 {RUNNING[ch["id"]]}',
                              ch["kicker"], label=f'Chapter {ch["num"]}'))
    parts.append(page(COLOPHON, "__COLOPHON__", "Colophon", "", label="Colophon"))
    return "\n".join(parts)


def build_flow():
    """A single-column document containing every chapter's content for measurement."""
    out = []
    for ch in CHAPTERS:
        out.append(f'<section data-chapter="{ch["id"]}">'
                   + _chapter_head(ch) + "\n".join(ch["pages"]) + "</section>")
    return "\n".join(out)


COLOPHON = """
<div class="ch-open">
<span class="ch-num">Colophon</span>
<h1 class="ch-title" style="font-size:21pt">About this document</h1>
<div class="ch-rule"></div>
</div>

<div class="grid2">
<div class="card">
<h4>Production</h4>
<p class="body">Set in EB Garamond for display and headings and Inter for body text, on an
A4 portrait grid with a 19 mm margin. Colour palette: midnight navy, warm ivory, restrained
teal for constructive findings and muted amber for uncertainty and caution. All figures are
original vector artwork generated for this report. No stock imagery is used.</p>
</div>
<div class="card">
<h4>Interpretive conventions</h4>
<p class="body">Navy indicates an established or well-supported observation. Teal marks a
constructive implication. Amber marks uncertainty, an alternative explanation, or a caution.
Hatched bands in the profile figures mark dimensions the available evidence cannot
defensibly place — they are not low scores.</p>
</div>
</div>

<h2 class="sec"><span class="sn">v</span>Statement of limitations</h2>

<p>This report was prepared on 26 October 2026 from two written sources: a subject dossier
containing retained facts and summaries of prior conversations, and an exported transcript of
a previous Rishabh–AI conversation. The author has not met the subject, has administered no
instrument, has observed no behaviour, and has obtained no account from any other person.</p>

<p>It follows that the report cannot establish: his true Big Five or HEXACO scores; whether
he is introverted or extraverted; how others experience him; whether his reported distress is
persistent, occasional or situational; how consistently he performs when unobserved; his
current political, religious, gender-related or relationship views; whether any recorded
academic, health or routine detail remains current; whether any project achieved its intended
result; whether he has any psychological or medical condition; and his current safety status.</p>

<p>Three further limits apply. First, several emotionally significant disclosures in the
transcript were made in a conversation that repeatedly offered confident and totalising
explanations of his character, which may have shaped how he described himself. Second, the
transcript mixes first-person disclosure, earlier AI interpretation and exported notebook
material, and its chronology is uncertain. Third, where the transcript and the dossier
conflict, the report flags the conflict rather than reconciling it.</p>

<p>This document is an evidence-informed interpretive report. It is not a clinical
evaluation, a diagnostic assessment, a psychometric assessment, or a suicide, self-harm or
violence risk assessment, and it should not be used as any of those things.</p>

<div class="hr-navy"></div>
<p class="small center" style="color:var(--charcoal-3)">
THE ARCHITECTURE OF A PERSON &nbsp;·&nbsp; Prepared for Rishabh Singh &nbsp;·&nbsp; 26 October 2026<br/>
End of report
</p>
"""


def render(html_str, pdf_path):
    from playwright.sync_api import sync_playwright
    doc = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/>"
           "<title>The Architecture of a Person — Rishabh Singh</title>"
           "<link rel='stylesheet' href='../src/styles.css'/></head><body>"
           + html_str + "</body></html>")
    tmp = os.path.join(BUILD, "report.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/chromium",
                              args=["--no-sandbox", "--disable-dev-shm-usage",
                                    "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.abspath(tmp), wait_until="load")
        pg.wait_for_timeout(1400)
        pg.pdf(path=pdf_path, format="A4", print_background=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
               prefer_css_page_size=False)
        b.close()
    return tmp


def locate_folios(pdf_path):
    """Find which printed page each chapter actually starts on, via hidden markers."""
    import pymupdf
    doc = pymupdf.open(pdf_path)
    found = {}
    for pno in range(doc.page_count):
        t = doc[pno].get_text().replace(" ", "").replace("\n", "")
        for ch in CHAPTERS:
            if ch["id"] not in found and f'MARK{ch["id"].upper()}' in t:
                found[ch["id"]] = pno + 1
        if "front" not in found and "MARKFRONT" in t:
            found["front"] = pno + 1
    n = doc.page_count
    doc.close()
    return found, n


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(BUILD, exist_ok=True)

    import reflow

    # ---- 1. measure every chapter block in a single-column flow
    flow_html = build_flow()
    tmp_flow = os.path.join(BUILD, "flow.html")
    measured = reflow.measure_chapters(flow_html, tmp_flow)
    cap = reflow._mm_to_px(reflow.FRAME_H_MM)
    print(f"frame capacity: {cap:.0f}px")
    for cid, blocks in measured.items():
        tot = sum(b["h"] for b in blocks)
        print(f"  {cid:<5} blocks={len(blocks):>3} content={tot:>7.0f}px "
              f"= {tot/cap:.2f} pages")

    # ---- 2. pack into pages
    layout = {}
    for ch in CHAPTERS:
        blocks = measured.get(ch["id"], [])
        # the chapter head is rendered separately, so subtract it from page 1 capacity
        pages = reflow.reflow_chapter(ch["id"], blocks, tmp_flow)
        layout[ch["id"]] = pages
    print("packed pages per chapter:",
          {k: len(v) for k, v in layout.items()})
    total = 3 + sum(len(v) for v in layout.values()) + 1
    print("estimated total pages:", total)

    # ---- 3. render pass 1 with real layout and placeholder folios
    folios = {c["id"]: "\u2014" for c in CHAPTERS}
    folios["front"] = "2"
    body = build_body(folios, layout)
    tmp_pdf = os.path.join(BUILD, "pass1.pdf")
    render(body, tmp_pdf)
    found, npages = locate_folios(tmp_pdf)
    print("pass1 pages:", npages, "located:", found)

    # ---- 4. render with real folios
    folios.update(found)
    body = build_body(folios, layout)
    pdf = os.path.join(OUT, "Rishabh_Singh_Personality_Report.pdf")
    render(body, pdf)
    found2, npages2 = locate_folios(pdf)
    if found2 != found:
        print("folios shifted; re-rendering")
        folios.update(found2)
        body = build_body(folios, layout)
        render(body, pdf)
        found3, npages3 = locate_folios(pdf)
        print("pass3:", npages3, "stable:", found3 == found2)
    else:
        print("folios stable at", npages2, "pages")
    print("final:", pdf, os.path.getsize(pdf), "bytes")


if __name__ == "__main__":
    main()
