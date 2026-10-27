from figures import fig_plan
"""Chapters 9-12 of the report. Condensed to the page budget."""



def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


# ---------------------------------------------------------------- predictions
_PREDS = [
dict(sit="A prolonged academic or technical problem that resists solution",
resp="Keeps working past the point of diminishing return, then reads the difficulty as evidence about himself rather than about the problem.",
why="His requests consistently aim at completeness and full mechanism; the thoroughness that produces good artefacts will not switch off on its own.",
alt="Ordinary persistence in a demanding field. Engineering problems are supposed to be hard, and long effort is what competence looks like from inside.",
conf="moderate",
imp="Time-box the session before starting, and write down what is now known that was not known at the start."),
dict(sit="A deadline arriving with information still incomplete",
resp="Gathers more before producing anything, and the gathering is genuinely useful, which is what makes it hard to interrupt.",
why="Every documented request is specification-first: complete syllabus coverage, complete test sets, exact layouts.",
alt="Rational risk management. Submitting incomplete work is sometimes worse than submitting late, and he may be making a correct judgement about stakes.",
conf="moderate",
imp="Decide the minimum viable version at the start, in writing, and treat everything added after that as optional."),
dict(sit="A disappointing result after substantial effort",
resp="Treats the result as information about his worth rather than about the method, and responds with self-criticism rather than method revision.",
why="Contingent self-worth tied to achievement and contribution is visible across the record, and the self-punitive rule he described has the same structure.",
alt="Normal disappointment. A bad result is genuinely unpleasant, and a period of frustration is not a personality pattern.",
conf="moderate",
imp="Write two lists after a setback: what the result says about the approach, and what it says about him. The second is usually empty."),
dict(sit="Criticism from someone he respects",
resp="Takes it seriously, examines it thoroughly, and may over-extend it — treating one specific criticism as a general verdict.",
why="He has asked for unsoftened feedback and said he prefers being challenged when defending a position already shown wrong. Criticism therefore lands without a buffer.",
alt="Accurate self-assessment. If the criticism is correct, taking it seriously is the right response and the discomfort is proportionate.",
conf="moderate",
imp="Convert the criticism into one concrete change and stop there. The specific change is the whole of the feedback."),
dict(sit="A disagreement with a teammate about contribution or standards",
resp="Raises it indirectly or not at all, discusses it with friends, and carries the irritation. Fairness concerns may intensify in private.",
why="He describes satisfying competing sides rather than escalating, and in the one documented case the disagreement went to friends rather than to the teammate.",
alt="Situational judgement. In a hostel or group project he may have limited standing to raise it, and waiting for a better moment is legitimate.",
conf="moderate",
imp="One sentence, once, about the work: <em>I need the section by Thursday or I'll do it myself.</em> No character judgement, no apology."),
dict(sit="Perceived unfair treatment by an institution or a person with power",
resp="Strong moral reaction, private intensity, limited direct challenge, and prolonged rumination afterwards.",
why="He describes intense reactions to hypocrisy and injustice alongside a non-confrontational social style. The combination predicts high internal activation with low external expression.",
alt="Accurate perception and realistic caution. Institutions frequently are unfair, and challenging them carries real costs a student is right to weigh.",
conf="moderate",
imp="Separate what is factually wrong, what can be changed by something available to him, and what cannot. Act on the middle category only."),
dict(sit="Envy or unfavourable social comparison",
resp="Notices it, treats it as a character defect to be eliminated, and adds it to the self-assessment.",
why="He has named envy and resentment as things he wants to reduce, which means he notices them. Naming a normal emotion as a defect tends to intensify it.",
alt="Legitimate dissatisfaction. Comparison is sometimes accurate and points at something genuinely worth pursuing.",
conf="moderate",
imp="Ask what the envy points at, then act on that thing for one week. If it is about a real goal it will persist and become useful."),
dict(sit="A routine that must be maintained without immediate reward",
resp="Starts well, loses it after a demanding stretch, and reads the loss as a failure of character.",
why="He has described difficulty sustaining a boxing routine after evening classes, and consistency as a stated goal. The pattern is specific to low-feedback routines — certifications were completed.",
alt="Ordinary capacity limits. A demanding engineering term with classes into the evening leaves little room, and dropping a routine may be correct prioritisation.",
conf="moderate",
imp="Set the minimum at a level that survives the worst week — ten minutes, not an hour — and define the missed-day rule in advance."),
dict(sit="A sexist joke or sexualised comment from friends",
resp="Discomfort, likely silence or a mild deflection, and later self-criticism for not having objected more firmly.",
why="In the one documented case he did object to degrading language, and he also participated in an adjacent intrusion. Both are recorded, so the response is genuinely uncertain.",
alt="Situational calculation. Objecting to a peer group carries social cost, and choosing not to fight every instance is a reasonable allocation of social capital.",
conf="moderate",
imp="Have one sentence ready and use it once: <em>not my business, let's talk about the work.</em> A rehearsed line requires no courage in the moment."),
dict(sit="Criticism of, or visible incompetence in, someone he has idealised",
resp="Discomfort and possible defensiveness; the idealisation may be defended rather than revised.",
why="He has identified pedestalisation as a pattern in himself, and idealisation is typically maintained because it carries meaning rather than because evidence supports it.",
alt="Loyalty. Defending someone he respects against unfair criticism is a virtue. The distinction is whether the evidence is weighed or dismissed.",
conf="low",
imp="Notice the specific moment the discomfort appears and ask what evidence would change the assessment. If none exists, the belief is not about the person."),
dict(sit="Emotionally provocative political or social content about injustice",
resp="Anger or collective guilt, rumination, tears or overwhelm, reduced concentration, and further consumption.",
why="He reports exactly this sequence: outrage content increasing his anger, sometimes leaving him crying or unable to concentrate, in a period when social-media use was the main trigger window.",
alt="Appropriate moral response. Some content deserves anger, and a person who feels nothing about injustice is not better adjusted. The cost is the displacement of focus, not the feeling.",
conf="high",
imp="Cap exposure by time, not by topic — a fixed window, then stop, regardless of how justified the anger is."),
dict(sit="An unwanted thought, followed by a decision about what to do with it",
resp="Monitors it, assigns it meaning about character, tries to suppress or atone for it, and the monitoring itself keeps it active.",
why="He has described intense guilt about a fleeting attention-related reaction, monitoring his own gaze, and a strict rule against attraction outside a future partner — the mechanics of thought-control rather than acceptance.",
alt="Ordinary conscience. Noticing that a thought is unwelcome and deciding not to act on it is healthy. The line is whether the thought is examined and released or examined and retained.",
conf="moderate",
imp="Treat the thought as a passing event with no evidential value about character, and judge only the action taken."),
dict(sit="Encountering a leader, cause or ideology promising total purpose or moral certainty",
resp="Strong pull, particularly when the narrative supplies clarity and belonging that ordinary life does not, with limited critical distance in the moment.",
why="He identifies with characters built around purpose, sacrifice and vengeance, has said he can imagine sacrificing himself for a charismatic leader, and has asked why a single leader or framework seems attractive to him.",
alt="Ordinary narrative engagement. Admiring fictional characters is not adopting an ideology, and the pull may be aesthetic rather than motivational.",
conf="moderate",
imp="Test the narrative by asking what it requires of him concretely this week. If the answer is that it requires surrendering his own judgement, slow down."),
dict(sit="Being unable to meet a study target, or unable to enjoy leisure without producing something",
resp="Guilt, restitution through more study, and reduced capacity to rest — which makes the next target harder to hit.",
why="He has described planning study tasks automatically during holidays and difficulty switching into a relaxed mode, and lists consistency as a goal rather than a possession. Rest appears to be treated as a debt.",
alt="High conscientiousness in a competitive programme. Engineering in India is demanding, and sustained effort during a term is proportionate rather than compulsive.",
conf="moderate",
imp="Schedule one block per week whose only rule is that nothing productive happens in it. If it produces guilt, the guilt is the finding."),
]

_PLAN = [
dict(name="Ship before you are ready, on a fixed weekly cadence",
behaviour="Each week, take one piece of work that has been prepared or refined and finish it at a quality he would call acceptable rather than ideal. Submit, publish or show it. The purpose is to build a stopping rule, not to lower standards.",
cells=["One deliverable finished and released per week, whatever its size",
"A dated list of finished items, one per week",
"If a week is missed, the next ships two — no restart, no penalty beyond the count",
"Ten minutes: what shipped, what the stopping rule was, what the next one is",
"Four consecutive weeks in which something was released rather than retained"]),
dict(name="One ordinary interaction a day, and no review afterwards",
behaviour="Have one unremarkable conversation with someone he would currently be careful around — a female classmate, a senior, a stranger. Ask a normal question. Disagree once if he disagrees. Then stop thinking about it, deliberately and by rule.",
cells=["One interaction per day; two minutes is enough",
"A tally per day, noting only whether he reviewed it afterwards",
"Missing a day is neutral; three in a row triggers one low-stakes interaction",
"Five minutes: how many days, how many reviews, what they were about",
"He can describe a conversation without replaying it, and stiffness has not increased"]),
dict(name="Bounded moral exposure, followed by regulation or repair",
behaviour="When he encounters injustice content, cap the exposure at a fixed time window, then either take one concrete constructive action within his reach or do something that settles his body. No further consumption on the same topic that day.",
cells=["Fixed 20-minute window; one action or one settling activity afterwards",
"Number of days the cap held; number of times exposure continued past it",
"A broken cap is recorded and does not reset the plan; the next day starts fresh",
"Ten minutes: which topics triggered flooding, and what ended it",
"Flooding episodes become shorter and less frequent, and moral concern still produces action"]),
]


def _pred_html(p, idx):

    """Compact table row: one prediction per row keeps all fourteen readable at
    a fraction of the height of an expanded block."""
    cls = {"high": "hi", "moderate": "md", "low": "lo"}[p["conf"]]
    return (f'<tr><td class="k" style="width:5%">{idx:02d}</td>'
    f'<td style="width:24%"><b>{p["sit"]}</b></td>'
    f'<td style="width:31%">{p["resp"]}</td>'
    f'<td style="width:26%;color:var(--charcoal-2)">{p["alt"]}</td>'
    f'<td style="width:14%">{p["imp"]}<br/><span class="conf {cls}">{p["conf"]}</span></td></tr>')


def _pred_table(preds):

    rows = "".join(_pred_html(p, i + 1) for i, p in enumerate(preds))
    return f"""<table>
    <caption>Fourteen conditional projections, with the alternative that fits the same evidence</caption>
    <thead><tr><th>#</th><th>Situation</th><th>Possible response, and why</th>
    <th>Alternative explanation</th><th>Implication · confidence</th></tr></thead>
    <tbody>{rows}</tbody></table>"""


# ============================================================ CHAPTER 9
CH10 = {
"id": "ch10", "num": "10", "kicker": "Projections",
"title": "Conditional Behavioural Predictions",
"sub": "Fourteen situations, each with its reasoning, its alternative and its confidence",
"pages": [
f"""
<p class="lede">These are conditional projections, not forecasts. Each states what the evidence
makes likely, what else would explain the same thing, how much confidence the record supports, and
what follows practically.</p>


{_pred_table(_PREDS)}
""",
],
}


# ============================================================ CHAPTER 10
CH11 = {
"id": "ch11", "num": "11", "kicker": "Development",
"title": "Development Plan",
"sub": "Three priorities, thirty days, observable indicators, and no requirement for anyone else's cooperation",
"pages": [
f"""
<p class="lede">Three priorities, chosen because the evidence for each is strong, each is within
his own control, and each is measurable without an app, a purchase or another person's agreement.</p>

<p>They are deliberately few. A plan that addresses every tension in Chapter 9 would be a plan that
gets abandoned in a week, and abandonment would add one more item to the self-assessment. The target
is a reliable minimum that survives a bad week.</p>

<figure>
{fig_plan(_PLAN, 520)}
<figcaption><b>Figure 8. The 30-day plan.</b> Each priority states one behaviour, a minimum action,
an indicator, a missed-day rule, a weekly review and a definition of progress. The missed-day rule
is the load-bearing element: a plan without one converts a single missed day into a reason to stop,
which is the most common way self-improvement plans fail.</figcaption>
</figure>

<h2 class="sec"><span class="sn">11.1</span>Why these three</h2>

<div class="grid3">
<div class="card teal">
<h4>Priority 1: shipping</h4>
<p class="body">Chosen because the preparation–execution gap is the most consistently evidenced
pattern in the technical material, and the one that most directly affects the outcomes he says he
wants. It also attacks the mechanism behind his self-criticism: work that never ships cannot
disprove the doubt.</p>
</div>
<div class="card">
<h4>Priority 2: ordinary contact</h4>
<p class="body">Chosen because the stiffness pattern is specific, documented, self-limiting in one
recorded instance, and trainable. It addresses the social material and the gender material with the
same behaviour, because both are the same error — processing a person through a category instead of
meeting them.</p>
</div>
<div class="card amber">
<h4>Priority 3: bounded exposure</h4>
<p class="body">Chosen because flooding is the most strongly evidenced emotional pattern and the
easiest to interrupt. It is a regulation target, not a moral one: the aim is to keep the concern
while removing the overwhelm that currently consumes the capacity it would use.</p>
</div>
</div>

<div class="callout caution">
<span class="lab">What this plan deliberately does not do</span>
<p>It does not ask him to abandon the rule about attraction, to start dating, to change his political
views, or to stop reading about injustice. It does not prescribe an exposure protocol for intrusive
thoughts, because that is a clinical intervention and this is not a clinical document. It does not
require him to disclose anything to anyone. And it does not attempt to address the self-hatred
directly, because self-hatred responds to behaviour over time rather than to a thirty-day exercise —
the three priorities work on it indirectly by giving him evidence of ordinary competence and ordinary
contact.</p>
</div>
""",
],
}


# ============================================================ CHAPTER 11
_QS = [
("Are the most distressing experiences — self-hatred, guilt, self-punishment — present now, and how often?",
"Every emotional conclusion in this report is conditional on this. The difference between a past phase and a current daily experience changes the assessment more than any other single fact."),
("Are the images of revenge, chaos or self-sacrifice current, and do they arrive unbidden or only when deliberately considered?",
"This separates remembered or deliberately imagined material from intrusive, hard-to-dismiss material. The two have very different implications, and the transcript does not distinguish them."),
("Does the social stiffness stop him doing anything — asking a question, disagreeing with a senior, speaking in a group?",
"The difference between an uncomfortable moment and a functional limit decides whether this is a skill to practise or a problem to address properly. The record contains no functional-impairment information at all."),
("Is the strict rule about attraction experienced as a freely chosen value or as something he must enforce?",
"A chosen boundary is restful; an enforced one requires vigilance and tends to produce the intrusive thoughts it was meant to prevent. The two are indistinguishable from outside and obvious from inside."),
("What concrete behaviour has changed in the last six months?",
"Intentions are well documented and behaviour is not. This question converts aspiration into evidence and would settle several tensions in Chapter 8 at once."),
("How much of the day is actually spent on study, projects and classes, and how much on social media?",
"His own account puts most of the day on work with a smaller social-media window, but the account is retrospective. The actual distribution decides whether the attention environment is a major driver or a minor one."),
("How did the Class 11 drop from 88% to 69% happen, and what changed between Class 11 and Class 12?",
"This is the clearest documented downturn in the record, and its cause would test the attribution he makes to a difficult school period."),
("Have the recorded projects been completed, maintained, or abandoned?",
"Repositories exist; their state is unknown. This decides whether the technical strengths in Chapter 8 are matched by sustained follow-through, which is the weakest layer of the record."),
("How do other people experience him — as warm, reserved, intense, distant?",
"There is not a single observer account in the source material. Observer ratings add information self-report systematically cannot, and would test the agreeableness and extraversion estimates directly."),
("What happened after the teammate disagreement, and what did he actually say to her?",
"This is the one documented values-and-conduct gap. What he did next is the only available evidence about whether the recognition he reports has produced a behavioural change."),
]

CH12 = {
"id": "ch12", "num": "12", "kicker": "Uncertainty",
"title": "What Remains Unknown",
"sub": "Ten questions that would materially change this assessment, and why each one matters",
"pages": [
f"""
<p class="lede">These are not gaps in effort. They are the specific pieces of information the
available material cannot supply and that would change the conclusions rather than merely add detail.</p>

<table>
<caption>The ten questions, with the uncertainty each would resolve</caption>
<thead><tr><th style="width:5%">#</th><th style="width:42%">Question</th><th>What it would resolve</th></tr></thead>
<tbody>
{''.join(f'<tr><td class="k">{i+1}</td><td class="k">{q}</td><td>{w}</td></tr>' for i, (q, w) in enumerate(_QS))}
</tbody>
</table>

<div class="callout caution">
<span class="lab">What is not unknown, and should not be treated as such</span>
<p>Some things are clear and are not in question. He is a capable student with dated, verifiable
achievements. He is genuinely interested in technical work. He holds himself to high standards. He is
willing to revise his views. He is trying to become a better and more dependable person, and he has
thought about what that requires more carefully than most people his age. Those conclusions do not
depend on any of the ten questions above.</p>
</div>
""",
],
}


# ============================================================ CHAPTER 12
CH13 = {
"id": "ch13", "num": "13", "kicker": "Synthesis",
"title": "Final Synthesis",
"sub": "What the evidence supports, what deserves attention, and what should not be concluded",
"pages": [
"""
<p class="lede">The evidence describes a capable, morally serious, self-critical young man whose
principal difficulty is not a deficiency of ability or values but a method: he converts ordinary,
imperfect, bounded action into an unanswerable question about his own worth, and then works on the
question.</p>

<h2 class="sec first"><span class="sn">13.1</span>What kind of person the evidence suggests</h2>

<p>The most defensible single sentence is this. Rishabh appears to be a high-openness,
high-standards, emotionally reactive young man in the middle of forming an identity, who has
unusually good insight into his own patterns and an unusually severe system for judging them, and
whose main practical problem is that the judging consumes the capacity the acting would use.</p>


<p>The emotional material is different in kind. It is extensive, articulate and self-generated, and
it is entirely uncorroborated. It establishes what he reported and believed about himself during a
long conversation in which he was asked directly about these things. It does not establish frequency,
severity, persistence or current status, and it cannot establish his safety now. Both kinds of
material belong in the same report, and they should not be given the same weight.</p>

<h2 class="sec"><span class="sn">13.2</span>Strengths worth building on</h2>

<div class="grid2">
<div class="card teal"><h4>Cross-domain learning</h4><p class="body">He moves between algorithm
theory, embedded hardware, database integration, hydrological simulation and moral philosophy without
losing rigour in any of them. This is the rarest and most durable asset in the record, and the one
least dependent on anything he needs to fix.</p></div>
<div class="card teal"><h4>Willingness to revise</h4><p class="body">He examined and partly
dismantled an identity he had adopted, then questioned the frame it came from. Most people never do
this once. It means he is likely to accept a finding in this report that he does not like, provided
the reasoning is visible.</p></div>
<div class="card teal"><h4>Insight</h4><p class="body">Identity by negation, pedestalisation, the
avoidance function of diagnosis-seeking, self-punishment that repairs nothing — he identified all
four himself. Insight is not the same as change, but it is the precondition for it and it is not
teachable.</p></div>
<div class="card teal"><h4>Moral seriousness</h4><p class="body">He wants to be someone women feel
safe around, he objected to degrading talk about a classmate, and he takes harm done by people like
him seriously. The failure mode of this trait is overreach, and overreach is easier to correct than
indifference.</p></div>
</div>

<h2 class="sec"><span class="sn">13.3</span>Liabilities that deserve attention</h2>

<p>Four, in order of how much they affect the outcomes he says he wants.</p>

<ul class="tick">
<li><b>Preparation outrunning execution.</b> The most consistently evidenced pattern in the technical
material, and the one most likely to limit his career if it persists. A person who gathers brilliantly
and ships rarely is outperformed by a person who gathers adequately and ships reliably.</li>
<li><b>Self-worth contingent on output, contribution and moral difference.</b> This is what makes rest
feel like failure, ordinary mistakes feel like verdicts, and comparison feel unbearable. It is also the
mechanism that turns his strengths into sources of pressure.</li>
<li><b>Distress that displaces action.</b> Collective self-blame, outrage-driven overwhelm and
imagined revenge all consume the capacity that constructive response would use. His moral concern is
real; the channel is inefficient.</li>
<li><b>Harmony preferred over clarity.</b> Unraised disagreements accumulate as resentment, and an
identity built partly on what he refuses to be has no positive content to fall back on when the
refusal loses force.</li>
</ul>
""",
"""
<h2 class="sec"><span class="sn">13.5</span>What should change, and how</h2>

<p>The developmental changes worth pursuing are behavioural rather than self-descriptive, and there
are three of them. Ship one thing a week at a quality he considers acceptable rather than ideal. Have
one ordinary interaction a day with someone he would currently be careful around, and do not review it
afterwards. Cap exposure to outrage content by time and follow it with either a concrete action or a
settling activity, not with more content.</p>

<p>What all three share is that they convert an internal question into an external act, and an
external act is the only thing that produces evidence. His self-assessment is currently built almost
entirely from inference and memory. It has very little data in it. Three small repeated behaviours,
recorded for a month, would supply more usable information about who he is than another year of
examining the question.</p>

<div class="pull">The problem is not that he thinks too much. It is that he is trying to think his way
to evidence that only acting can produce.</div>

<p>One further point belongs here, because it is the one place where a change of method matters more
than any behaviour on a list. He has asked for unsoftened feedback, so this is offered plainly. His
self-punitive rule is not accountability, and the record shows he has begun to see that. What is
missing is its replacement. The mechanism that lets a person stay in contact with their own failures
long enough to learn from them — rather than avoiding the subject or attacking themselves over it — is
self-compassion, and it is the one strategy conspicuously absent from everything he has said he wants.
It is not softness, it is not excuse-making, and it is not a lowering of standards. It is the thing
that makes standards survivable, and without it the standards he has will keep producing the
exhaustion they currently produce.</p>
""",
],
}
