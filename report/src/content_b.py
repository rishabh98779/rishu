"""Chapters 4-5 of the report. Condensed to the page budget."""


def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


# ============================================================ CHAPTER 4
# ============================================================ CHAPTER 5
CH6 = {
"id": "ch6", "num": "6", "kicker": "Achievement",
"title": "Ambition, Standards and Conscientiousness",
"sub": "Separating ambition from planning, planning from effort, and effort from outcome",
"pages": [
f"""
<p class="lede">Ambition is easy to observe and easy to mistake for its downstream consequences.
This chapter keeps five things apart: what he wants, what he plans, what he does, what he
sustains, and what results.</p>

<table>
<caption>The five layers, and the evidence at each</caption>
<thead><tr><th style="width:16%">Layer</th><th style="width:48%">Evidence in the record</th><th>Assessment</th></tr></thead>
<tbody>
<tr><td class="k">Wants</td><td>Software development and technical internships; longer-term interest in game development; stated priority on DSA and web development over aptitude practice</td><td>{_ev("SELF", "Clear and repeated")}</td></tr>
<tr><td class="k">Plans</td><td>Structured syllabus coverage; AMCAT preparation with a specified CBT interface and at least four sample sets; hackathon presentation planning; semester scheduling around internal test windows</td><td>{_ev("DIRECT", "Detailed and dated")}</td></tr>
<tr><td class="k">Does</td><td>Two Microsoft certifications passed first attempt; AI-900 score of 834/1000 after roughly 1,000 practice questions; multiple project repositories; hackathon participation</td><td>{_ev("DIRECT", "Substantial and verifiable")}</td></tr>
<tr><td class="k">Sustains</td><td>Stated goal of greater consistency; difficulty holding a boxing routine after evening classes; automatic study planning during holidays; sleep often under six hours in one period</td><td>{_ev("SELF", "The weakest layer in the record")}</td></tr>
<tr><td class="k">Outcomes</td><td>Academic results improved from 69% (Class 11) to 80% (Class 12); prior CGPA of 8.43 reported; current third-semester status</td><td>{_ev("DIRECT", "Positive trend, dated")}</td></tr>
</tbody>
</table>

<p class="tbl-note">The gap that matters is between <em>Plans</em> and <em>Sustains</em>. The record
is strong at the first two layers and thin at the fourth, which is a common and specific profile
rather than a general weakness.</p>

<h2 class="sec"><span class="sn">6.1</span>What the achievements actually show</h2>


<p>The academic trajectory is more informative than any single result. Class 10 at 88 per cent,
Class 11 at 69 per cent, Class 12 at 80 per cent with a 78.25 per cent PCM aggregate. A drop in
Class 11 followed by recovery is a common pattern and often reflects disruption rather than
capacity. He has attributed importance to a difficult period during school; the dossier does not
establish causation, and a recovering trend is at least as consistent with resilience as with
lasting damage.</p>

<div class="callout">
<span class="lab">A counterweight to the conscientiousness concern</span>

</div>

<h2 class="sec"><span class="sn">6.2</span>Learning preferences as strategy, not fussiness</h2>

<p>His requirements for study material are specific enough that they could be read as difficulty
being satisfied. Read against the evidence, they look more like an accurate model of how he learns.</p>

<ul class="tick">
<li><b>Visual and structural over discursive.</b> Recursion trees, dry runs, diagrams, interactive
materials. He is asking for the representation that lets him verify understanding without
re-reading prose.</li>
<li><b>Complete coverage.</b> No subtopic missing, university notes as a subset of a fuller text.
He is managing the risk of discovering a gap during an exam.</li>
<li><b>Mark-weighted organisation.</b> Two, five and ten mark divisions. He is allocating effort by
return, which is an exam-strategy judgement rather than a completeness instinct.</li>
<li><b>Efficiency over volume.</b> He dislikes long, slow explanations. He wants depth without
padding.</li>
</ul>



<p>The honest test is simple and he is the only person who can run it. Take a topic he has studied
thoroughly. Ask whether the material he gathered was used, and whether the marks reflected it. If
yes, his thoroughness is an asset and should be left alone. If the gathering has repeatedly outrun
the studying, that is the finding.</p>
""",
f"""""",
],
}
