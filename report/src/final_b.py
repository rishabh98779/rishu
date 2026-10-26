"""Chapters 3-4, written to the page budget."""
from figures import fig_siebc


def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


CH3 = {
"id": "ch3", "num": "3", "kicker": "Cognition",
"title": "The Thinking System",
"sub": "How he analyses, how he decides, and when analysis stops helping",
"pages": [
f"""
<p class="lede">Rishabh thinks like someone who has learned that the way to make a problem safe is
to specify it completely. That instinct has produced real competence. It has also produced a habit of
applying the same treatment to questions that specification cannot answer.</p>

<h2 class="sec first"><span class="sn">3.1</span>Analytical habits, curiosity and its domain</h2>

<p>The evidence for how he thinks is unusually concrete, because it is embedded in what he asks for.
Across many subjects the requests have the same shape: define the full scope, represent the structure
visually, work through the mechanism step by step, and do not leave a gap.</p>

<div class="grid2">
<div class="card teal">
<h4>What he asks for, repeatedly</h4>
<ul class="plain" style="margin-bottom:0">
<li>Recursion trees and step-by-step dry runs</li>
<li>Visual representations over prose theory</li>
<li>Complete syllabus coverage, no subtopic omitted</li>
<li>Questions divided by mark value (2, 5, 10)</li>
<li>Textbook depth for university notes</li>
<li>Minimal, targeted edits rather than rewrites</li>
<li>User-input-based, runnable code</li>
</ul>
</div>
<div class="card">
<h4>What the pattern implies</h4>
<p class="body">He is not seeking reassurance that he understands something. He is seeking the
<em>structure</em> of the thing — the shape that lets him verify his own understanding without asking
again. Recursion trees, dry runs and mark divisions all serve the same purpose: they externalise a
check. </p>
</div>
</div>

<p>That is a rational strategy, and the strategy of a competent learner. It is worth noting how far it
has got him: he moved from a Class 11 result of 69 per cent to a Class 12 result of 80 per cent, with a
78.25 per cent Physics–Chemistry–Mathematics aggregate, then passed two Microsoft certification exams
on first attempt. </p>

<p>His curiosity is broad but unevenly distributed. Within technical and conceptual domains it is close
to voracious: data structures, algorithms, database systems, computer architecture, probability,
embedded hardware, hydrological simulation, deployment engineering. Within a second domain — the moral
and psychological — it is intense and self-directed: he reads about caste, about misogyny, about
ideology, and he has spent enormous effort interrogating his own motives.</p>

<p>Outside those two domains the record shows deliberate closure. He has ruled out anime and manga
entirely, not as a preference but as a commitment, and adopted a rule against romantic or sexual
attraction except toward a future partner. Those are not the choices of someone maximally open to
experience; they are the choices of someone who has decided that certain kinds of exposure are unsafe
or unhelpful and has walled them off.</p>

<div class="callout">
<span class="lab">Reading the walls without pathologising them</span>
<p>Rules like these are common in late adolescence and often functional. They reduce decision load, they
protect a valued self-image, and they can be a legitimate response to having noticed that a particular
input makes him worse. They become costly only if they persist past their usefulness, or if they are
maintained by fear rather than choice. The record cannot distinguish those two cases, and the difference
is one he is better placed than anyone to test: a freely chosen rule is restful, while a fear-maintained
one requires continuous monitoring to sustain.</p>
</div>

<h2 class="sec"><span class="sn">3.2</span>Decision-making, and the preparation–execution relationship</h2>



<p>There is a second pattern here that deserves careful statement, because it is easy to overstate. He
prepares extensively. The preparation is high quality. And in several places the record shows the
preparation continuing past the point where it is converting into output: planning study tasks during
holidays without switching off, considering a boxing routine and struggling to sustain it, wanting to
dance and not dancing, and repeatedly asking for a fuller version of material he already has.</p>

<p>Two readings fit. The first is <b>avoidance by preparation</b>: gathering and refining feels
productive while postponing the riskier step of acting or being seen. The second is <b>calibration</b>:
he is genuinely building competence in a demanding field and his thoroughness is proportionate to the
stakes. The record cannot distinguish them, and the difference would be settled by a simple question
the dossier does not answer: does the preparation reliably produce the output it was preparing for?</p>

<div class="pull">The test of preparation is not how good it feels. It is whether the thing it was
preparing for gets done.</div>
""",
f"""
<h2 class="sec first"><span class="sn">3.3</span>The search for a single root cause</h2>

<p>This is the clearest and most repeated cognitive signature in the transcript. He has asked for one
word, a syndrome, a disease, a numerical prediction, a "red flag or green flag" classification, a
mathematical function, and C++ code to model how he receives, interprets and responds to events. He has
asked whether medication or a diagnosis could make the problem easier to handle, and he has recognised
in the same conversation that a label might function as a way of avoiding responsibility.</p>

<table>
<caption>Four readings of the single-cause request</caption>
<thead><tr><th style="width:24%">Reading</th><th style="width:44%">What it predicts</th><th>Status</th></tr></thead>
<tbody>
<tr><td class="k">Intolerance of uncertainty</td><td>Discomfort with unresolved questions drives the search; the answer matters less than closing the question</td><td>{_ev("HYPOTH", "Plausible; repeated seeking, little settling")}</td></tr>
<tr><td class="k">Intellectualisation</td><td>Converting an emotional problem into a technical one makes it tractable and temporarily less painful</td><td>{_ev("HYPOTH", "Fits the technical framing; unverified")}</td></tr>
<tr><td class="k">Analytical learning style</td><td>He reasons in the idiom he knows best — systems, functions, debugging — because it is genuinely useful to him</td><td>{_ev("INFER", "Underrated; must be held open")}</td></tr>
<tr><td class="k">Reassurance-seeking loop</td><td>Each authoritative answer briefly relieves distress and lowers the threshold for seeking the next one</td><td>{_ev("HYPOTH", "Consistent with the dialogue's shape")}</td></tr>
</tbody>
</table>

<p class="tbl-note">No single reading should be adopted. The third is the most respectful of the
evidence and the most easily forgotten, because a technical metaphor for an emotional problem can be a
genuine tool rather than a defence.</p>

<div class="callout caution">
<span class="lab">The interactional confound</span>
<p>The transcript is a long dialogue with a system that repeatedly supplied confident, totalising
explanations — hidden causes, a "core" of the personality, single root causes. A conversation of that
shape can teach a person to narrate themselves in the terms the conversation rewards. This is not a
criticism of Rishabh, and it is not a claim that his distress is invented. It is a reason to treat the
<em>structure</em> of his self-description as partly co-produced, and to weight his concrete, dated,
observable reports more heavily than his summary self-assessments.</p>
</div>

<h2 class="sec"><span class="sn">3.4</span>Systems thinking, and what the thinking system does well</h2>


<div class="grid3">
<div class="card teal"><h4>Demonstrated</h4><p class="body">Choosing stacks appropriate to a problem.
Structuring an application with named components and separate architecture and deployment documents.
Passing certification exams first attempt. Specifying deliverables precisely enough to be
reproduced.</p></div>
<div class="card amber"><h4>Claimed, not demonstrated</h4><p class="body">Breadth of language
proficiency. The résumé lists C++, Java, Python, JavaScript and HTML, plus Arduino, ESP32 and AI
tooling. Evidence exists of use, not of depth in each.</p></div>
<div class="card"><h4>Not established</h4><p class="body">Whether projects were completed to their
intended standard, maintained afterwards, or produced the results their descriptions imply. Persistence
under prolonged difficulty is not observable from a repository's existence.</p></div>
</div>

<p>He converts vague problems into specified ones, which is the single most valuable cognitive habit in
technical work. He learns by reconstructing structure rather than by memorising conclusions. He notices
integration problems that many students miss. He is willing to revise a position he has already
committed to, which is the hardest part of intellectual honesty and the rarest.</p>

<p>What it does less well is stop. Analysis has a stopping rule for a well-formed problem — you are done
when the thing works. It has no natural stopping rule for questions like "am I a good person" or "what
is fundamentally wrong with me," and applying it there produces activity that feels like progress and
is not. The developmental task is not to think less. It is to attach the analytical engine to questions
that can actually be resolved, and to notice the moment when a question has stopped being a problem and
become a way of waiting.</p>
""",
],
}


CH4 = {
"id": "ch4", "num": "4", "kicker": "Affect and regulation",
"title": "The Emotional System",
"sub": "How discomfort is met, and what the record can and cannot establish about it",
"pages": [
f"""
<p class="lede">The emotional material is the most vivid part of the record and the least secure.
What follows separates the sequence he describes from the mechanism that might underlie it, and marks
clearly where the second is inference.</p>

<p>Two things are established. He experiences strong emotion in response to moral content and to
perceived evaluation. He has an explicit, articulated wish to become better at regulating it.
Everything beyond that is a hypothesis, and several competing hypotheses fit the same evidence.</p>

<figure>
{fig_siebc(520)}
<figcaption><b>Figure 4. Situation–interpretation–emotion–behaviour–consequence, with per-link
evidence.</b> The model is a reading aid, not a claim that every episode runs this way. Links marked
<em>documented</em> rest on reports where he described the step directly; links marked <em>inferred</em>
are the analyst's reconstruction of what must connect them. The feedback arrow marks the possibility
that matters most: behaviour that reduces discomfort in the moment tends to make the same appraisal
cheaper to repeat.</figcaption>
</figure>

<h2 class="sec first"><span class="sn">4.1</span>The two candidate loops, and their alternatives</h2>






<h2 class="sec"><span class="sn">4.2</span>Guilt, shame and self-punishment</h2>



<table>
<caption>Separating three things that are often called the same thing</caption>
<thead><tr><th style="width:17%">Construct</th><th style="width:41%">What it is</th><th>What it predicts in this record</th></tr></thead>
<tbody>
<tr><td class="k">Guilt</td><td>Discomfort about a specific act, with a reparative pull toward the person affected</td><td>{_ev("INFER", "Present: he names specific acts and has said he tries not to repeat mistakes")}</td></tr>
<tr><td class="k">Shame</td><td>Discomfort about the self as a whole, with a pull toward hiding or withdrawal</td><td>{_ev("SELF", "Present and explicitly described: self-hatred, no redeeming qualities, disclosing it to others")}</td></tr>
<tr><td class="k">Self-punishment</td><td>Inflicting suffering on oneself as a way of settling a moral debt</td><td>{_ev("SELF", "Stated as a rule; he reports it as past or superseded, which is unverified")}</td></tr>
</tbody>
</table>

<p class="tbl-note">The three are not a ladder from bad to good. They are different processes with
different consequences, and only guilt reliably improves behaviour.</p>

<div class="callout caution">
<span class="lab">Why self-punishment is not a form of accountability</span>
<p>Punishing oneself feels like taking responsibility, and it is important to say clearly that it is
not. Research on guilt and self-punishment describes a pattern in which people who feel responsible for
a harm voluntarily accept suffering — sometimes in ways that help no one — because suffering appears to
restore a moral balance. The difficulty is that this settles the account internally while leaving the
affected person unaffected. Genuine accountability is specific, directed at the person harmed, and
finite: acknowledge the act, repair what can be repaired, change what produced it, and stop.
Self-punishment is unbounded, directed inward, and never quite completes, which is why it can persist
for years while changing nothing.</p>
</div>

<p>There is a second reason for care here. He has connected the self-punitive rule to wanting to be
morally different from people who justify harm. If that link is real, the rule is doing identity work:
it is proof of membership in the category of people who take harm seriously. That makes it
self-reinforcing, because abandoning the punishment would feel like losing the proof. This is an
inference, and a testable one: if self-punishment is identity work, then reducing it should produce
anxiety about becoming indifferent, whereas if it is genuine remorse, reducing it should feel like
relief.</p>
""",
f"""
<h2 class="sec first"><span class="sn">4.3</span>Composure, suppression and the stoicism question</h2>

<p>He wants to become more stoic and better at controlling emotional reactions. The important question
is what he means by control, because two very different programmes sit behind that word.</p>

<div class="grid2">
<div class="card teal">
<h4>Regulation</h4>
<p class="body">Feeling the emotion fully and choosing the response. Discomfort is information and is
allowed to be present. The target is the <em>action</em>, not the feeling. In the Stoic sources this is
the distinction between an impression and an assent — the feeling may arise, and what is up to you is
what you do next.</p>
</div>
<div class="card amber">
<h4>Suppression</h4>
<p class="body">Preventing the emotion from being felt or shown. Discomfort is treated as a failure of
control. The target is the <em>experience</em>, and the strategy is effortful concealment. This
reliably costs: it requires continuous monitoring, it reduces the information available about what
matters, and it tends to surface later as strain.</p>
</div>
</div>

<p>The record contains evidence for both and does not settle which he is pursuing. On the regulation
side: he distinguishes genuine injustice from situations where dwelling stops being productive, which
is exactly the Stoic discrimination. On the suppression side: he describes a diplomatic style that
avoids displaying frustration or anxiety socially, and he has described self-punishment as an internal
practice rather than as something expressed. He also describes a great deal of internal monitoring
without much description of sharing difficulty with another person.</p>

<div class="pull">Composure and stability are not the same thing. A person can look calm because
nothing is disturbing them, or because they have become expert at not letting it show.</div>

<p>The practical difference is easy to test. Regulation shows up as recovering faster from upset while
still being able to say what upset you. Suppression shows up as not being upset in the first place, or
as being unable to say. Only one of those is sustainable over decades, and only one of them is what the
Stoics were actually describing.</p>

<h2 class="sec"><span class="sn">4.4</span>Empathic concern versus personal distress</h2>

<p>An important distinction in the empathy literature separates <em>empathic concern</em> — feeling for
another person, which tends to produce helping — from <em>personal distress</em> — feeling overwhelmed
by one's own reaction to their suffering, which tends to produce withdrawal or self-protection. The two
feel similar from inside and have opposite behavioural consequences.</p>

<p>Several features of the record point toward the second being active alongside the first. He describes
hearing about harm to women and blaming himself for sharing a gender with perpetrators. He describes
collective self-blame about abuse involving Indians. He describes being left crying and unable to
concentrate by outrage content. In each case the emotional response is intense, and in each case the
response is about <em>his</em> position relative to the harm rather than about the person harmed.</p>


<div class="callout">
<span class="lab">A testable implication</span>
<p>If his reaction to injustice is mostly empathic concern, then exposure to an account of harm should
leave him thinking about the person affected and inclined toward a concrete act. If it is mostly
personal distress, the same exposure should leave him thinking about himself — his category, his
complicity, his own moral standing — and inclined toward rumination. He is in a position to notice which
happens, and noticing is the first step to shifting it.</p>
</div>
""",
f"""
<h2 class="sec first"><span class="sn">4.5</span>What the emotional record establishes, and what it does not</h2>

<div class="grid2">
<div class="card">
<h4>Established</h4>
<p class="body">He experiences strong negative emotion in moral and evaluative situations. He has
described self-hatred, guilt, self-punitive thinking and collective self-blame in his own words and at
length. He reports bodily and cognitive signs of self-consciousness in specific social situations, with
at least one counterexample of improvement. He has described intrusive-feeling imagery in moral and
political contexts, in the past tense and without reference to current intent or action. He wants to
change how he handles all of this, and he has thought about it carefully.</p>
</div>
<div class="card amber">
<h4>Not established</h4>
<p class="body">Whether any of this is current, or how current. Whether it is frequent or occasional.
Whether it causes functional impairment, and if so where. Whether it is situational or pervasive.
Whether his self-descriptions have been shaped by the questions he was asked and the confident answers
he received. Whether he has any psychological or medical condition. His safety status now, which this
document cannot assess and does not assess.</p>
</div>
</div>

"""
],
}
