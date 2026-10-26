# The Architecture of a Person

A comprehensive personality, character and behavioural analysis prepared for
**Rishabh Singh**, and the source code that builds it.

The deliverable is a 23-page A4 report, typeset as a premium behavioural
research monograph. This repository contains the finished PDF, the sources that
generate it, and the reference data used to verify its citations.

## Deliverable

| File | Description |
|---|---|
| `out/Rishabh_Singh_Personality_Report.pdf` | The finished 23-page report (vector text and charts) |

## Repository layout

```
report/
├── out/         finished PDF
├── src/         report generator (Python + CSS)
├── fonts/       EB Garamond and Inter, the display and body typefaces
└── research/    resolved bibliography data and the DOI verification scripts
```

### `src/`

| File | Role |
|---|---|
| `build2.py` | Build driver. Two-pass render, folio resolution and stamping. |
| `styles.css` | Print stylesheet: A4 page box, palette, type scale. |
| `content.py` | Chapter aggregator and shared evidence-tagging helper. |
| `final_a.py` | Chapters 1–2 |
| `final_b.py` | Chapters 3–4 |
| `content_b.py` | Chapter 5 |
| `content_c.py` | Chapters 6–8 |
| `content_d.py` | Chapters 9–12 |
| `content_e.py` | Chapter 13, bibliography and reference groups |
| `figures.py` | Vector figures and the cover artwork |
| `build.py`, `reflow.py`, `qa_layout.py` | Earlier build and layout-QA utilities |

### `research/`

`dois*.json` hold the resolved Crossref records for the bibliography;
`verify*.py` are the scripts that resolved and validated them.

## Building

The generator needs Python 3, Playwright with a Chromium build, and PyMuPDF.

```bash
pip install playwright pymupdf requests
playwright install chromium
cd src && python3 build2.py
```

The build renders twice. The first pass produces a raw PDF used to locate each
chapter's opening page; the second renders with resolved folios. Page numbers,
running heads and footers are then stamped into the page margins with PyMuPDF,
and the cover's page and word counts are measured from the finished document
itself rather than hard-coded.

Output lands in `out/Rishabh_Singh_Personality_Report.pdf`.

## Method

The report is an evidence-informed interpretive document. It was produced
without meeting its subject, without administering any instrument, and without
access to any observer account. It is **not** a clinical evaluation, a
diagnostic assessment, a psychometric assessment, or a suicide, self-harm or
violence risk assessment, and it should not be used as any of those things.

Two sources were used:

1. A subject dossier of retained facts, dated academic history, project records
   and stated preferences.
2. *The Architecture of Internal Liberation* — a long export of a previous
   Rishabh–AI conversation, mixing first-person disclosure, earlier AI
   interpretation and notebook material.

The second source is weighted accordingly: moderate for what he reported
believing, fearing and wanting; low for frequency, severity and current status;
and not evidence about him at all where the text is the previous AI's assertion.

Every substantive claim carries an evidence tag:

| Tag | Meaning |
|---|---|
| `direct` | a dated, checkable fact in the dossier |
| `artefact` | something that exists independently of his account |
| `self` | his own first-person report, uncorroborated |
| `infer` | a reading drawn by the analyst |
| `hypoth` | a testable possibility, offered with the test stated |

## Citation verification

The bibliography cites 78 unique DOI-linked sources. Each was resolved against
the Crossref API and checked against publisher metadata; all 78 resolved
successfully. Some publisher landing pages return HTTP 403 to automated
requests, which is bot-blocking rather than a bad identifier — the Crossref
record is the authority used here.

External research is used only to explain frameworks and established general
findings. It is never used to verify anything about the subject.

## Privacy

The published report contains no personal identifiers: no student or
institutional numbers, email addresses, account handles, examination ranks or
third-party names. Peers are referred to by role.

`src/content_mid.py` is a superseded draft that still contains dated personal
academic history. It is dead code — `content.py` takes those chapters from
`final_b.py` — and it is excluded via `.gitignore` rather than published.

## Licence

The report text and figures are personal and confidential material prepared for
the named subject. The build code is provided for reproducibility.
