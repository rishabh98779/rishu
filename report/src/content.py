"""Final report content, Chapters 1-13, written to the page budget.

Evidence vocabulary used consistently throughout:
  DIRECT   dated record in the dossier (enrolment, scores, artefacts, results)
  ARTEFACT repository, submission or document that exists independently
  SELF     first-person report, uncorroborated
  INFER    a reading the analyst draws from one or more of the above
  HYPOTH   a testable possibility, offered with the test stated
"""
from figures import (fig_bigfive, fig_confidence, fig_siebc, fig_loops,
                     fig_strengths, fig_values, fig_plan, fig_predkey)
from content_e import CH14


def _ev(kind, s):

    cls = {"DIRECT": "hi", "ARTEFACT": "hi", "SELF": "md",
           "INFER": "md", "HYPOTH": "lo"}[kind]
    return f'<span class="conf {cls}">{kind.lower()}</span> {s}'


# ============================================================ CHAPTER 1
from final_a import CH1, CH2  # noqa: E402,F401

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




# Chapter bodies live in dedicated modules.
from final_b import CH3, CH4        # noqa: E402,F401
from content_risk import CH5        # noqa: E402,F401
from content_b import CH6           # noqa: E402,F401
from content_c import CH7, CH8, CH9  # noqa: E402,F401
from content_d import CH10, CH11, CH12, CH13  # noqa: E402,F401
from content_e import CH14          # noqa: E402,F401
