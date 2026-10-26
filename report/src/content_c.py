"""Chapters 6-8 of the report. Condensed to the page budget."""
from figures import fig_strengths, fig_values


def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


# ============================================================ CHAPTER 6
CH6 = {
"id": "ch6", "num": "6", "kicker": "Interpersonal",
"title": "Diplomacy, Empathy and Relationships",
"sub": "Where his stated values hold, where they have slipped, and what cannot be seen from here",
"pages": [
f"""
<p class="lede">This chapter deals with the material most likely to be either softened or
weaponised. Both would be failures. The record contains genuine moral seriousness and a concrete
instance of conduct that contradicted it, and the analysis has to hold both.</p>

<div class="callout caution">
<span class="lab">Anonymity and scope</span>
<p>No classmate, relative or third party is named in this report. The incidents discussed are
described in terms of roles and behaviour only. Nothing here should be read as a claim about any
other person's conduct, character or relationships, and no allegation recorded in the source is
treated as established fact.</p>
</div>


<h2 class="sec"><span class="sn">6.1</span>The one documented values-and-conduct gap</h2>

<p>This is the most concrete evidence in the whole assessment about how his values behave under
social pressure, and it deserves to be stated plainly and without embellishment.</p>

<p>He believed a female teammate was not completing her share of the work. He was frustrated about
contribution and accountability — a legitimate concern. He discussed it with male friends. One of
them used sexualised, degrading language about her and made claims about her relationships.
<b>Rishabh objected to that language.</b> He also admits that in the same episode he asked whether
the classmate was a virgin, and later recognised that as an unfair intrusion into a person's private
life. He reports that peers in this environment routinely mocked female classmates' character or
motives rather than limiting criticism to their work.</p>

<table>
<caption>What this episode does and does not establish</caption>
<thead><tr><th style="width:46%">It shows</th><th>It does not show</th></tr></thead>
<tbody>
<tr><td>His values were active: he objected to the degrading language rather than joining it silently</td><td>That his objection was consistent — he participated in an adjacent intrusion himself</td></tr>
<tr><td>He can recognise his own inconsistency afterwards, which is not universal at any age</td><td>That the recognition has changed the behaviour, since no later instance is recorded</td></tr>
<tr><td>A real distinction he already grasps: work contribution can be criticised without judging a person's sexuality or worth</td><td>That he applied the distinction in the moment, under peer pressure</td></tr>
<tr><td>The peer environment appears to normalise sexualised talk about classmates</td><td>Anything about the classmate's conduct, character or relationships</td></tr>
</tbody>
</table>

<div class="callout">
<span class="lab">The useful lesson, stated without moralising</span>
<p>Two separate things were happening and they are worth keeping apart. One was a legitimate
disagreement about work, which was his to raise. The other was a collective turn toward judging a
person's private life, which was not. He saw the second clearly enough to object, and then entered
it himself with a single question. That is what conformity pressure does: it rarely converts a
person wholesale, it produces one specific slip in an otherwise considered position. The behaviour
to build is not shame about the slip. It is a rehearsed, low-cost line for the moment —
<em>I don't want to talk about her personal life, let's sort the work</em> — said once, without a
lecture, and then dropped.</p>
</div>
""",
f"""
<h2 class="sec"><span class="sn">6.2</span>Objectification, pedestalisation and the wish for ordinariness</h2>

<p>He has described wanting women to feel safe and comfortable around him, and not wanting to
objectify them. He has also described seeing women as especially vulnerable or morally better than
men, wanting to protect them, and fearing that treating women with the same ordinary familiarity he
has with male peers might lead him to criticise them harshly or become misogynistic. He has named
<em>pedestalisation</em> himself as a real problem, and has said he wants to treat women as complete
individuals rather than as symbols of purity, vulnerability, moral redemption or danger.</p>

<p>That last formulation is worth pausing on, because it is the most psychologically sophisticated
thing in the gender-related material. Recognising that idealisation and objectification are two
versions of the same error — treating a person as a category rather than as a person — is a
distinction that takes many adults decades to reach, and it appears in his own account rather than
being supplied to him.</p>

<div class="grid2">
<div class="card amber">
<h4>Objectification</h4>
<p class="body">Treating a person as a body, an instrument, or a source of gratification. Reduces
them below the ordinary. Predicts intrusive sexualised speculation and boundary-crossing curiosity
about private life.</p>
</div>
<div class="card amber">
<h4>Pedestalisation</h4>
<p class="body">Treating a person as a symbol — purer, more fragile, more moral. Raises them above
the ordinary. Predicts deference, formality, protective impulses, and difficulty disagreeing with
them.</p>
</div>
</div>

<p>The record contains evidence of both, and the second is better supported. The intrusive question
in the teammate episode is the first. The reported stiffness, over-formality, protective framing and
stated fear of criticising women are the second. Both have the same root: the person in front of him
is being processed through a category before being met as an individual. Objectification makes them
less than a person; pedestalisation makes them something other than a person. Neither allows the
ordinary, unremarkable, slightly friction-ful interaction that he says he wants.</p>

<div class="pull">The goal is not to think better of women. It is to think about them less and
notice them more.</div>

<h3 class="sub">6.5 · Two further statements that need careful handling</h3>

<p>He has discussed dowry and a hypothetical future spouse partly in terms of whether she would work
and contribute financially to the household, and described himself as an "asset" too, with social
and household worth depending on contribution. This may reflect a moment of reasoning inside a
cultural frame, an unresolved belief, or a settled view — the source does not establish which, and
it does not establish that it is his current position. What can be said is that a framework in which
worth equals contribution is a difficult foundation for a relationship, and it is the same framework
that drives his own self-criticism. The two are worth noticing together: the standard he applies to
a hypothetical partner is the standard he applies to himself, and it produces the same result in
both cases.</p>

<p>He has also stated a strict personal rule against romantic or sexual attraction except toward a
future life partner, and asked that advice respect it. That request is respected here. The report
does not recommend dating, does not pathologise celibacy or the decision not to date, and does not
prescribe any romantic or sexual identity. It is worth noting only that a rule of this kind can be
experienced as a freely chosen value or as a fear-based suppression, and the two feel very different
from inside. A chosen boundary is restful and needs no enforcement; a fear-based one requires
constant vigilance, which is itself exhausting and tends to produce the intrusive thoughts it was
meant to prevent.</p>
""",
f"""
<h2 class="sec"><span class="sn">6.3</span>Social stiffness: what it is and what it is not</h2>

<p>He reports breaking eye contact quickly when speaking face-to-face with women, shoulders locking
or the body becoming stiff, and being unusually careful or formal. He says the same can occur around
accomplished or high-status seniors, that he is comfortable with his parents, and that the stiffness
is not universal. He records one counterexample: a small sense of pride after a conversation with a
woman that he felt he had handled more comfortably than before.</p>

<p>The pattern's shape — present with women <em>and</em> with high-status men, absent in familiar
settings, improving with exposure — argues against a broad trait explanation and for a situational
one. The most economical account is self-focused attention under perceived evaluation: attention
turns inward to monitor one's own performance, which consumes the capacity that would otherwise read
the other person, which makes the interaction feel awkward, which confirms the concern. The
self-focus model of social difficulty describes exactly this mechanism.</p>

<div class="callout plain">
<span class="lab">What cannot be inferred from here</span>
<p>The record contains no assessment of duration, frequency or functional impairment, and no observer
account of how others experience him. Stiffness in a first conversation with a stranger is ordinary.
Stiffness that prevents him from speaking up in a tutorial, asking a question in a lab, or
disagreeing with a senior would be a real cost. The dossier does not tell us which of those applies,
and no inference about a clinical condition can be drawn from a conversational transcript in either
direction.</p>
</div>

<p>Three interpretations are live and cannot be separated on this evidence. <b>Ordinary
unfamiliarity</b>: if he has had little casual conversation with women, awkwardness is a skill gap,
not a disposition. <b>Respectful caution</b>: a deliberate wish not to intrude or offend produces
careful, formal behaviour that looks like anxiety from outside. <b>Evaluation concern</b>: a genuine
fear of negative judgement, which is the only one of the three that would need addressing directly.
All three produce the same surface, and the intervention is different for each. The cheapest way to
tell them apart is behavioural: if the stiffness decreases with repeated ordinary contact, it was
unfamiliarity. If it persists unchanged across many exposures, it is evaluation concern.</p>
""",
],
}


# ============================================================ CHAPTER 7
_STR = [
dict(name="Curiosity", strength="rapid learning across unrelated domains",
shadow="exploration that outlives its purpose", evidence=3),
dict(name="Thoroughness", strength="work that is complete and reproducible",
shadow="gathering as a substitute for finishing", evidence=2),
dict(name="Ambition", strength="sustained effort toward real credentials",
shadow="achievement as the only permitted source of worth", evidence=3),
dict(name="Diplomacy", strength="low friction, strong relationships",
shadow="unspoken disagreement that returns as resentment", evidence=2),
dict(name="Moral sensitivity", strength="notices harm others overlook",
shadow="personal distress that displaces helpful action", evidence=3),
dict(name="Self-analysis", strength="unusual insight into own patterns",
shadow="rumination that changes nothing", evidence=3),
dict(name="Accountability", strength="willingness to own specific acts",
shadow="self-punishment presented as responsibility", evidence=3),
dict(name="Independence", strength="decides and acts without permission",
shadow="refusing help that would be faster", evidence=1),
dict(name="Empathy", strength="wants others safe and at ease",
shadow="pedestalisation that prevents ordinary contact", evidence=2),
dict(name="Purpose-seeking", strength="resistance to a pointless life",
shadow="surrendering judgement to a cause or leader", evidence=2),
dict(name="Analytical precision", strength="converts vague problems into defined ones",
shadow="demanding one cause where several operate", evidence=3),
dict(name="Productivity", strength="real, verifiable competence",
shadow="output as a precondition for self-acceptance", evidence=3),
]

CH7 = {
"id": "ch7", "num": "7", "kicker": "Capacities",
"title": "Strengths and Their Shadow Sides",
"sub": "Every entry below is one disposition with two outcomes, not a virtue beside a fault",
"pages": [
f"""
<p class="lede">A strength and its failure mode are usually the same trait under different
conditions. This chapter pairs them deliberately, because the useful question is not which column
he is in but what moves him between them.</p>

<figure>
{fig_strengths(_STR, 520)}
<figcaption><b>Figure 5. Strengths and their shadow sides.</b> Evidence squares indicate how much
support exists for the <em>left-hand</em> column, which is the better-evidenced side in every case.
Several right-hand entries are inferences from the pattern of his requests and self-descriptions
rather than from observed failures — they mark where to look, not where a defect is proven to
be.</figcaption>
</figure>

<h2 class="sec"><span class="sn">7.1</span>The strongest assets</h2>

<div class="grid2">
<div class="card teal">
<h4>Rapid cross-domain learning</h4>
<p class="body">Dated evidence: certifications passed first attempt, a hydrology simulation specified
with a real stack, a Swing application with its own architecture documents, and coursework across
data structures, databases, architecture and statistics. The breadth is real rather than claimed,
because the artefacts are specific.</p>
</div>
<div class="card teal">
<h4>Willingness to revise a settled position</h4>
<p class="body">He adopted a political identity in school and then examined it, criticised it, and
questioned the frame it came from. That is the hardest cognitive move available, and most people
never make it. It also predicts he will accept an uncomfortable finding in this report if the
reasoning is visible.</p>
</div>
<div class="card teal">
<h4>Insight into his own patterns</h4>
<p class="body">He identified identity-by-negation, pedestalisation, the avoidance function of
diagnosis-seeking, and the possibility that punishment was no longer useful — all without being
told. Most people described in psychological terms recognise the description; far fewer generate
it.</p>
</div>
<div class="card teal">
<h4>Moral seriousness</h4>
<p class="body">He objected to degrading talk about a classmate, wants to be someone women feel
safe around, and takes harm done by people like him seriously. The failure mode of this trait is
overreach, not indifference.</p>
</div>
</div>

<div class="keep">
<h2 class="sec"><span class="sn">7.2</span>The sharpest liabilities</h2>

<div class="grid2">
<div class="card amber">
<h4>Self-worth contingent on output and purity</h4>
<p class="body">The record shows worth tied to contribution, comparison with peers, and moral
difference from others. Contingent self-worth is fragile by construction: it makes rest feel like
failure and every ordinary mistake feel like evidence about the self.</p>
</div>
<div class="card amber">
<h4>Distress that displaces action</h4>
<p class="body">Collective self-blame, being left crying by outrage content, and imagined revenge all
consume the capacity that constructive response would use. The moral concern is real; the channel is
inefficient.</p>
</div>
<div class="card amber">
<h4>Analysis applied to unanswerable questions</h4>
<p class="body">The same engine that makes him good at systems runs on "what is wrong with me" and
"am I a good person," where no amount of specification produces an answer. It produces activity that
feels like progress.</p>
</div>
<div class="card amber">
<h4>Preference for harmony over clarity</h4>
<p class="body">The cost is invisible in the moment and visible later: unraised disagreements,
accumulating irritation, and an identity built partly on what he refuses to be rather than on what
he chooses.</p>
</div>
</div>
</div>


<div class="callout">
<span class="lab">What links all four</span>
<p>Each is a version of the same move: converting something that requires ordinary, imperfect action
into something that requires analysis, judgement or endurance. Working is imperfect action. Sitting
with a disagreement and saying one clear sentence is imperfect action. Making peace with a mediocre
output and shipping it is imperfect action. The strengths are not in tension with his goals; the
<em>method</em> is. He has been trying to solve by thinking and by standards problems that are solved
by moving.</p>
</div>
""",
],
}


# ============================================================ CHAPTER 8
_VAL = [
dict(value="Independence", note="consulted his sister on a major decision; reports wanting autonomy",
direction="mixed", evidence=2),
dict(value="Honesty and directness", note="requests unsoftened feedback; withholds disagreement socially",
direction="tension", evidence=2),
dict(value="Equality", note="objected to degrading talk; joined one intrusive question",
direction="mixed", evidence=2),
dict(value="Respect for boundaries", note="states the rule explicitly; describes monitoring his own gaze",
direction="leaning", evidence=2),
dict(value="Empathy", note="wants others at ease; distress centres on his own position",
direction="mixed", evidence=3),
dict(value="Consistency", note="certifications completed; states this as a goal still to reach",
direction="mixed", evidence=3),
dict(value="Accountability", note="owns specific acts; converts them into self-punishment",
direction="tension", evidence=3),
dict(value="Discipline", note="stoic aims; hard on himself; unverified sustained routines",
direction="mixed", evidence=2),
dict(value="Practicality", note="wants working deliverables and deployment paths",
direction="consistent", evidence=3),
dict(value="Curiosity", note="broad reading; walls off whole domains by rule",
direction="leaning", evidence=2),
dict(value="Fairness in relationships", note="framed contribution and household worth economically",
direction="tension", evidence=1),
dict(value="Self-compassion", note="no evidence of it anywhere in the record",
direction="untested", evidence=0),
]

CH8 = {
    "id": "ch8", "num": "8", "kicker": "Tensions",
    "title": "Contradictions and Blind Spots",
    "sub": "Fourteen tensions, the evidence on each side, and what would settle them",
    "pages": [
        f"""
<p class="lede">Inconsistency is not hypocrisy. It is what a person looks like while changing, and
the difference is decided by what happens next. Each entry below states the evidence for both
readings and names a test that would settle it.</p>

<figure>
{fig_values(_VAL, 520)}
<figcaption><b>Figure 6. Values against behavioural evidence.</b> Position on the horizontal axis
records how much <em>behavioural</em> evidence supports the stated value — not how sincere the value
is. A point left of centre means the record shows the value being overridden at least once, not that
it is false. The dashed row marks a value that is nowhere tested in the record. This is a reflection
aid, not a moral scorecard, and it is built only from his own reported conduct because no observer
accounts exist.</figcaption>
</figure>

<table class="tensions">
<caption>Fourteen tensions, each with its evidence and the observation that would settle it</caption>
<thead><tr><th style="width:23%">Tension</th><th style="width:44%">Evidence on both sides</th><th>How to test it</th></tr></thead><tbody>
<tr><td class="k">Aspiration versus repeated behaviour</td><td>He has listed emotional self-control, consistency, less envy, greater empathy, independence and dependable execution as things he wants to develop. The list is coherent and specific, and it is also a list of goals rather than achievements.</td><td>which item on that list has shown a measurable change in the last six months? If none, the list is aspiration; if one or two have, the others will follow the same method.</td></tr>
<tr><td class="k">Planning versus starting</td><td>Preparation is well evidenced and detailed. Beginning is less visible. He has described planning study tasks automatically during holidays and struggling to sustain a routine after evening classes.</td><td>pick one prepared topic and check whether the studying actually began within a week of the material being ready. This is the single most informative test in the report.</td></tr>
<tr><td class="k">High standards versus timely completion</td><td>He demands completeness, and he dislikes unnecessary length. Those pull against each other, and the record shows the first more strongly than the second.</td><td>is there any finished deliverable he considers below standard? If everything he has submitted was submitted at the quality he wanted, the standards are calibrated. If some work went unfinished rather than imperfect, they are not.</td></tr>
<tr><td class="k">Emotional control versus emotional suppression</td><td>He wants Stoic composure. The record contains both the discriminating version — separating genuine injustice from unproductive dwelling — and the concealing version, in a diplomatic style that avoids displaying frustration.</td><td>can he describe an upset to another person while it is happening? Regulation permits this; suppression does not.</td></tr>
<tr><td class="k">Diplomacy versus direct boundary-setting</td><td>He prefers to satisfy competing sides. In the teammate case, the disagreement went to friends rather than to the teammate.</td><td>after a disagreement, was anything said to the person concerned? If not, the harmony was purchased with unexpressed irritation.</td></tr>
<tr><td class="k">Independence versus reassurance-seeking</td><td>He wants to be more independent, consults his sister on major decisions, and has had a very long conversation in which he repeatedly asked for a definitive explanation of himself. Those are compatible — consultation is not dependence, and asking questions is not weakness — but they are in tension, and the direction of travel is what matters.</td><td>what decision has he made in the last month without checking it with anyone, including an AI?</td></tr>
<tr><td class="k">Equality as belief versus sexualised judgement in specific statements</td><td>He objected to degrading language about a classmate and then asked her an intrusive question about her private life. He has stated egalitarian aims and discussed a future spouse partly in terms of financial contribution.</td><td>this is the clearest peer-pressure effect in the record. It is settled not by reflection but by one rehearsed sentence he can use the next time the conversation turns that way. What he does on that occasion is the evidence.</td></tr>
<tr><td class="k">Respect for women versus idealising them as better or more fragile</td><td>He wants women to feel safe and to be treated as equals, and he also sees them as more vulnerable and more moral, wants to protect them, and fears that ordinary familiarity would make him harsh. He has named this himself.</td><td>can he disagree with a woman as easily as with a man? If disagreement feels riskier, the pedestal is operational, and it is a form of distance rather than respect.</td></tr>
<tr><td class="k">Fear of objectification versus hyper-monitoring ordinary attention</td><td>He reports a brief attention-related reaction toward a person he believed to be underage while travelling, looking away within seconds, and then intense guilt and self-disgust. No approach, contact or action is described. He also reports monitoring his own gaze. The intrusive-thought literature is relevant and reassuring here: unwanted intrusive thoughts, including sexual and aggressive ones, are close to universal in non-clinical populations and are not by themselves meaningful about character. What distinguishes a problem is the meaning assigned to the thought and the effort spent controlling it.</td><td>is the guilt proportionate to anything he did? If the answer is no, the monitoring is the problem, not the thought.</td></tr>
<tr><td class="k">Compassion for victims versus responsibility for a group's wrongdoing</td><td>He blames himself for harm committed by people who share his gender or nationality. This converts a finite responsibility into an infinite one.</td><td>what specific act of his own is he answering for? If none, the guilt is about identity, and identity guilt cannot be discharged by any amount of self-punishment.</td></tr>
<tr><td class="k">Anger at injustice versus revenge and chaos imagery under overload</td><td>He reports strong reactions to real injustice and, historically, imagined revenge, chaos and severe violence, alongside imagined self-sacrifice for a cause. These are reported as thoughts.</td><td>are these images present now, and are they connected to anything he might do? If they are frequent, intrusive or hard to leave alone, that is a reason to speak with a professional rather than to keep examining them in writing. If they are occasional and clearly not action-linked, they say more about how he organises meaning than about risk.</td></tr>
<tr><td class="k">Dependability versus self-punishment as proof of goodness</td><td>He wants to be someone who does what he says. He has also described a rule of mentally punishing himself at least as much as anyone he has harmed, connected to wanting to be morally different from people who justify harm. That rule produces suffering rather than dependability, and it settles the account internally while leaving the affected person untouched.</td><td>does the punishment produce a changed action, or only relief? If only relief, it is functioning as a substitute for repair.</td></tr>
<tr><td class="k">Admiration for fictional sacrifice versus independent agency</td><td>He has referenced Dune 's Paul Atreides and the Fremen, and characters associated with self-hatred, vengeance or extreme purpose, and has said he can imagine sacrificing himself for a charismatic leader or a greater cause — while continuing to value his technical education and career. Narrative identification of this kind is common and often serves a function: it supplies purpose, certainty and moral clarity that ordinary life does not.</td><td>what would he have to give up to follow that narrative? If the answer is his own judgement, the appeal is worth watching closely. If the answer is nothing concrete, it is aesthetic rather than motivational.</td></tr>
<tr><td class="k">Wanting to stop self-analysing versus repeatedly requesting self-classification</td><td>He says he wants to reduce over-analysis and self-hatred, and he has asked repeatedly for a label, a root cause, a numerical prediction and a mathematical model of his own responses. He has also noticed that a label can function as avoidance.</td><td>notice what happens in the moment after receiving a definitive explanation. If the effect is relief that fades and returns as a new question, the search is the problem rather than the solution.</td></tr>
</tbody></table>
"""
    ],
}
