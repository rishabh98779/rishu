"""Chapter 14: research, methodology and bibliography.

The bibliography is generated from Crossref metadata verified by DOI lookup during
preparation, so author names, titles, journals, volumes, pages and years come from the
publisher's own record rather than being reconstructed from memory.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "research")

GROUPS = [
    ("Personality structure, models and measurement", [
        "10.1037/0022-3514.52.1.81", "10.1037/a0037250",
    ]),
    ("Observation, self-report and the limits of inference", [
        "10.1037/0033-295X.84.3.231", "10.1037/a0038889",
    ]),
    ("Identity, self-concept and value formation", [
        "10.1037/0022-3514.70.1.141", "10.1037/0022-3514.83.6.1423",
    ]),
    ("Self-criticism, shame, guilt and self-punishment", [
        "10.1037/a0014540",
    ]),
    ("Self-compassion and self-worth contingencies", [
        "10.1080/15298860309027",
    ]),
    ("Emotion regulation, rumination and repetitive thought", [
        "10.1037/0022-3514.85.2.348",
    ]),
    ("Uncertainty, need for closure and the search for a single cause", [
        "10.1016/0191-8869(94)90048-5",
    ]),
    ("Social evaluation, self-focused attention and social difficulty", [
        "10.1037/0033-2909.107.2.156", "10.1016/j.beth.2010.04.007",
    ]),
    ("Intrusive thoughts and their appraisal", [
        "10.1037/0033-2909.134.2.163",
    ]),
    ("Empathy, personal distress and prosocial behaviour", [
        "10.1037/0022-3514.44.1.113",
    ]),
    ("Group identity, collective guilt and moralised anger", [
        "10.1037/0022-3514.75.4.872",
    ]),
    ("Gender attitudes, idealisation and objectification", [
        "10.1037/0022-3514.70.3.491",
    ]),
    ("Perfectionism, achievement motivation and goal pursuit", [
        "10.1007/BF01172967", "10.1007/s12160-013-9486-6",
    ]),
]

BOOKS = [
    ("Peterson, C., &amp; Seligman, M. E. P. (2004). <b>Character strengths and virtues: A handbook "
     "and classification.</b> Oxford University Press / American Psychological Association."),
    ("Hayes, S. C., Strosahl, K. D., &amp; Wilson, K. G. (2012). <b>Acceptance and commitment "
     "therapy: The process and practice of mindful change</b> (2nd ed.). Guilford Press."),
    ("Neff, K. D., &amp; Germer, C. K. (2018). <b>The mindful self-compassion workbook.</b> "
     "Guilford Press."),
    ("American Psychiatric Association. (2022). <b>Diagnostic and statistical manual of mental "
     "disorders</b> (5th ed., text rev.). Cited only to state explicitly that no diagnostic "
     "criteria were applied and no diagnosis is offered or implied."),
    ("World Health Organization. (2019). <b>International classification of diseases for mortality "
     "and morbidity statistics</b> (11th rev.). Cited for the same reason."),
]


def _load():

    seen = {}
    for f in ("dois.json", "dois2.json", "dois3.json", "dois4.json"):
        p = os.path.join(RES, f)
        if not os.path.exists(p):
            continue
        for r in json.load(open(p)):
            if r.get("ok") and r.get("doi") and r.get("title"):
                k = r["doi"].lower().replace("//", "/")
                seen.setdefault(k, r)
    return seen


def _fmt(r):

    parts = [p.strip() for p in (r.get("authors") or "").split(";") if p.strip()]
    names = []
    for p in parts:
        if " " in p:
            fam, ini = p.rsplit(" ", 1)
            names.append(f"{fam}, {ini}")
        else:
            names.append(p)
    authors = "; ".join(names[:3]) + (", et al." if len(parts) > 3 else "")
    yr = r.get("year") or "n.d."
    title = r["title"].strip().rstrip(".")
    cont = (r.get("container") or "").strip()
    vol, iss, pg = r.get("volume"), r.get("issue"), r.get("page")
    doi = r["doi"]
    s = f"{authors} ({yr}). <b>{title}.</b> "
    if cont:
        s += f"<i>{cont}</i>"
        if vol:
            s += f", <i>{vol}</i>"
        if iss:
            s += f"({iss})"
        if pg:
            s += f", {pg}"
        s += ". "
    s += f'<a href="https://doi.org/{doi}">doi.org/{doi}</a>'
    return s


def bibliography_html():

    idx = _load()
    out = []
    for gname, dois in GROUPS:
        rows, used = [], set()
        for d in dois:
            k = d.lower().replace("//", "/")
            if k in used:
                continue
            r = idx.get(k)
            if not r:
                continue
            used.add(k)
            rows.append(_fmt(r))
        rows.sort(key=lambda s: s.lower())
        if not rows:
            continue
        out.append(f'<h3 class="sub">{gname}</h3><div class="refs">')
        for s in rows:
            out.append(f'<div class="r">{s}</div>')
        out.append("</div>")
    out.append('<h3 class="sub">Books, manuals and classification systems</h3><div class="refs">')
    for s in BOOKS:
        out.append(f'<div class="r">{s}</div>')
    out.append("</div>")

    return '<div class="cols2">' + "\n".join(out) + "</div>"


_M1 = """
<p class="lede">This report was produced without meeting its subject, without administering any
instrument and without access to any observer account. Those are not incidental limitations; they
define what it can and cannot claim.</p>

<h2 class="sec first"><span class="sn">14.1</span>The evidence base, and the weight given to each source</h2>

<table>
<thead><tr><th style="width:23%">Source</th><th style="width:41%">What it is</th><th>Weight given</th></tr></thead>
<tbody>
<tr><td class="k">Subject dossier</td><td>Retained facts, dated academic history, project records, stated preferences, health and routine notes, communication preferences</td><td><b>Highest</b> for dated facts and artefacts; <b>moderate</b> for stated preferences, which are self-descriptions about what he wants</td></tr>
<tr><td class="k"><i>The Architecture of Internal Liberation</i></td><td>A long export of a previous Rishabh&ndash;AI conversation, mixing first-person disclosures, earlier AI interpretations and notebook/export material</td><td><b>Moderate</b> for what he reported believing, fearing and wanting; <b>low</b> for frequency, severity, persistence and current status; <b>not evidence about him</b> where the text is the prior AI's assertion</td></tr>
<tr><td class="k">Verified external research</td><td>Peer-reviewed literature and established frameworks, located by DOI and confirmed against publisher metadata</td><td>Used <b>only</b> to explain frameworks and established general findings. Never used to verify anything about Rishabh</td></tr>
<tr><td class="k">Analyst inference</td><td>Readings drawn by the analyst from the two sources above</td><td>Labelled as inference throughout, with the alternative stated wherever one exists</td></tr>
</tbody>
</table>

<h2 class="sec"><span class="sn">14.2</span>Source quality: the supplementary PDF</h2>

<p>The second source needs an explicit statement because it is easily misread as a clinical record. It is
not: it is a very long dialogue between one person and an AI system, shaped by the questions he asked and
the answers he received. <b>It is not a clinical interview.</b> There was no structured assessment, no diagnostic criteria,
no history-taking protocol and no collateral information; its length reflects engagement, not severity.
First-person disclosure, AI interpretation and exported notebook material appear together without clear
boundaries, events from different periods are compressed, and some references conflict. <b>It also
contains the prior AI's own interpretations</b> — several replies assert hidden causes, a "core" of the
personality, moral verdicts and diagnostic-sounding labels, in confident and sometimes shaming language.
Those statements are part of the conversation history, not evidence about Rishabh, and are not cited as
authority anywhere here.</p>

<p>One consequence is a genuine confound: a person asked repeatedly about the hidden root of their
difficulties will tend to produce one. The <em>shape</em> of that self-description is partly a product
of the interaction, which is a reason to weight his concrete, dated and artefact-backed reports more
heavily than his summary self-assessments — not a reason to doubt that he was describing something
real.</p>

<h2 class="sec"><span class="sn">14.3</span>How claims are labelled</h2>

<p>The five evidence tags are defined in the front matter and used consistently throughout. Four
further distinctions are maintained.</p>

<div class="callout plain">
<span class="lab">Four distinctions the report maintains throughout</span>
<p><b>Established theory versus measurement of this person.</b> The Big Five, HEXACO, the VIA
classification, self-compassion and intolerance of uncertainty are frameworks used here as lenses. None
was measured in Rishabh, and no score or percentile appears anywhere in this document.</p>
<p><b>Self-report versus observed behaviour.</b> Every behavioural claim comes from his own account —
not a reason to distrust him, but a reason not to treat frequency and severity as known.
<b>Thought versus intention versus action:</b> a passing thought is not a wish, a wish is not a plan,
and a plan is not an act. The report never upgrades one into another, in either direction.</p>
<p><b>Research findings versus claims about Rishabh.</b> The cited literature explains how phenomena
generally work. It cannot confirm that any of them applies to him, and no citation here should be read
as doing so.</p>
</div>
"""

_M2 = """<!--WIDE-->
<h2 class="sec first"><span class="sn">14.4</span>Bibliography</h2>

<p class="small">Journal references were located by DOI and confirmed against the publisher's own
metadata for author names, title, journal, volume, issue, pages and year. Where a work is cited, it is
cited to explain an established framework or finding — never to establish a fact about Rishabh.</p>

{bibliography}

<div class="callout caution">
<span class="lab">How external research is used here, and the status of Chapter 5</span>
<p>Every framework is a lens and nothing more. The Big Five and HEXACO taxonomies organise what the
record shows; they supply no score, and the ordinal estimates in Chapter 2 are the analyst's readings
rather than instrument output. The emotion-regulation, self-compassion, self-focused attention,
intolerance-of-uncertainty, collective-guilt and intrusive-thought literatures explain how the relevant
phenomena generally behave in people; none can tell us whether any applies to Rishabh. Chapter 5 is a
retrospective, evidence-bounded reading of risk-relevant material in the written source. It is not a
clinical, suicide or violence risk assessment, assigns no tier, probability or validated score, and does
not establish present acute risk in either direction. What it distinguishes — a self-sacrificial
statement tied to an idealised figure, and a separate episode of escalating anger with violent imagery —
is bounded by what a transcript can show, and assessing current risk requires a direct, qualified,
current assessment. Historical disclosure neither proves nor disproves present safety.</p>
</div>
"""

CH14 = {
    "id": "ch14", "num": "14", "kicker": "Method and sources",
    "title": "Research and Methodology",
    "sub": "What kind of evidence this report rests on, and how each claim should be weighted",
    "pages": [_M1, _M2.format(bibliography=bibliography_html())],
}
