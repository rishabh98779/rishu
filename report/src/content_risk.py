"""Chapter 5: Safety and Risk Formulation.

A retrospective, evidence-bounded account of risk-relevant material in the
source. This is not a clinical risk assessment and cannot establish present
acute risk. The chapter is written to the instruction that the two explicit
first-person disclosures in the source -- a self-sacrificial statement tied to
an idealised fictional figure, and a separate episode of escalating anger with
recurrent violent imagery -- are material historical signals that must be
reported plainly rather than softened, while not being upgraded into intent,
plan or action, and not being downgraded into harmless symbolism.
"""
from figures import fig_risk


def _ev(kind, s):
    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


_RISK_DOMAINS = [
    dict(name="Self-directed", tone="high",
         historical="A first-person statement that he wanted to kill himself for an "
                    "idealised fictional figure so that his death would have purpose, "
                    "alongside reported exhaustion, self-hatred and self-punishment.",
         current="Wish to die now; intent; plan; means; preparations; past attempts or "
                 "self-injury; ability to stay safe."),
    dict(name="Harm to others", tone="high",
         historical="A separate episode in which political videos were reported to be "
                    "escalating rage beyond what he felt able to control, with recurring "
                    "imagery of butchering people.",
         current="Whether imagery persists; intensity and recency; any target, plan or "
                 "preparation; history of real-world violence; impulse control."),
    dict(name="Escalation and vulnerability", tone="mid",
         historical="Emotional overload, punitive self-monitoring, collective guilt, and "
                    "repeated exposure to rage-inducing short-form content.",
         current="Current exposure; sleep; substance use; acute stressors; whether any "
                 "threshold described is still being reached."),
    dict(name="Protective and stabilising", tone="mid",
         historical="Stated commitment to empathy and restraint, explicit wish not to harm, "
                    "willingness to disclose distress, and concrete academic and career goals.",
         current="Whether these remain active, and whether any support is currently engaged. "
                 "Insight and remorse are not proof that risk is absent."),
    dict(name="Functional and social", tone="mid",
         historical="Situational social stiffness, self-consciousness, and difficulty "
                    "switching out of a work mode into rest.",
         current="Whether this causes impairment in daily life, and in which settings."),
]


CH5 = {
"id": "ch5", "num": "5", "kicker": "Safety and risk",
"title": "Safety and Risk Formulation",
"sub": "Historical signals in the source, and what cannot be established about the present",
"pages": [
f"""
<p class="lede">This chapter is required, and it is not a disclaimer. The source contains two
explicit first-person disclosures that are risk-relevant. They are reported here plainly, because
softening them would misrepresent the record, and they are bounded carefully, because a historical
transcript cannot establish present risk in either direction.</p>

<div class="callout caution">
<span class="lab">What this chapter is, and what it is not</span>
<p><b>It is</b> a retrospective, evidence-bounded account of risk-relevant material in a written
source, separating what the source contains from what a qualified assessor would need to know.
<b>It is not</b> a clinical, suicide or violence risk assessment, and not a diagnosis. No instrument
was administered, no interview took place, no collateral information was obtained, and no risk tier,
probability or score is assigned anywhere below.</p>
</div>

<h2 class="sec first"><span class="sn">5.1</span>Self-directed risk</h2>

<p>The source records a first-person statement that Rishabh wanted to kill himself for an idealised
figure — Paul Atreides, from <em>Dune</em> — so that his death would have purpose.
{_ev("SELF", "This is his own statement, in a long exported conversation, and it is material.")} It
sits within a broader reported pattern: exhaustion, a wish for the struggle to end, self-hatred, and
a self-punitive rule he described as settling a moral debt.</p>

<p>This deserves to be read as a suicidal or self-sacrificial signal rather than dismissed as
symbolism. A person can hold a wish for death organised around meaning rather than despair, and a
meaningful frame does not make the signal smaller. The previous AI's response in the source — that he
did not really want to die — was an interpretation offered at the time, not a verified finding, and it
is not treated here as evidence that the signal is benign.</p>

<p>Two things follow with equal weight. The source records no plan, preparation, access to means,
attempt or statement of present intent. And the statements span a long dialogue that may not describe
a single moment or a current state. Neither point licenses the conclusion that risk is absent; both
mean it cannot be characterised from this material.</p>

<h2 class="sec"><span class="sn">5.2</span>Risk of harm to others</h2>

<p>Separately, the source records an episode in which Rishabh reported that political videos were
escalating his anger beyond what he felt able to control, and that vivid imagery of butchering people
was recurring in his mind.
{_ev("SELF", "A first-person account of an internal state, reported in the past tense.")}</p>

<p>This is not the same disclosure as the first and should not be merged with it: it describes
anger and imagery, not a wish, plan, target or act. It should also not be reduced to "just intrusive
thoughts", because the source describes the anger reaching a threshold he could not control, and that
reported loss of control is the specific element warranting attention. Whether the imagery was
intrusive and unwanted, or elaborated and deliberate, cannot be determined from the transcript, and
the two carry different implications. The record contains no indication of a real-world target, plan,
preparation or act of violence — and no information that would rule one out. Political anger of this
kind is not a diagnosis, and is not treated as one here.</p>

<figure>
{fig_risk(_RISK_DOMAINS, 520)}
<figcaption><b>Figure 5. Risk-relevant domains.</b> The hatched column is an absence of
information, not a favourable reading.</figcaption>
</figure>
""",
f"""
<h2 class="sec first"><span class="sn">5.3</span>Escalation and vulnerability factors</h2>

<p>The following factors are recorded in the source and are relevant to how risk might escalate.
None of them is claimed to have caused anything, and none establishes a diagnosis.</p>

<div class="grid2">
<div class="card amber">
<h4>Reported in the source</h4>
<p class="body"><b>Emotional overload</b> — crying, overwhelm and difficulty concentrating after
exposure to rage-inducing content. <b>Punitive self-monitoring</b> — a rule that harm done should be
answered with self-inflicted mental suffering. <b>Exhaustion</b> — periods of under six hours of
sleep, and a reported wish for the struggle to end. <b>Collective guilt</b> — taking personal
responsibility for the wrongdoing of a group he belongs to. <b>Repeated exposure</b> — short-form
political content described as directly increasing his anger.</p>
</div>
<div class="card">
<h4>Why these matter, and their limits</h4>
<p class="body">Each of these is a recognised way in which distress can intensify: they reduce the
capacity for reflection, shorten the distance between feeling and action, and make extreme
conclusions feel more available. That is a statement about general mechanisms, not about him. The
source records these as reported states at unspecified times. It does not record their current
frequency, their severity, or whether they cluster together. Elevated vulnerability is not the same
as elevated risk, and this report does not equate them.</p>
</div>
</div>

<h2 class="sec"><span class="sn">5.4</span>Protective and stabilising factors</h2>

<p>Several factors in the record point away from risk. They are listed because omitting them would
distort the picture, and each is stated with its limit, because a protective factor is not a
guarantee.</p>

<ul class="tick">
<li><b>Stated restraint and an explicit wish not to harm others</b> — wanting women to feel safe
around him, objecting to degrading talk, holding rules against humiliating people.
<em>Limit:</em> stated values and conduct under pressure differ, and the record contains one
documented lapse (Chapter 7).</li>
<li><b>Willingness to disclose distress.</b> He described self-hatred openly, including in front of
classmates and a teacher. <em>Limit:</em> disclosure to an AI conversation is not the same as
disclosure to a person who can act, and it is not treatment.</li>
<li><b>Reflection on consequences and a stated wish to change.</b> <em>Limit:</em> insight and
remorse are not protective in themselves. People who act on violent thoughts frequently understand
that they are wrong.</li>
<li><b>Concrete future-oriented goals</b> — technical education, certifications, projects, a
longer-term interest in game development. <em>Limit:</em> goals indicate reasons to continue; they do
not establish that risk is absent, and they are not a substitute for assessment.</li>
<li><b>Reported attachment to family.</b> <em>Limit:</em> the record does not describe what he has
disclosed to them, or what they know.</li>
</ul>

<div class="callout">
<span class="lab">How to read the protective column</span>
<p>The presence of protective factors changes the balance of an assessment. It does not close it.
Every item above is a self-report, most are stated intentions rather than observed behaviour, and none
addresses whether self-harm or violent thoughts are current. They are reasons for a careful,
non-alarmist reading — not a basis for reassurance.</p>
</div>

<h2 class="sec"><span class="sn">5.5</span>Critical unknowns</h2>

<p>The following are marked <b>unknown</b>, not "no". The source does not establish any of them, and
a report of this kind must not convert silence into a negative finding.</p>

<div class="grid2">
<div class="card">
<h4>Self-directed</h4>
<p class="body">Whether any wish to die is present now. Its frequency, intensity and recency. Whether
there is intent. A plan, preparations, or access to means. Any past attempt or episode of self-injury.
Whether the specific statement about sacrifice was a momentary thought, a repeated one, or something
he found compelling. His current ability to stay safe, and his own confidence in it.</p>
</div>
<div class="card">
<h4>Harm to others</h4>
<p class="body">Whether violent imagery is current. Whether it is intrusive and unwanted, or
elaborated and deliberate. Any specific target. Any plan, preparation or rehearsal. Any history of
real-world violence or loss of control. Current substance use. The triggers that precede escalation,
and whether he can interrupt it.</p>
</div>
</div>

<p class="tbl-note">Support and context are equally unknown: who currently knows about any of this,
whether any professional has been seen, whether there has been any prior assessment, and what his
day-to-day circumstances are now.</p>

<h2 class="sec"><span class="sn">5.6</span>Formulation</h2>

<table>
<caption>Risk domains: historical evidence, context, unknowns and bounded conclusion</caption>
<thead><tr><th style="width:15%">Risk domain</th><th style="width:27%">Historical evidence</th>
<th style="width:22%">Protective / contextual evidence</th>
<th style="width:20%">Critical unknowns</th><th>Bounded conclusion</th></tr></thead>
<tbody>
<tr>
<td class="k">Self-directed / suicidal</td>
<td>A first-person statement of wanting to kill himself for an idealised figure so his death would
have purpose; reported exhaustion, self-hatred and self-punishment</td>
<td>Stated goals; family attachment; willingness to disclose; no recorded plan, means, preparation or
attempt</td>
<td>Present wish to die; intent; plan; means; recency; past attempts; ability to stay safe</td>
<td>A material historical signal requiring direct follow-up. No present-risk characterisation is
possible from this source.</td>
</tr>
<tr>
<td class="k">Harm to others / violent ideation</td>
<td>A separate reported episode: political videos escalating rage beyond felt control, with recurring
imagery of butchering people</td>
<td>Stated restraint and explicit wish not to harm; objection to degrading talk; no recorded target,
plan or act</td>
<td>Currency, intrusiveness, target, plan, preparation, violence history, impulse control</td>
<td>A material historical signal requiring direct follow-up. Cannot be read as intent, and cannot be
read as harmless.</td>
</tr>
<tr>
<td class="k">Escalation and functional vulnerability</td>
<td>Emotional overload, punitive self-monitoring, collective guilt, exhaustion, repeated
rage-content exposure, social stiffness</td>
<td>Insight, stated wish to change, structured academic and technical engagement</td>
<td>Current exposure, sleep, stressors, impairment across settings, substance use</td>
<td>Plausible intensifying factors, reported at unspecified times. Not established as current or
clustered.</td>
</tr>
</tbody>
</table>

<div class="grid2">
<div class="card teal">
<h4>Historical formulation</h4>
<p class="body">The source contains serious, explicit historical self-sacrificial and suicidal
language, and a separate episode of escalating anger with violent imagery. Both are material risk
signals that deserve attention and direct follow-up. Neither is proof that he has acted or will act.
The statements are bounded by what a transcript can show: what he reported, in one long conversation,
at some point in the past.</p>
</div>
<div class="card amber">
<h4>Current acute risk</h4>
<p class="body"><b>Cannot be determined from this historical AI conversation alone.</b> No tier, no
probability and no validated score is assigned. Where a form requires a tier, the accurate entry is:
<em>unable to determine from available historical source; requires direct assessment</em>. Determining
present risk needs a direct, current, qualified assessment — which this document is not and does not
replace.</p>
</div>
</div>

<div class="callout caution">
<span class="lab">What would warrant prompt or urgent help</span>
<p>If either kind of thought is <b>current, recurrent, compelling, escalating, or hard to leave
alone</b>, the appropriate step is a timely conversation with a qualified mental-health professional —
a university counselling service, a psychologist or a psychiatrist. If there is <b>current intent, a
plan, a preparation, access to means, an identifiable target, or an inability to stay safe</b>, that
warrants immediate real-world support: local emergency or crisis services, and a trusted person who
can be physically present. This report is not treatment, not a crisis service, and not a substitute
for either. Nothing here should be read as establishing that such support is, or is not, needed.</p>
</div>
""",
],
}
