"""Build the report as a continuously flowing document with real pagination.

Fixed-height page containers clip content rather than reflowing it, which makes
overflow inevitable. This builder instead renders one continuous document, lets
Chromium paginate it properly, then stamps page furniture (spine, running head,
folio) into the empty margins with PyMuPDF. Content and furniture can therefore
never overlap, because they occupy different regions of the page.

Two passes are used so the table of contents can carry real page numbers: the
first pass renders with placeholders, chapter opener pages are located by hidden
marker text, and the second pass writes the resolved numbers in.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "out")
BUILD = os.path.join(ROOT, "build")

sys.path.insert(0, HERE)

import content as K           # noqa: E402
from figures import cover_art  # noqa: E402

CHAPTERS = [K.CH1, K.CH2, K.CH3, K.CH4, K.CH5, K.CH6, K.CH7, K.CH8,
            K.CH9, K.CH10, K.CH11, K.CH12, K.CH13, K.CH14]

RUNNING = {c["id"]: c["title"] for c in CHAPTERS}

TOC = [
    ("Front matter", "Evidence vocabulary, scope note and limitations", "front"),
    ("The Architecture of a Person", "Overall portrait, main tensions, boundaries of the evidence", "ch1"),
    ("Personality at a Glance", "Big Five, HEXACO and VIA readings with evidence strength", "ch2"),
    ("The Thinking System", "Analysis, decisions, and the search for one root cause", "ch3"),
    ("The Emotional System", "Guilt, shame, self-punishment, composure, empathy", "ch4"),
    ("Safety and Risk Formulation", "Historical signals, protective factors and current unknowns", "ch5"),
    ("Ambition, Standards and Conscientiousness", "Ambition, planning, effort, execution, outcome", "ch6"),
    ("Diplomacy, Empathy and Relationships", "Values in practice, idealisation, social stiffness", "ch7"),
    ("Strengths and Their Shadow Sides", "Twelve capacities with their failure modes", "ch8"),
    ("Contradictions and Blind Spots", "Fourteen tensions, each with a test", "ch9"),
    ("Conditional Behavioural Predictions", "Fourteen situations with reasoning and alternatives", "ch10"),
    ("Development Plan", "Three priorities and a thirty-day structure", "ch11"),
    ("What Remains Unknown", "Ten questions and two structural limits", "ch12"),
    ("Final Synthesis", "Conclusions, liabilities, and what not to infer", "ch13"),
    ("Research and Methodology", "Evidence base, source quality, bibliography", "ch14"),
]

# page geometry, millimetres
PW, PH = 210.0, 297.0
M_TOP, M_SIDE, M_BOTTOM = 12.6, 14.2, 10.8
SPINE_W = 3.2


def mm(v):
    return v * 72.0 / 25.4


# --------------------------------------------------------------------- cover
def cover_html(words="15,300", pages="23"):
    return f"""
<section class="cover-page">
  <div class="cover-inner">
    <div class="cover-rule">
      <span>Confidential personal report</span><span>26 October 2026</span>
    </div>
    <div class="cover-block">
      <span class="cover-kicker">Personality · Character · Behaviour</span>
      <h1>THE<br/>ARCHITECTURE<br/>OF A PERSON</h1>
      <div class="cover-sub">A Comprehensive Personality, Character and Behavioural Analysis</div>
    </div>
    <div class="cover-art">{cover_art(760, 300)}</div>
    <div class="cover-prep">Prepared for Rishabh Singh</div>
    <div class="cover-meta">
      Evidence-informed interpretive report · Approximately {words} words · {pages} pages<br/>
      Based on a subject dossier and an exported Rishabh–AI conversation transcript<br/>
      No instrument administered · Includes a bounded, retrospective Safety and Risk Formulation (Ch. 5)
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------- front matter
FRONT = """
<span class="pagemark">MARKFRONT</span>
<h2 class="sec first"><span class="sn">i</span>How to read this report</h2>

<p class="lede">This is an interpretive report about a person the author has not met. It is built
from written material only. Understanding what kind of material that is will make the report more
useful and less misleading.</p>

<p>Every substantive claim below is tagged with the kind of evidence behind it. The tags are not
decoration; they are the difference between a finding and a guess.</p>

<table>
<caption>Evidence vocabulary used throughout</caption>
<thead><tr><th style="width:18%">Tag</th><th style="width:36%">Meaning</th><th>What it establishes</th></tr></thead>
<tbody>
<tr><td class="k"><span class="conf hi">direct</span></td><td>A dated, checkable fact in the dossier</td><td>That it happened or was recorded — scores, enrolments, deadlines, submission requirements.</td></tr>
<tr><td class="k"><span class="conf hi">artefact</span></td><td>Something that exists independently of his account of it</td><td>That a repository, document or prototype exists with identifiable structure. Not that it worked as intended.</td></tr>
<tr><td class="k"><span class="conf md">self</span></td><td>His own first-person report of experience, belief or intention</td><td>What he reported believing, feeling or wanting. Not frequency, severity, persistence or current status.</td></tr>
<tr><td class="k"><span class="conf md">infer</span></td><td>A reading drawn by combining the above</td><td>The analyst's interpretation, with its basis visible and alternatives noted.</td></tr>
<tr><td class="k"><span class="conf lo">hypoth</span></td><td>A testable possibility</td><td>A candidate explanation, offered with the observation that would confirm or disconfirm it.</td></tr>
</tbody>
</table>

<div class="grid2">
<div class="card">
<h4>What this report is</h4>
<p class="body">An evidence-informed reading of a young man's personality, thinking style,
emotional patterns and development needs, assembled from a factual dossier and a long exported AI
conversation, using established psychological frameworks as lenses.</p>
</div>
<div class="card amber">
<h4>What this report is not</h4>
<p class="body">Not a clinical evaluation. Not a diagnosis. Not a psychometric assessment. It
contains a retrospective, evidence-bounded Safety and Risk Formulation (Chapter 5), but that chapter
is <b>not</b> a formal clinical risk assessment and cannot establish present acute risk. This report
is not a substitute for speaking with a qualified professional, and not a basis for anyone else to
make decisions about him.</p>
</div>
</div>

<div class="callout plain">
<span class="lab">Three sentences that carry most of the methodological weight</span>
<p><b>Length of discussion is not severity.</b> A pattern described at length in a conversation is
not thereby more frequent, more intense or more current than one described briefly. In this material
the emotional themes were discussed exhaustively and the technical themes briefly, and the report
weights the dated technical evidence more heavily as a result.</p>
<p><b>Self-report is the only route to inner experience and is weak on frequency, severity,
comparability and current status.</b> There is not one observer account in the source material.</p>
<p><b>Thoughts, feelings, intentions and actions are treated as four separate things throughout.</b>
Nothing in this report upgrades one into another in either direction.</p>
</div>

<div class="callout caution">
<span class="lab">One paragraph the reader should not skip</span>
<p>The source material contains two explicit first-person disclosures that are risk-relevant: a
self-sacrificial statement tied to an idealised figure, and a separate episode of escalating anger
with violent imagery. Both are examined in Chapter 5 and neither is softened there. If either kind of
thought is currently frequent, severe, escalating or difficult to leave alone, or if there is any
thought of harm to himself or anyone else, the appropriate step is to speak with a qualified
mental-health professional — a university counselling service, a psychologist or a psychiatrist. If
there is current intent, a plan, access to means, an identifiable target, or an inability to stay
safe, that requires immediate local help. Nothing in this report substitutes for that, and no part of
it should be read as establishing that such support is or is not needed.</p>
</div>

<p class="tiny">Personal identifiers, account names, institutional numbers, contact details and the
names of all third parties have been omitted. No third party is named anywhere in this document, and
no allegation recorded in the source is treated as established fact.</p>
"""


def toc_html(folios):
    rows = []
    for label, note, cid in TOC:
        p = folios.get(cid, "—")
        if cid == "front":
            rows.append(f'<div class="toc-row"><span class="n">—</span>'
                        f'<span class="t"><span class="toc-ital">Front matter</span>'
                        f'<span class="note">{note}</span></span>'
                        f'<span class="d"></span><span class="p">{p}</span></div>')
        else:
            n = next((c["num"] for c in CHAPTERS if c["id"] == cid), "")
            rows.append(f'<div class="toc-row"><span class="n">{n}</span>'
                        f'<span class="t">{label}<span class="note">{note}</span></span>'
                        f'<span class="d"></span><span class="p">{p}</span></div>')
    return f"""
<span class="pagemark">MARKTOC</span>
<h2 class="sec"><span class="sn">ii</span>Contents</h2>
<div class="toc-list">{"".join(rows)}</div>

<h2 class="sec"><span class="sn">iii</span>Figures and tables</h2>
<div class="grid2">
<div>
<h4 class="min">Figures</h4>
<div class="xsmall">
<p><b>1</b>&nbsp; Big Five profile with evidence strength<br/>
<b>2</b>&nbsp; HEXACO profile with evidence strength<br/>
<b>3</b>&nbsp; Evidence-confidence matrix<br/>
<b>4</b>&nbsp; Situation–interpretation–emotion–behaviour–consequence model<br/>
<b>5</b>&nbsp; Risk-relevant domains: historical evidence vs. current unknowns<br/>
<b>6</b>&nbsp; Strengths and their shadow sides<br/>
<b>7</b>&nbsp; Values against behavioural evidence<br/>
<b>8</b>&nbsp; The thirty-day plan</p>
</div>
</div>
<div>
<h4 class="min">Tables</h4>
<div class="xsmall">
<p>Evidence vocabulary used throughout (front matter)<br/>
Four readings of the single-cause request (Ch. 3)<br/>
Separating guilt, shame and self-punishment (Ch. 4)<br/>
Risk domains: evidence, context, unknowns, bounded conclusion (Ch. 5)<br/>
The five layers of ambition (Ch. 6)<br/>
What the teammate episode does and does not establish (Ch. 7)<br/>
Fourteen tensions with their evidence and test (Ch. 9)<br/>
Fourteen conditional projections (Ch. 10)<br/>
The ten questions and what each would resolve (Ch. 12)<br/>
Sources used and the weight given to each (Ch. 14)</p>
</div>
</div>
</div>
"""


COLOPHON = """
<span class="pagemark">MARKCOLOPHON</span>
<h2 class="sec first"><span class="sn">iv</span>About this document</h2>

<p class="small">Set in EB Garamond for display and headings and Inter for body text, on an A4 portrait
grid. Palette: midnight navy, warm ivory, restrained teal for constructive findings, muted amber for
uncertainty and caution. All figures are original vector artwork generated for this report; no stock
imagery is used.</p>

<h2 class="sec"><span class="sn">v</span>Statement of limitations</h2>

<p>This report was prepared on 26 October 2026 from two written sources: a subject dossier containing
retained facts and summaries of prior conversations, and an exported transcript of a previous
Rishabh–AI conversation. The author has not met the subject, has administered no instrument, has
observed no behaviour, and has obtained no account from any other person.</p>

<p>It follows that the report cannot establish: his true Big Five or HEXACO scores; whether he is
introverted or extraverted; how others experience him; whether his reported distress is persistent,
occasional or situational; how consistently he performs when unobserved; his current political,
religious, gender-related or relationship views; whether any recorded academic, health or routine
detail remains current; whether any project achieved its intended result; whether he has any
psychological or medical condition; and his current safety status, which Chapter 5 addresses as a
retrospective formulation and which no historical transcript can settle.</p>

<p>Three further limits apply. First, several emotionally significant disclosures were made in a
conversation that repeatedly offered confident and totalising explanations of his character, which may
have shaped how he described himself. Second, the transcript mixes first-person disclosure, earlier AI
interpretation and exported notebook material, and its chronology is uncertain. Third, where the
transcript and the dossier conflict, the report flags the conflict rather than reconciling it.</p>

<p>This document is an evidence-informed interpretive report. It is not a clinical evaluation, a
diagnostic assessment, a psychometric assessment, or a suicide, self-harm or violence risk assessment,
and it should not be used as any of those things.</p>

<p class="tiny center" style="margin-top:6mm">THE ARCHITECTURE OF A PERSON &nbsp;·&nbsp; Prepared for
Rishabh Singh &nbsp;·&nbsp; 26 October 2026 &nbsp;·&nbsp; End of report</p>
"""


def chapter_html(ch):
    mark = f'<span class="pagemark">MARK{ch["id"].upper()}</span>'
    head = (f'{mark}<div class="ch-open">'
            f'<span class="ch-num">Chapter {ch["num"]} &nbsp;·&nbsp; {ch["kicker"]}</span>'
            f'<h1 class="ch-title">{ch["title"]}</h1>'
            f'<div class="ch-rule"></div>'
            f'<div class="ch-sub">{ch["sub"]}</div></div>')
    # A page may opt out of the two-column flow with a leading <!--WIDE--> marker.
    # The bibliography uses this: a nested column-span:all block inside a multicol
    # container is pushed to a fresh page by Chromium rather than filling the
    # current one, which wastes most of a page.
    flows, wide = [], []
    for pg in ch["pages"]:
        if pg.lstrip().startswith("<!--WIDE-->"):
            wide.append(pg.replace("<!--WIDE-->", "", 1))
        else:
            flows.append(pg)
    body = ""
    if flows:
        body += '<div class="two-col">' + "\n".join(flows) + "</div>"
    if wide:
        body += '<div class="wide">' + "\n".join(wide) + "</div>"
    return f'<section class="chapter" data-chapter="{ch["id"]}">{head}{body}</section>'


def build_html(folios, words="15,300", pages="23"):
    parts = [cover_html(words=words, pages=pages)]
    parts.append(f'<section class="front">{FRONT}</section>')
    parts.append(f'<section class="front tocpage">{toc_html(folios)}</section>')
    for ch in CHAPTERS:
        parts.append(chapter_html(ch))
    parts.append(f'<section class="colophon">{COLOPHON}</section>')
    return "\n".join(parts)


CSS_PRINT = f"""
@page {{ size: A4 portrait; margin: {M_TOP}mm {M_SIDE}mm {M_BOTTOM}mm {M_SIDE}mm; }}
@page :first {{ margin: 0; }}
"""


def render(body, pdf_path):
    from playwright.sync_api import sync_playwright
    doc = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/>"
           "<title>The Architecture of a Person — Rishabh Singh</title>"
           f"<style>{CSS_PRINT}</style>"
           "<link rel='stylesheet' href='../src/styles.css'/></head><body>"
           + body + "</body></html>")
    tmp = os.path.join(BUILD, "report.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/chromium",
                              args=["--no-sandbox", "--disable-dev-shm-usage",
                                    "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.abspath(tmp), wait_until="load")
        pg.wait_for_timeout(1500)
        pg.pdf(path=pdf_path, format="A4", print_background=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
               prefer_css_page_size=True)
        b.close()
    return tmp


# --------------------------------------------------------- furniture stamping
IVORY = (0.984, 0.973, 0.945)
NAVY = (0.063, 0.102, 0.200)
TEAL = (0.078, 0.431, 0.408)
CHAR3 = (0.431, 0.459, 0.494)
AMBER = (0.757, 0.541, 0.165)


def stamp(src_pdf, dst_pdf, folios, pagemap):
    import pymupdf
    doc = pymupdf.open(src_pdf)
    n = doc.page_count
    for i in range(n):
        page = doc[i]
        if i == 0:                       # cover: full bleed, no furniture
            continue
        # ivory background behind nothing (content already drawn) -> skip
        # navy spine at the left edge, inside the side margin
        page.draw_rect(pymupdf.Rect(0, 0, mm(SPINE_W), mm(PH)),
                       color=None, fill=NAVY, overlay=True)
        # thin teal accent near the foot of the spine
        page.draw_rect(pymupdf.Rect(0, mm(PH) - mm(52), mm(SPINE_W), mm(PH)),
                       color=None, fill=TEAL, overlay=True)

        # chapter membership comes from the located opener pages
        cid = pagemap.get(i + 1)
        ch = next((c for c in CHAPTERS if c["id"] == cid), None)
        if ch:
            label, kicker = f'Chapter {ch["num"]}', ch["kicker"]
            run_title = ch["title"]
        else:
            label, kicker = "Front matter", ""
            run_title = "Personality, Character and Behavioural Analysis"

        # running head: chapter title (right), kicker (left)
        y_head = mm(M_TOP) - mm(4.6)
        page.draw_line(pymupdf.Point(mm(M_SIDE), y_head + mm(2.0)),
                       pymupdf.Point(mm(PW - M_SIDE), y_head + mm(2.0)),
                       color=(0.902, 0.875, 0.812), width=0.4)
        rh_left = (f'{label} · {run_title}' if kicker else "Front matter")
        page.insert_text(pymupdf.Point(mm(M_SIDE), y_head), rh_left,
                         fontname="helv", fontsize=6.0, color=CHAR3)
        if kicker:
            w = pymupdf.get_text_length(kicker.upper(), fontname="helv", fontsize=6.0)
            page.insert_text(pymupdf.Point(mm(PW - M_SIDE) - w, y_head), kicker.upper(),
                             fontname="helv", fontsize=6.0, color=CHAR3)

        # footer: title left, folio right
        y_foot = mm(PH) - mm(M_BOTTOM) + mm(5.2)
        page.draw_line(pymupdf.Point(mm(M_SIDE), y_foot - mm(3.4)),
                       pymupdf.Point(mm(PW - M_SIDE), y_foot - mm(3.4)),
                       color=(0.902, 0.875, 0.812), width=0.4)
        page.insert_text(pymupdf.Point(mm(M_SIDE), y_foot),
                         "Rishabh Singh  ·  Personality, Character and Behavioural Analysis",
                         fontname="helv", fontsize=5.8, color=CHAR3)
        folio = str(i + 1)
        w = pymupdf.get_text_length(folio, fontname="tiro", fontsize=9.0)
        page.insert_text(pymupdf.Point(mm(PW - M_SIDE) - w, y_foot), folio,
                         fontname="tiro", fontsize=9.0, color=NAVY)
    doc.save(dst_pdf, garbage=3, deflate=True)
    doc.close()
    return n


def locate(src_pdf):
    """Find each chapter's first page by matching its unique opener text.

    Hidden markers are unreliable because letter-spaced display type defeats the
    PDF text extractor, so matching on the chapter subtitle (set in normal
    letter-spacing) is the robust route.
    """
    import pymupdf
    doc = pymupdf.open(src_pdf)
    found = {}
    subs = {ch["id"]: " ".join(ch["sub"].split())[:46] for ch in CHAPTERS}
    for i in range(doc.page_count):
        t = " ".join(doc[i].get_text().split())
        if "front" not in found and "How to read this report" in t:
            found["front"] = i + 1
        for ch in CHAPTERS:
            if ch["id"] in found:
                continue
            if subs[ch["id"]] and subs[ch["id"]] in t:
                found[ch["id"]] = i + 1
    n = doc.page_count
    doc.close()
    return found, n


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(BUILD, exist_ok=True)

    folios = {c["id"]: "—" for c in CHAPTERS}
    folios["front"] = "—"
    raw = os.path.join(BUILD, "pass1_raw.pdf")
    render(build_html(folios), raw)
    found, n = locate(raw)
    print("pass1 pages:", n, "located:", found)

    folios.update(found)
    raw2 = os.path.join(BUILD, "pass2_raw.pdf")
    render(build_html(folios), raw2)
    found2, n2 = locate(raw2)
    if found2 != found:
        print("pagination shifted; third pass")
        folios.update(found2)
        raw2 = os.path.join(BUILD, "pass3_raw.pdf")
        render(build_html(folios), raw2)
        found2, n2 = locate(raw2)
    print("final pages:", n2, "folios:", found2)

    # map each page to the chapter whose opener is the nearest at or before it
    order = sorted(((v, k) for k, v in found2.items() if k != "front"))
    pagemap = {}
    for pno in range(1, n2 + 1):
        cid = None
        for v, k in order:
            if v <= pno:
                cid = k
        pagemap[pno] = cid
    final = os.path.join(OUT, "Rishabh_Singh_Personality_Report.pdf")
    stamp(raw2, final, folios, pagemap)

    # the cover states the page and word counts, so measure them from the build
    # itself and re-render once; the cover is a single page either way, so the
    # substituted digits cannot shift pagination.
    import pymupdf
    doc = pymupdf.open(final)
    measured = doc.page_count
    words = sum(len(doc[i].get_text().split()) for i in range(1, measured))
    doc.close()
    if n2 != measured:  # pragma: no cover - defensive
        print("WARNING: page count drifted during stamping")
    print("cover metadata:", words, "words,", n2, "pages")

    final2 = os.path.join(OUT, "_tmp_final.pdf")
    render(build_html(folios, words=f"{words:,}", pages=str(n2)), final2)
    stamp(final2, final, folios, pagemap)
    os.remove(final2)
    print("final:", final, os.path.getsize(final), "bytes")


if __name__ == "__main__":
    main()
