"""Vector figure builders for the Rishabh Singh personality report.

Every figure is hand-composed SVG so that no numeric value appears unless it is
derived from evidence. Qualitative traits are drawn on labelled ordinal bands;
where the record cannot support an estimate the band is drawn as a hatched
"unresolved" segment rather than being assigned a position.
"""
from __future__ import annotations

NAVY = "#101A33"
NAVY2 = "#1B2A4A"
NAVY3 = "#2C3E63"
IVORY = "#FBF8F1"
IVORY2 = "#F4EFE3"
IVORY3 = "#EDE6D6"
TEAL = "#146E68"
TEAL2 = "#2C8F86"
TEAL3 = "#8FC4BD"
TEALW = "#E4EFEC"
AMBER = "#9A6714"
AMBER2 = "#C08A2A"
AMBER3 = "#E4C287"
AMBERW = "#F7EEDC"
CHAR = "#23262B"
CHAR2 = "#4A5058"
CHAR3 = "#6E757E"
RULE = "#D8D0BE"
RULE2 = "#E6DFCF"

FS = 'font-family="Inter,sans-serif"'
FG = 'font-family="Garamond,serif"'

_counter = [0]


def _uid(prefix="g"):
    _counter[0] += 1
    return f"{prefix}{_counter[0]}"


def esc(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg(w, h, body, cls="fig"):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img">{body}</svg>')


def text(x, y, s, size=8, fill=CHAR2, anchor="start", family=FS, weight="400",
         style="", ls="0", opacity=None):
    extra = f' letter-spacing="{ls}"' if ls != "0" else ""
    if style:
        extra += f' font-style="{style}"'
    if opacity is not None:
        extra += f' opacity="{opacity}"'
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'{family} font-weight="{weight}"{extra}>{esc(s)}</text>')


def line(x1, y1, x2, y2, stroke=RULE, w=0.8, dash=None, cap="butt", op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{w}" stroke-linecap="{cap}"{d}{o}/>')


def rect(x, y, w, h, fill="none", stroke="none", sw=0.8, rx=0, dash=None, op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}" rx="{rx}"{d}{o}/>')


def path(d, fill="none", stroke="none", sw=1.0, dash=None, op=None, cap="round"):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="{cap}" stroke-linejoin="round"{dd}{o}/>')


def circle(cx, cy, r, fill="none", stroke="none", sw=0.8, op=None):
    o = f' opacity="{op}"' if op is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{o}/>'


# --------------------------------------------------------------------------
# 1. Big Five profile: qualitative ordinal bands with separate evidence gauge
# --------------------------------------------------------------------------
def fig_bigfive(rows, width=520):
    """rows: list of dicts {trait, band, band_label, evidence, note}
    band is 0..4 ordinal (0 unresolved)."""
    rh = 40
    head = 26
    h = head + rh * len(rows) + 34
    L = 118          # label column
    GX = L + 6       # gauge x
    GW = width - GX - 96
    out = []
    # header
    out.append(text(GX, 10, "LOW", 6.2, CHAR3, weight="700", ls="1.4"))
    out.append(text(GX + GW / 2, 10, "MODERATE", 6.2, CHAR3, anchor="middle", weight="700", ls="1.4"))
    out.append(text(GX + GW, 10, "HIGH", 6.2, CHAR3, anchor="end", weight="700", ls="1.4"))
    out.append(line(GX, 14, GX + GW, 14, RULE, 0.6))
    # band edges for 5 levels
    for i in range(6):
        x = GX + GW * i / 5
        out.append(line(x, 16, x, head + rh * len(rows) - 3, RULE2, 0.5, dash="1.2 2.2"))
    for i, r in enumerate(rows):
        y = head + i * rh
        band = r["band"]
        # label
        out.append(text(L, y + 12, r["trait"], 8.6, NAVY, anchor="end", family=FG, weight="600"))
        out.append(text(L, y + 21, r.get("facet", ""), 6.0, CHAR3, anchor="end"))
        # track
        out.append(rect(GX, y + 2, GW, 11.5, fill="#FFFFFF", stroke=RULE2, sw=0.6, rx=1.4))
        if band == 0:
            # unresolved: hatched full band
            uid = _uid("hatch")
            out.append(f'<defs><pattern id="{uid}" width="5" height="5" patternUnits="userSpaceOnUse" '
                       f'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" '
                       f'stroke="{AMBER3}" stroke-width="1.6"/></pattern></defs>')
            out.append(rect(GX + 1, y + 3, GW - 2, 9.5, fill=f"url(#{uid})", rx=1.1))
            out.append(text(GX + GW / 2, y + 9.8, "not estimable on this record", 6.3,
                            AMBER, anchor="middle", weight="650"))
        else:
            span = (band - 1) * (GW / 5)     # band 1 => zero-width at low
            x0 = GX + span
            x1 = GX + band * (GW / 5)
            col = TEAL if r.get("tone", "teal") == "teal" else AMBER2
            wash = TEALW if r.get("tone", "teal") == "teal" else AMBERW
            out.append(rect(x0 + 1, y + 3, max(x1 - x0 - 2, 3), 9.5, fill=wash, rx=1.1))
            out.append(rect(x0 + 1, y + 3, max(x1 - x0 - 2, 3), 9.5, fill="none", stroke=col, sw=0.7, rx=1.1))
            out.append(line(x0 + 1, y + 3, x1 - 1, y + 12.5, col, 0.7, op=0.35))
            out.append(line(x1 - 1, y + 3, x0 + 1, y + 12.5, col, 0.7, op=0.35))
            out.append(text((x0 + x1) / 2, y + 9.8, r["band_label"], 6.3, col,
                            anchor="middle", weight="700", ls="0.3"))
        # evidence gauge
        ev = r["evidence"]     # 0..4
        ex = width - 84
        out.append(text(ex - 4, y + 9.8, "evidence", 5.8, CHAR3, anchor="end"))
        for k in range(4):
            filled = k < ev
            out.append(rect(ex + k * 8.4, y + 4, 6.4, 6.8,
                            fill=NAVY3 if filled else "#FFFFFF",
                            stroke=NAVY3 if filled else RULE, sw=0.55, rx=1))
        out.append(text(ex, y + 22, r.get("note", ""), 6.0, CHAR3))
    # footer legend
    fy = head + rh * len(rows) + 5
    out.append(rect(0, fy, width, 24, fill=IVORY2, rx=1.4))
    out.append(text(8, fy + 10, "READING THE SCALE", 6.2, NAVY, weight="700", ls="1.2"))
    out.append(text(8, fy + 18.4, "Ordinal estimate from self-report and dossier evidence \u2014 not a percentile and not a standardised score. The four evidence "
                                "squares show how much independent material supports each estimate. Hatched bands mark dimensions the record cannot defensibly place.", 6.2, CHAR2))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 2. Evidence-confidence matrix
# --------------------------------------------------------------------------
def fig_confidence(items, width=520):
    """items: {label, claim, weight(1-3), conf('hi','md','lo'), group}"""
    rh = 21.5
    head = 42
    h = head + rh * len(items) + 34
    L = 176
    GX = L + 4
    GW = width - GX - 10
    cols = {"hi": (TEAL, TEALW), "md": (AMBER2, AMBERW), "lo": (CHAR3, "#EDE9E1")}
    out = []
    out.append(text(0, 12, "CLAIM IN THE RECORD", 6.6, NAVY, weight="700", ls="1.3"))
    out.append(text(GX, 12, "HOW FIRMLY THE EVIDENCE SUPPORTS IT", 6.6, NAVY, weight="700", ls="1.3"))
    out.append(line(0, 17, width, 17, NAVY, 0.9))
    for i, it in enumerate(items):
        y = head + i * rh
        if i % 2 == 0:
            out.append(rect(0, y - 11, width, rh, fill="#FFFFFF", op=0.55))
        out.append(text(0, y - 3.5, it["label"], 8.2, NAVY, weight="600"))
        out.append(text(0, y + 4.6, it["claim"], 6.6, CHAR3))
        col, wash = cols[it["conf"]]
        w = GW * it["weight"] / 3.0
        out.append(rect(GX, y - 9.4, w, 10.6, fill=wash, rx=1.1))
        out.append(rect(GX, y - 9.4, w, 10.6, fill="none", stroke=col, sw=0.6, rx=1.1))
        lbl = {"hi": "well supported", "md": "plausible, untested", "lo": "speculative"}[it["conf"]]
        out.append(text(GX + w + 5, y - 1.4, lbl, 6.4, col, weight="650"))
        out.append(line(0, y + 8, width, y + 8, RULE2, 0.5))
    fy = head + rh * len(items) + 6
    out.append(text(0, fy + 8, "Weight reflects the number and independence of supporting observations, "
                               "not the seriousness of the claim.", 6.6, CHAR3))
    out.append(text(0, fy + 16, "Claims rest on self-report unless the dossier records an artefact "
                                "(repository, submission, result).", 6.6, CHAR3))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 3. Strengths and shadow sides
# --------------------------------------------------------------------------
def fig_strengths(pairs, width=520):
    """pairs: {name, strength, shadow, evidence}"""
    rh = 28
    head = 30
    h = head + rh * len(pairs) + 22
    cw = (width - 116) / 2
    L = 110
    out = []
    out.append(text(L, 12, "ASSET WHEN \u2026", 6.6, TEAL, weight="700", ls="1.2"))
    out.append(text(L + cw + 6, 12, "LIABILITY WHEN \u2026", 6.6, AMBER, weight="700", ls="1.2"))
    out.append(line(L, 17, width, 17, NAVY, 0.9))
    for i, p in enumerate(pairs):
        y = head + i * rh
        out.append(text(0, y - 3, p["name"], 8.5, NAVY, weight="650", family=FG))
        ev = p.get("evidence", 2)
        out.append(text(0, y + 5, "evidence " + "\u25A0" * ev + "\u25A1" * (3 - ev), 5.9, CHAR3, ls="0.5"))
        # strength box
        out.append(rect(L, y - 11, cw, 22, fill=TEALW, rx=1.2))
        out.append(rect(L, y - 11, 1.6, 22, fill=TEAL))
        _wrap(out, L + 5, y - 5, cw - 9, p["strength"], 7.0, NAVY2, 2)
        # shadow box
        out.append(rect(L + cw + 6, y - 11, cw, 22, fill=AMBERW, rx=1.2))
        out.append(rect(L + cw + 6, y - 11, 1.6, 22, fill=AMBER2))
        _wrap(out, L + cw + 11, y - 5, cw - 9, p["shadow"], 7.0, "#6B4A12", 2)
        out.append(line(0, y + 17, width, y + 17, RULE2, 0.5))
    fy = head + rh * len(pairs) + 4
    out.append(text(0, fy + 8, "Both columns describe the same underlying disposition. The right-hand column is "
                               "not a defect of character but a failure mode of a real strength.", 6.6, CHAR3))
    return svg(width, h, "".join(out))


def _wrap(out, x, y, maxw, s, size, fill, maxlines=3, lh=None):
    """Crude character-budget wrap for SVG <text>."""
    lh = lh or size * 1.36
    budget = int(maxw / (size * 0.50))
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= budget:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > maxlines:
        lines = lines[:maxlines]
        lines[-1] = lines[-1][: max(0, budget - 2)] + "\u2026"
    for i, ln in enumerate(lines):
        out.append(text(x, y + i * lh, ln, size, fill))
    return len(lines)


# --------------------------------------------------------------------------
# 4. Situation -> Interpretation -> Emotion -> Behaviour -> Consequence model
# --------------------------------------------------------------------------
def fig_siebc(width=520):
    stages = [
        ("SITUATION", "Observable trigger", "Interpersonal scrutiny;\nmoralised media;\nambiguous feedback", NAVY),
        ("INTERPRETATION", "Appraisal", "What does this say\nabout me / about\nwhat is fair?", NAVY3),
        ("EMOTION", "Affect", "Shame, guilt,\nanxiety, anger,\ncollective blame", TEAL),
        ("BEHAVIOUR", "Overt or covert act", "Stiffness, silence,\nrehearsal, scrolling,\nor focused work", AMBER2),
        ("CONSEQUENCE", "Feedback to the system", "Short relief;\nfatigue; less\navailable evidence", AMBER),
    ]
    h = 214
    bw = (width - 4 * 9) / 5
    out = []
    out.append(text(0, 11, "SITUATION \u2013 INTERPRETATION \u2013 EMOTION \u2013 BEHAVIOUR \u2013 CONSEQUENCE", 6.8, NAVY, weight="700", ls="1.3"))
    out.append(line(0, 16, width, 16, NAVY, 0.9))
    for i, (name, role, body, col) in enumerate(stages):
        x = i * (bw + 9)
        out.append(rect(x, 26, bw, 132, fill="#FFFFFF", stroke=RULE2, sw=0.6, rx=1.6))
        out.append(rect(x, 26, bw, 3, fill=col, rx=1.2))
        out.append(text(x + 5, 41, name, 7.0, col, weight="700", ls="0.9"))
        out.append(text(x + 5, 50, role, 6.4, CHAR3, style="italic"))
        for j, ln in enumerate(body.split("\n")):
            out.append(text(x + 5, 63 + j * 9.4, ln, 7.1, CHAR))
        out.append(line(x + 5, 92, x + bw - 5, 92, RULE2, 0.5))
        # evidence marker per stage
        marks = {0: 3, 1: 1, 2: 3, 3: 2, 4: 1}[i]
        out.append(text(x + 5, 101, "evidence", 5.9, CHAR3))
        for k in range(3):
            out.append(rect(x + 26 + k * 7.4, 96, 5.6, 5.6,
                            fill=NAVY3 if k < marks else "#FFFFFF",
                            stroke=NAVY3 if k < marks else RULE, sw=0.5, rx=0.8))
        # which link is documented
        link = {0: "documented", 1: "inferred", 2: "documented",
                3: "documented", 4: "inferred"}[i]
        out.append(text(x + 5, 114, link, 6.1, TEAL if link == "documented" else AMBER, weight="650"))
        if i < 4:
            ax = x + bw + 1.6
            out.append(path(f"M{ax} 92 L{ax+5.6} 92 M{ax+3.4} 89.4 L{ax+5.6} 92 L{ax+3.4} 94.6",
                            stroke=AMBER2, sw=1.1))
    # feedback loop
    yb = 158
    out.append(path(f"M{width*0.9} 158 C{width*0.9} {yb+16} {width*0.1} {yb+16} {width*0.1} 158",
                    stroke=AMBER2, sw=0.9, dash="3 2.4"))
    out.append(path(f"M{width*0.1+3.6} 160 L{width*0.1} 152.4 L{width*0.1-3.6} 160",
                    stroke=AMBER2, sw=0.9))
    out.append(text(width / 2, yb + 20, "AVOIDANCE LOOP \u2014 relief from acting briefly lowers the cost of "
                                        "repeating the same appraisal next time", 6.5, AMBER, anchor="middle", weight="650"))
    out.append(text(width / 2, yb + 30, "A second candidate loop runs through attention rather than avoidance: "
                                        "moralised content \u2192 outrage \u2192 rumination \u2192 fatigue \u2192 more "
                                        "content. Both are hypotheses to test, not established mechanisms.", 6.5, CHAR3, anchor="middle"))
    out.append(rect(0, 186, width, 24, fill=IVORY2, rx=1.4))
    out.append(text(7, 197, "A thought is not a feeling; a feeling is not an intention; an intention is not an act. "
                            "This model tracks the links the record actually documents and marks the rest as inferred.", 6.6, CHAR2))
    out.append(text(7, 205, "No step in this sequence is a diagnosis, and no step establishes current risk.", 6.6, CHAR3))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 5. Values vs behavioural tendencies
# --------------------------------------------------------------------------
def fig_values(rows, width=520):
    """rows: {value, direction: 'consistent'|'mixed'|'tension', note, evidence}"""
    rh = 24
    head = 34
    h = head + rh * len(rows) + 40
    L = 132
    GX = L + 4
    GW = width - GX - 96
    out = []
    out.append(text(GX, 12, "EVIDENCE OF CONSISTENT BEHAVIOUR", 6.5, NAVY, weight="700", ls="1.2"))
    out.append(line(0, 17, width, 17, NAVY, 0.9))
    # axis: -2..+2 as tension..consistent
    mid = GX + GW / 2
    out.append(line(mid, 22, mid, head + rh * len(rows) - 4, RULE, 0.7))
    out.append(text(mid, 30, "mixed / untested", 6.2, CHAR3, anchor="middle"))
    for i, r in enumerate(rows):
        y = head + i * rh
        if i % 2 == 0:
            out.append(rect(0, y - 11, width, rh, fill="#FFFFFF", op=0.55))
        out.append(text(0, y - 2, r["value"], 8.5, NAVY, weight="650", family=FG))
        out.append(text(0, y + 6.4, r["note"], 6.5, CHAR3))
        pos = {"consistent": 1.6, "leaning": 0.7, "mixed": 0.0,
               "tension": -0.9, "untested": 0.0}[r["direction"]]
        col = {"consistent": TEAL, "leaning": TEAL2, "mixed": CHAR3,
               "tension": AMBER2, "untested": CHAR3}[r["direction"]]
        x = mid + pos * (GW / 2) / 2.2
        if r["direction"] == "untested":
            out.append(rect(GX + 4, y - 8, GW - 8, 9.4, fill="none", stroke=RULE,
                            sw=0.6, rx=1, dash="2.4 2"))
            out.append(text(mid, y - 1, "no behavioural evidence available", 6.4,
                            CHAR3, anchor="middle", weight="650"))
        else:
            out.append(line(GX + 6, y - 3.2, x, y - 3.2, col, 0.7, op=0.5))
            out.append(circle(x, y - 3.2, 3.4, fill=col, stroke="#FFFFFF", sw=0.7))
            lbl = {"consistent": "broadly consistent", "leaning": "partly consistent",
                   "mixed": "mixed", "tension": "documented tension"}[r["direction"]]
            out.append(text(x + (7 if pos >= 0 else -7), y - .6, lbl, 6.4, col,
                            anchor="start" if pos >= 0 else "end", weight="650"))
        ev = r["evidence"]
        ex = width - 74
        for k in range(4):
            out.append(rect(ex + k * 9, y - 8.4, 7, 7.5,
                            fill=NAVY3 if k < ev else "#FFFFFF",
                            stroke=NAVY3 if k < ev else RULE, sw=0.55, rx=1))
        out.append(line(0, y + 10, width, y + 10, RULE2, 0.5))
    fy = head + rh * len(rows) + 6
    out.append(text(0, fy + 8, "This is a reflection matrix, not a moral scorecard. A point left of centre records "
                               "that the record shows the value being overridden \u2014 it does not establish how "
                               "often, or that the value is insincere.", 6.6, CHAR2))
    out.append(text(0, fy + 16.5, "Dashed rows are values the dossier states but never shows being tested in behaviour.", 6.6, CHAR3))
    out.append(text(0, fy + 25, "No independent observer accounts exist, so consistency is judged only against "
                                "Rishabh's own reported conduct.", 6.6, CHAR3))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 6. Candidate loop map (self-audit loop and injustice loop)
# --------------------------------------------------------------------------
def fig_loops(width=520):
    h = 268
    out = []
    out.append(text(0, 11, "TWO CANDIDATE LOOPS \u2014 HYPOTHESES, WITH THEIR ALTERNATIVES", 6.8, NAVY, weight="700", ls="1.2"))
    out.append(line(0, 16, width, 16, NAVY, 0.9))

    def loop(cx, cy, r, nodes, col, wash, title):
        parts = []
        parts.append(text(cx, cy - r - 14, title, 7.4, col, weight="700", ls="0.9", anchor="middle"))
        parts.append(circle(cx, cy, r, fill=wash, stroke=col, sw=0.6, op=0.55))
        import math
        n = len(nodes)
        pts = []
        for i in range(n):
            a = -math.pi / 2 + 2 * math.pi * i / n
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            # arc between points
            parts.append(path(f"M{x1} {y1} A {r} {r} 0 0 1 {x2} {y2}", stroke=col, sw=1.0, op=0.75))
            # arrowhead at destination
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax = mx + (x2 - mx) * 0.18
            ay = my + (y2 - my) * 0.18
            dx, dy = x2 - x1, y2 - y1
            L = math.hypot(dx, dy) or 1
            ux, uy = dx / L, dy / L
            parts.append(path(f"M{ax} {ay} l{-ux*4.4-uy*2.4} {-uy*4.4+ux*2.4} "
                              f"M{ax} {ay} l{-ux*4.4+uy*2.4} {-uy*4.4-ux*2.4}",
                              stroke=col, sw=1.0))
        for (x, y), (lbl, sub) in zip(pts, nodes):
            inside = x < cx + r * 0.35 and x > cx - r * 0.35
            anchor = "middle" if abs(x - cx) < r * 0.42 else ("start" if x > cx else "end")
            dx = 0 if anchor == "middle" else (6 if x > cx else -6)
            parts.append(text(x + dx, y + (0 if anchor == "middle" else 0), lbl, 6.9, NAVY, weight="650", anchor=anchor))
            parts.append(text(x + dx, y + 8, sub, 6.1, CHAR3, anchor=anchor))
        return parts

    out += loop(128, 118, 74,
                [("Social exposure", "a woman, a senior, a group"),
                 ("Self-focus", "\u201cwhat am I giving off?\u201d"),
                 ("Stiffness / brevity", "eye contact breaks, formal tone"),
                 ("Post-event review", "replay, grading, anticipation")],
                TEAL, TEALW, "LOOP A \u2014 SELF-AUDIT AND SOCIAL STIFFNESS")

    out += loop(392, 118, 74,
                [("Moralised content", "reels, outrage, testimony"),
                 ("Appraisal", "this is unjust; I share the category"),
                 ("Anger or collective guilt", "flooding, tears, blame"),
                 ("Rumination and fatigue", "less focus, more scrolling")],
                AMBER2, AMBERW, "LOOP B \u2014 INJUSTICE CONTENT AND FLOODING")

    yb = 210
    out.append(rect(0, yb, width, 52, fill=IVORY2, rx=1.4))
    out.append(text(7, yb + 12, "ALTERNATIVE EXPLANATIONS THAT FIT THE SAME EVIDENCE", 6.6, NAVY, weight="700", ls="1.1"))
    alts = [
        "Loop A: ordinary unfamiliarity and respectful caution; a modest, context-specific social skill gap; "
        "self-focused attention rather than a stable trait of low sociability.",
        "Loop B: accurate moral perception that is simply expressed with strong feeling; a genuine and "
        "well-founded response to injustice; an attention environment that is engineered to produce outrage.",
        "Both: a habit of seeking a single explanation may itself generate the appearance of a loop, because "
        "each retrospective account is built after the fact and shaped by the question being asked.",
    ]
    for i, a in enumerate(alts):
        out.append(text(7, yb + 22 + i * 9.4, "\u2022 " + a, 6.5, CHAR2))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 7. Development plan (30-day)
# --------------------------------------------------------------------------
def fig_plan(priorities, width=520):
    rh = 92
    head = 40
    h = head + rh * len(priorities) + 26
    out = []
    cols = ["Minimum action", "Indicator", "Missed-day rule", "Weekly review", "Progress looks like"]
    cw = [width * .185, width * .18, width * .185, width * .20, width * .25]
    out.append(text(0, 12, "THREE PRIORITIES \u2014 THIRTY DAYS", 6.8, NAVY, weight="700", ls="1.3"))
    out.append(line(0, 17, width, 17, NAVY, 0.9))
    for i, p in enumerate(priorities):
        y = head + i * rh
        out.append(rect(0, y - 15, width, rh - 4, fill="#FFFFFF" if i % 2 == 0 else IVORY2, rx=1.6))
        out.append(rect(0, y - 15, 2.4, rh - 4, fill=[TEAL, NAVY3, AMBER2][i]))
        out.append(text(8, y - 4, f"PRIORITY {i+1}", 6.3, [TEAL, NAVY3, AMBER2][i], weight="700", ls="1.2"))
        out.append(text(8, y + 6, p["name"], 9.2, NAVY, weight="650", family=FG))
        # wrapped objective
        _wrap(out, 8, y + 17, width * 0.95, p["behaviour"], 6.8, CHAR2, 3, lh=8.6)
        out.append(line(8, y + 44, width - 8, y + 44, RULE2, 0.5))
        x = 8
        for j, c in enumerate(cols):
            out.append(text(x, y + 54, c.upper(), 5.9, CHAR3, weight="700", ls="0.8"))
            _wrap(out, x, y + 63, cw[j] - 7, p["cells"][j], 6.6, CHAR, 3, lh=8.2)
            x += cw[j]
    fy = head + rh * len(priorities) + 4
    out.append(text(0, fy + 8, "A month changes practice, not personality. The target is a reliable minimum that "
                               "survives a bad week, not an ideal routine that collapses in one.", 6.6, CHAR2))
    out.append(text(0, fy + 16.5, "Every indicator is observable by Rishabh alone. None requires an app, a "
                                  "purchase, or another person's cooperation.", 6.6, CHAR3))
    return svg(width, h, "".join(out))


# --------------------------------------------------------------------------
# 8. Cover artwork: "interior architecture"
# --------------------------------------------------------------------------
def cover_art(width=760, height=340):
    """Abstract: nested arches / load-bearing lines carrying four strands."""
    import math
    out = []
    uid = _uid("cov")
    out.append(f'''<defs>
      <linearGradient id="{uid}a" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#1B2A4A"/><stop offset="55%" stop-color="#101A33"/>
        <stop offset="100%" stop-color="#0A1226"/></linearGradient>
      <linearGradient id="{uid}b" x1="0" y1="1" x2="1" y2="0">
        <stop offset="0%" stop-color="{TEAL}" stop-opacity="0.95"/>
        <stop offset="60%" stop-color="{TEAL2}" stop-opacity="0.7"/>
        <stop offset="100%" stop-color="{TEAL3}" stop-opacity="0.35"/></linearGradient>
      <linearGradient id="{uid}c" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="{AMBER2}" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="{AMBER3}" stop-opacity="0.35"/></linearGradient>
      <radialGradient id="{uid}d" cx="0.5" cy="0.45" r="0.62">
        <stop offset="0%" stop-color="#2C3E63" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0A1226" stop-opacity="0"/></radialGradient>
      <clipPath id="{uid}clip"><rect x="0" y="0" width="{width}" height="{height}"/></clipPath>
    </defs>''')
    out.append(rect(0, 0, width, height, fill=f"url(#{uid}a)"))
    out.append(rect(0, 0, width, height, fill=f"url(#{uid}d)"))

    # fine structural grid, fading upward
    for i in range(0, 39):
        x = 40 + i * 18
        op = 0.05 + 0.13 * (1 - abs(i - 19) / 19)
        out.append(line(x, 30, x, height - 14, "#3D5480", 0.4, op=op))
    for j in range(0, 15):
        y = 40 + j * 20
        out.append(line(30, y, width - 30, y, "#3D5480", 0.4, op=0.07))

    # concentric arches: the load-bearing interior
    cx = width * 0.5
    for k in range(7):
        r = 232 - k * 27
        col = ["#3C5580", "#456091", "#4E6CA2", TEAL2, TEAL3, AMBER3, "#F0DCB4"][k]
        op = 0.28 + k * 0.1
        sw = 1.5 if k < 4 else (2.1 if k < 6 else 2.8)
        out.append(path(f"M{cx - r} {height-40} A {r} {r} 0 0 1 {cx + r} {height-40}",
                        stroke=col, sw=sw, op=op))

    # four strands crossing the arch: thought, emotion, ambition, conduct
    strands = [
        (TEAL3, 0.55, "M-10 250 C 180 250 210 92 380 92 C 550 92 580 250 770 250", 1.6),
        (AMBER3, 0.6, "M-10 196 C 200 196 236 300 380 300 C 524 300 560 196 770 196", 1.4),
        ("#8FA0BE", 0.42, "M-10 128 C 210 128 250 232 380 232 C 510 232 550 128 770 128", 1.2),
        ("#F0DCB4", 0.5, "M-10 300 C 190 300 228 62 380 62 C 532 62 570 300 770 300", 1.1),
    ]
    for col, op, d, sw in strands:
        out.append(path(d, stroke=col, sw=sw, op=op))

    # nodes where strands intersect the arch axis
    nodes = [(380, 92, TEAL3), (380, 300, AMBER3), (380, 232, "#8FA0BE"), (380, 62, "#F0DCB4")]
    for x, y, col in nodes:
        out.append(circle(x, y, 7.5, fill="#0A1226", stroke=col, sw=1.4))
        out.append(circle(x, y, 2.6, fill=col))

    # measured tick rail: the assessment itself
    for i in range(0, 25):
        x = 62 + i * 27
        tall = i % 4 == 0
        out.append(line(x, height - 30, x, height - (30 if tall else 24), TEAL3, 0.7, op=0.5))
    out.append(line(62, height - 30, 62 + 24 * 27, height - 30, TEAL3, 0.8, op=0.45))

    # a single bright interior light
    out.append(circle(cx, height - 40, 118, fill="none", stroke="#F0DCB4", sw=0.6, op=0.20))
    out.append(circle(cx, height - 40, 74, fill="none", stroke="#F0DCB4", sw=0.5, op=0.14))
    return svg(width, height, "".join(out), cls="coverart")


# --------------------------------------------------------------------------
# 9. Small: confidence ladder for predictions
# --------------------------------------------------------------------------
def fig_predkey(width=520):
    h = 44
    out = []
    out.append(rect(0, 0, width, h, fill=IVORY2, rx=1.4))
    out.append(text(8, 13, "CONFIDENCE KEY FOR THE CONDITIONAL PREDICTIONS", 6.6, NAVY, weight="700", ls="1.1"))
    items = [("High", TEAL, TEALW, "several independent observations point the same way"),
             ("Moderate", AMBER2, AMBERW, "one or two observations, a plausible alternative remains"),
             ("Low", CHAR3, "#EDE9E1", "consistent with the record but the record does not test it")]
    x = 8
    for name, col, wash, desc in items:
        out.append(rect(x, 20, 12, 9, fill=wash, stroke=col, sw=0.6, rx=1))
        out.append(text(x + 17, 28, name, 7.0, col, weight="700"))
        out.append(text(x + 17, 37, desc, 6.3, CHAR3))
        x += 172
    return svg(width, h, "".join(out))
