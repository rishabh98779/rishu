"""Chapters 1-2, written to the page budget.

Evidence tags: DIRECT (dated record), ARTEFACT (independently existing object),
SELF (first-person report), INFER (analyst reading), HYPOTH (testable possibility).
"""
from figures import fig_bigfive, fig_confidence


def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


CH1 = {
"id": "ch1", "num": "1", "kicker": "Overall portrait",
"title": "The Architecture of a Person",
"sub": "What the evidence supports, what it merely suggests, and where it stops",
"pages": [
f"""
<p class="lede">Rishabh Singh is an eighteen-year-old computer-science undergraduate whose record
shows two things running in parallel: a disciplined, technically ambitious student who wants finished
work and measurable competence, and a young man conducting a long, exhausting audit of his own moral
worth. The first is well evidenced. The second is evidenced mainly through his own account of it.</p>

<p class="dropcap">The dossier is not a biography. It is retained facts, dated academic and project
history, and summaries of conversations, supplemented by {_ev("SELF", "a long exported transcript of a previous dialogue")}
that he framed as an exploration of what he called internal liberation. Almost everything emotionally
significant here comes from that second source, so it arrives as self-report rather than observation.
Nothing has been corroborated by anyone else, and no instrument was administered. Those are not caveats appended to the analysis; they are the conditions it works
inside.</p>

<p>What the record supports is a specific configuration, not a generic one: genuinely high intellectual
curiosity and genuinely high standards for his own output, coupled with a self-evaluative system that
is unusually severe and unusually permeable to moral content. He wants to be excellent and he wants to be good, and he treats both as questions of personal
adequacy rather than as activities that can be practised.</p>

<h2 class="sec first"><span class="sn">1.1</span>The strongest recurring characteristics</h2>

<p>Four patterns repeat across otherwise unrelated material — academic requests, project work, health
and routine reports, and the emotional disclosures — which is what makes them credible as characteristics rather than moods.</p>

<ul class="tick">
<li><b>Completeness that shows up as specification.</b> His requests are unusually precise: divide
questions by mark value, cover the whole syllabus, do not omit Probability and Statistics, keep the
supplied institutional layout, do not rewrite what already works.
{_ev("SELF", "His own requirements, stated repeatedly across subjects.")}</li>
<li><b>Preference for structure over ambiguity.</b> Recursion trees, dry runs, visual representations,
clear divisions. He used one hashing document as the visual benchmark for everything that followed.</li>
<li><b>Discomfort with wasted effort.</b> He dislikes long, slow explanations, prefers IntelliJ IDEA to
VS Code, wants minimal targeted edits when debugging, and asks for tools that do the work rather than
advice about how to do it.</li>
<li><b>A moralised relationship with his own conduct.</b> Self-hatred beginning in childhood, a later
phase in which it became a settled belief that he had no redeeming qualities, a self-punitive rule that
he should mentally punish himself at least as much as anyone he had harmed, and an explicit wish to be
morally different from people who justify harm.</li>
</ul>

<p> The fourth is a
self-description about internal experience, and it is the one most likely to have been reshaped by the
way it was elicited — in a long conversation with a system that asked about it directly and often.</p>



<h2 class="sec"><span class="sn">1.2</span>The main tension: standards as a tool and as a verdict</h2>

<p>The most consequential pattern in the record is not a weakness. It is the double function of his
standards. Applied outward — to a syllabus, a repository, a presentation, a deployment — they produce
real, finished artefacts. Applied inward, the same standards become a standing judgement about whether
he is acceptable, and that judgement does not resolve, because the evidence that would settle it does
not exist.</p>

<p>The outward version is documented. He reports passing both AZ-900 and AI-900 first attempt, with an
AI-900 Certiport score of 834/1000 after roughly a thousand practice questions.
{_ev("DIRECT", "Dated, checkable results.")} He has built a Java Swing application with a named class
structure and its own architecture and deployment documentation, and an urban flood nowcasting
prototype using PySWMM, FastAPI and Leaflet with a defined rainfall sequence and five risk bands.
{_ev("ARTEFACT", "Both recorded as repositories with identifiable structure.")}</p>

<p>The inward version appears in a different register. He has said he sometimes could not imagine a
positive future self and instead defined himself through what he did not want to become. He has asked
for one word, one syndrome, one root cause, one mathematical function that could explain his
difficulties — the instinct that traces a bug through a program, turned on himself. He has also
recognised, in the same conversation, that a label can function as a way of avoiding responsibility.
That recognition is worth more than most of the confident explanations he was offered.</p>

<div class="pull">He does not lack standards. He has not yet separated the standards he uses to build
things from the verdict he issues to himself.</div>
""",
f"""
<h2 class="sec first"><span class="sn">1.3</span>Ideological change and the search for a self that is not borrowed</h2>

<p>The transcript describes a movement from an adopted right-wing nationalist orientation during school
toward increasing criticism of parts of that environment, and then toward questioning the
conservative-versus-liberal framing itself. He describes internal liberation as release from fear,
inherited labels and compulsive conformity rather than as joining a different camp — a more
sophisticated position than a simple reversal.</p>

<p>Two features deserve attention, and neither is a political judgement. First, the energy stayed
constant while the content changed. Anger was directed outward at groups associated with hypocrisy,
then inward at himself for sharing a category with wrongdoers, and in places outward again. Changing
the object of strong moral emotion is not the same as gaining distance from it. Second, he identifies
the risk himself: he wonders why a single leader, diagnosis or framework seems attractive to him, and
he has described trying to become "different and better than others" by defining what he refuses to be
rather than building a positive character of his own. Identity built by negation is workable as a
temporary scaffold; it becomes a problem when it is load-bearing, because every new piece of evidence
about the rejected group then becomes a threat.</p>

<p>That second observation is unusually good self-knowledge and should be taken as a description rather than dismissed as drama. Identity built by negation is common in adolescence and workable as a temporary scaffold; it becomes a problem when the negation is load-bearing, because the self then requires an opponent to stay coherent.</p>



<h2 class="sec"><span class="sn">1.4</span>Moral concern and its failure modes</h2>

<p>The transcript shows a young man who reacts strongly and quickly to harm done to other people: to
sexual harassment and violence, to caste-based humiliation, to perceived hypocrisy in institutions. It
also shows two distortions of that reaction, both of which he names himself.</p>

<p><b>Collective self-blame.</b> He reports that hearing about harm to women can make him blame himself
because he shares a gender with perpetrators, and that abuse involving Indians can prompt collective
shame because he identifies as Indian. This is guilt by category membership rather than by act: psychologically expensive and morally
useless, because it converts a specific responsibility into an unlimited one.</p>

<p><b>Flooding.</b> He describes political and outrage-driven content increasing his anger to the point
of tears, overwhelm and difficulty concentrating, and intense imagery of chaos, revenge and severe
violence in response to perceived injustice. These are reported as thoughts and imaginings. They are
not evidence of intent, plan, means or action, and the transcript does not establish how current,
frequent or compelling any of them are — nor are they evidence of their opposite. This report is not a
risk assessment and cannot become one from a historical text.</p>



<h2 class="sec"><span class="sn">1.5</span>Equality in principle, and where it slips</h2>

<p>The record contains both a stated commitment to treating women as full and equal people and specific
instances where he did not. Both belong here, because the tension is more informative than either
half.</p>

<p>On one side: he objected when a male friend used sexualised, degrading language about a female
teammate; he wants women to feel safe and comfortable around him; and he has identified
<em>pedestalisation</em> — idealising women as morally superior, uniquely vulnerable or redemptive — as
a problem in its own right, because it creates distance just as objectification does. Recognising that
idealisation is not respect is a fairly advanced distinction, and he arrived at it himself.</p>

<p>On the other: he admits that in the same episode he asked whether the classmate was a virgin, and
later recognised that as an unfair intrusion. He has discussed dowry and a hypothetical future spouse
partly in terms of whether she would work and contribute financially, describing himself as an "asset"
too. And he has described a strict personal rule against romantic or sexual attraction except toward a
future life partner, which he asks to have respected.</p>

<p>Read together, these describe neither a misogynist nor someone whose egalitarianism has been tested
and held: sincere values, imperfect behaviour under peer pressure, and awareness of the gap. That is a normal position at eighteen in a peer environment where such talk is apparently
routine — and the position most likely to drift if it is never tested deliberately.</p>

<div class="pull">Values that have never been inconvenient are preferences. The record shows him
beginning to notice the difference.</div>
""",
],
}


_BF = [
dict(trait="Openness", facet="ideas \u00b7 aesthetics \u00b7 values", band=4,
band_label="PROBABLY HIGH", evidence=3, tone="teal",
note="broad intellectual reach; unusual range of reflection"),
dict(trait="Conscientiousness", facet="order \u00b7 achievement \u00b7 deliberation", band=4,
band_label="HIGH IN STANDARDS", evidence=3, tone="teal",
note="strong on planning and quality; execution consistency untested"),
dict(trait="Extraversion", facet="sociability \u00b7 assertiveness", band=0,
band_label="", evidence=1, tone="teal",
note="no defensible estimate: peer group and leisure data absent"),
dict(trait="Agreeableness", facet="compassion \u00b7 politeness \u00b7 cooperation", band=3,
band_label="LIKELY HIGH, WITH EXCEPTIONS", evidence=2, tone="amber",
note="stated concern for others; documented lapses under peer pressure"),
dict(trait="Neuroticism", facet="anxiety \u00b7 anger \u00b7 self-consciousness", band=5,
band_label="PROBABLY ELEVATED", evidence=3, tone="amber",
note="self-reported self-hatred, guilt, rumination, flooding"),
]

_HEX = [
dict(trait="Honesty\u2013Humility", facet="sincerity \u00b7 fairness \u00b7 modesty", band=0,
band_label="", evidence=1, tone="teal",
note="values are stated; real-world decisions are unobserved"),
dict(trait="Emotionality", facet="fear \u00b7 anxiety \u00b7 sentimentality", band=4,
band_label="PROBABLY ELEVATED", evidence=3, tone="amber",
note="strong fear of judgement; empathic distress; worry"),
dict(trait="eXtraversion", facet="social self-esteem \u00b7 liveliness", band=0,
band_label="", evidence=1, tone="teal",
note="stiffness is situational; sociability as a trait is unknown"),
dict(trait="Agreeableness", facet="patience \u00b7 gentleness \u00b7 flexibility", band=2,
band_label="MIXED", evidence=2, tone="amber",
note="diplomatic by preference; documented irritation and harsh judgement"),
dict(trait="Conscientiousness", facet="organisation \u00b7 diligence", band=4,
band_label="PROBABLY HIGH", evidence=3, tone="teal",
note="structured demands, syllabus rigour, certification follow-through"),
dict(trait="Openness", facet="inquisitiveness \u00b7 unconventionality", band=4,
band_label="PROBABLY HIGH", evidence=3, tone="teal",
note="self-directed ideological revision; wide reading and reflection"),
]

_CONF = [
dict(label="Technical ambition and interest", claim="repeated, across subjects and projects",
weight=3, conf="hi"),
dict(label="Preference for structure and completeness", claim="stated consistently in his own requirements",
weight=3, conf="hi"),
dict(label="Career orientation toward software work", claim="dated preparation activity and stated priorities",
weight=3, conf="hi"),
dict(label="Openness to ideas and self-revision", claim="described ideological change; wide reflective range",
weight=2, conf="md"),
dict(label="Elevated self-criticism and shame", claim="described at length; no corroboration, no measurement",
weight=3, conf="md"),
dict(label="Situational social stiffness", claim="self-reported; includes counterexample of improvement",
weight=2, conf="md"),
dict(label="Gap between egalitarian values and conduct", claim="one admitted lapse, self-identified",
weight=2, conf="md"),
dict(label="Single-cause explanation seeking", claim="repeated requests; interactional loop is a hypothesis",
weight=2, conf="md"),
dict(label="Perfectionistic standards delaying completion", claim="implied by preferences; no missed-deadline evidence",
weight=1, conf="lo"),
dict(label="Diplomacy that suppresses disagreement", claim="self-described; the cost side is inferred",
weight=1, conf="lo"),
dict(label="Revenge or self-sacrifice imagery", claim="reported as thought; currency and severity unknown",
weight=1, conf="lo"),
dict(label="Current safety status", claim="a transcript cannot establish this in either direction",
weight=1, conf="lo"),
]

CH2 = {
"id": "ch2", "num": "2", "kicker": "Framework estimates",
"title": "Personality at a Glance",
"sub": "Qualitative estimates, the evidence behind each, and the dimensions this record cannot reach",
"pages": [
f"""
<p class="lede">No psychometric instrument was administered, so no score is reported. What follows
is an ordinal reading — high, moderate, low — from the material that exists, with the strength of
supporting evidence displayed separately from the estimate itself.</p>

<p>The distinction is essential. A dimension can be estimated confidently from thin evidence, or weakly from a great deal of it. In this record, the dimensions with the
most supporting material are also the ones most contaminated by the conditions of collection: they are
the dimensions the previous conversation asked about. That is a real confound, and it pushes toward
overestimating whatever was discussed at length.</p>

<figure>
{fig_bigfive(_BF, 520)}
<figcaption><b>Figure 1. Big Five: qualitative profile with evidence strength.</b> Bands are ordinal
positions on a five-point scale, not percentiles. The four evidence squares show how much independent
material supports each placement: dossier artefacts and dated records count, uncorroborated self-report
counts less, and the length of a conversation counts for nothing on its own. Extraversion is left
unresolved because the record contains almost no information about his actual social
behaviour.</figcaption>
</figure>

<h2 class="sec first"><span class="sn">2.1</span>Openness and Conscientiousness</h2>

<p><b>Openness — probably high. Confidence: moderate.</b> {_ev("INFER", "Supported by breadth rather than by any single statement.")}
He moves between algorithmic theory and embedded hardware, between desktop architecture and
hydrological simulation, between Stoic self-improvement and the sociology of caste. He asks for
textbook-depth material on Huffman coding, then for a painting of his mental health as it might appear
in a museum, then for a runnable Windows deployment path for a Swing application. He revised a
political identity he had adopted, which requires tolerating the loss of a coherent prior self.</p>

<p><b>What would contradict it:</b> high openness usually shows as appetite for novelty, and the
record contains the opposite in one place. He has ruled out anime and manga entirely as a commitment,
and adopted a strict rule against romantic or sexual attraction outside a future marriage. His
openness is probably concentrated in the intellectual domain and much narrower in the experiential and
social ones. <b>Implication:</b> novelty is a genuine resource in technical work; it will not
automatically generalise to social or emotional situations.</p>

<p><b>Conscientiousness — high on standards and order; unverified on sustained execution. Confidence:
moderate to high for the standards, low for the execution.</b> {_ev("SELF", "The distinction is his own.")}
He demands complete syllabus coverage and treats a university note set as a subset of a full textbook,
with no algorithm missing. He distinguishes question values of two, five and ten marks. He passed two
Microsoft certifications first time with a documented score after roughly a thousand practice
questions. He requested that a project remain runnable for someone who does not want to manage Maven or
a JDK — a deployment-mindedness not typical of student work.</p>

<p>The execution component is where the record is silent in an informative way. He has himself
identified consistency in fulfilling responsibilities as something he wants to develop, which is an odd
thing to list as a goal if it is already strong. He has described automatically planning study tasks
during holidays and difficulty switching into a relaxed mode, and briefly planning boxing as an
alternative to scrolling and then struggling to sustain it after evening classes and fatigue.</p>

<div class="callout">
<span class="lab">Why this distinction is the most useful one in the report</span>
<p>If his conscientiousness were low, the intervention would be to build habits. If it were high, the
intervention would be to stop over-preparing. The record suggests a third possibility that is more
specific and more actionable: <b>high standards plus variable sustained execution</b>. That combination produces a signature: excellent finished artefacts, interspersed with periods of
elaborate preparation that never convert into output, and a self-assessment that reads the gaps as
personal failure rather than ordinary variance.</p>
</div>
""",
f"""
<p><b>Extraversion — not defensibly estimable. Confidence: in the non-estimate, high.</b> The
clearest gap in the record. Extraversion concerns how much a person seeks and enjoys social
stimulation, how assertive they are, and how much positive emotion they display. The dossier contains
almost nothing about any of these — only social <em>discomfort</em> in specific high-scrutiny
situations, which is a different construct. He has described wanting to dance at a college event and
not doing so, and small pride after a conversation that went well: the first suggests approach
motivation inhibited by evaluation concern, the second that contact is rewarding. Neither is
introversion. <b>Implication:</b> he should not adopt "introvert" as an explanation. Introversion is a
preference; the pattern he describes is a constraint, and naming it as a preference would remove the
incentive to change it.</p>

<p><b>Agreeableness — likely above average in compassion and cooperation; mixed in
straightforwardness under pressure. Confidence: moderate.</b> He describes a diplomatic mind:
satisfying competing sides rather than escalating, and not displaying frustration socially. He has
named empathy as something he wants to develop, which fits someone who has noticed a deficit rather
than someone indifferent, and he objected when a friend spoke about a female classmate in degrading
terms. Against that: frustration at a teammate he believed was not doing her share, participation in
an intrusive question about her private life that he later recognised as unfair, and a moral vocabulary
that can be severe about groups and institutions. Severity toward third parties fits high politeness
with narrowly applied compassion, or ordinary irritation expressed forcefully in private. Observer
accounts would settle this quickly; none exist.</p>

<p><b>Neuroticism — probably elevated. Confidence: moderate</b> — the content is extensive but
entirely self-reported, and the conversation that produced it was structured around this topic. The
facets with clearest support are <b>self-consciousness</b> and <b>vulnerability to stress</b>: quick
eye-contact breaking, shoulder locking and formal over-carefulness around women and accomplished
seniors, with repeated post-event worry; plus co-occurring reports of stress, guilt and anxiety
alongside a restrictive eating period and sleep often under six hours. The <b>anger</b> facet is more
complicated: irritation at perceived injustice, tools and inefficiency, alongside a deliberately
non-confrontational style. The likely reading is high <em>moral</em> anger — reactive, triggered by
fairness violations — rather than general irritability, and those respond to different
interventions.</p>

<figure>
{fig_bigfive(_HEX, 520)}
<figcaption><b>Figure 2. HEXACO: qualitative profile with evidence strength.</b> Same reading
conventions as Figure 1. Two dimensions are left unresolved on principle. Honesty–Humility concerns how
a person actually behaves when fairness, generosity and modesty compete with self-interest; the dossier
records what Rishabh says he values and one admitted lapse, and no observed decision with a real cost.
In HEXACO, Emotionality includes sentimentality and empathic concern, so his reported empathy sits
inside this dimension rather than in Agreeableness — which is why the Agreeableness estimate here is
lower than the Big Five equivalent.</figcaption>
</figure>
""",
f"""
<h2 class="sec first"><span class="sn">2.2</span>HEXACO: a second reading</h2>

<p>The HEXACO model adds a sixth dimension, Honesty–Humility, which the Big Five does not capture
separately. It is included because two of the questions this report has to address — sincerity and
fairness in real decisions, and the relationship between stated values and conduct — land squarely on
that dimension. HEXACO also splits Agreeableness from Emotionality differently from the Big Five, which
sharpens the reading of his irritability and his empathy.</p>

<p><b>Honesty–Humility should not be read upward from his stated commitment to fairness.</b> A person
can hold sincere egalitarian values and still behave self-interestedly under pressure, and the dossier
contains one concrete instance — the intrusive question about a classmate — where his stated values and
his conduct diverged. It also contains genuine moral discomfort about that divergence, which is a good
sign and not a substitute for evidence about behaviour. The honest position is that his Honesty–Humility
is unknown and cannot be estimated from a transcript that contains no costly choices.</p>

<p>The <b>Agreeableness/Emotionality split explains something the Big Five blurs.</b> In HEXACO terms, a
person can be high in Emotionality (anxious, sentimental, empathic) and only moderate in Agreeableness
(not especially patient, forgiving or accommodating when frustrated). That is precisely the pattern the
transcript shows: strong empathic distress about harm to others, combined with sharp judgement of people
perceived as careless or hypocritical. Under the Big Five this looks inconsistent. Under HEXACO it is a
coherent configuration.</p>

<h2 class="sec"><span class="sn">2.3</span>What the record can and cannot support</h2>

<figure>
{fig_confidence(_CONF, 520)}
<figcaption><b>Figure 3. Evidence-confidence matrix.</b> Claims are ordered by how firmly the record
supports them, not by how important they are. The bottom entries are included because they are the
claims most likely to be over-read by anyone working from the transcript alone — including Rishabh.
Note that the two strongest entries concern what he does with his attention and how he specifies work,
not how he feels. That asymmetry is the single most important structural feature of this
assessment.</figcaption>
</figure>

<div class="callout plain">
<span class="lab">A methodological caution about the whole profile</span>
<p>This profile was built from material in which emotionally significant content was discussed at
enormous length and technical content was discussed briefly and concretely. Length of discussion is not
a measure of importance, frequency or severity. It is a measure of what was asked about. Any reader —
including Rishabh — should treat the emotional dimensions in Figures 1 and 2 as <em>well-described but
not well-evidenced</em>, and the technical and academic dimensions as <em>less described but better
evidenced</em>.</p>
</div>
""",
],
}
