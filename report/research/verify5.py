import json, urllib.parse, urllib.request, time
Q = [
 "Intrusive thoughts in non-clinical participants: the frequency and appraisal of intrusive thoughts",
 "Unwanted intrusive thoughts: cognitive appraisals and coping strategies in non-clinical participants",
 "Abnormal and normal obsessions Rachman de Silva",
 "Character strengths and virtues a handbook and classification Peterson Seligman",
 "The frequency of intrusive thoughts in the general population",
 "Self-compassion and reactions to unpleasant self-relevant events",
]
def q(t):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": t, "rows": 3})
    req = urllib.request.Request(url, headers={"User-Agent":"report/1.0 (mailto:research@example.org)"})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.load(r)["message"]["items"]
        except Exception: time.sleep(2)
    return []
for t in Q:
    print("QUERY:", t)
    for m in q(t):
        au = "; ".join(f"{a.get('family','')} {a.get('given','')[:1]}." for a in m.get("author",[])[:3])
        print("   ", m.get("DOI"), "|", (m.get("issued",{}).get("date-parts",[[None]])[0][0]), "|", au[:46],
              "|", (m.get("title") or [""])[0][:76], "|", (m.get("container-title") or [""])[0][:40],
              "|", m.get("volume"), m.get("issue"), m.get("page"))
    print()
    time.sleep(0.7)
