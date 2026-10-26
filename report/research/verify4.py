import json, urllib.parse, urllib.request, time
QUERIES = [
 ("Criticizing and reassuring oneself: An exploration of forms, styles and reasons in female students", "Gilbert self-criticism 2004"),
 ("Part of the Solution or Part of the Problem? A Critical Review of the Literature on Intrusive Thoughts", "normative intrusive thoughts review"),
 ("Intrusive thoughts in non-clinical participants", "Radomsky 2014 JOCRD"),
 ("The VIA Classification of Strengths and Virtues", "VIA classification"),
 ("Character strengths and their relation to happiness", "VIA strengths"),
 ("Sexual orientation, controversy, and science", "Bailey 2016"),
 ("Cognitive-behavioral therapy for social anxiety disorder", "social anxiety CBT"),
 ("Identity-based motivation", "Oyserman identity-based motivation"),
 ("Heterosexuals' attitudes toward transgender people", "trans attitudes"),
 ("Cognitive defusion", "defusion"),
 ("The structure of phenotypic personality traits", "Goldberg 1993"),
 ("An alternative 'description of personality': the Big-Five factor structure", "Goldberg 1990"),
 ("A five-factor theory of personality", "McCrae Costa 1999 five-factor theory"),
 ("Interpersonal complementarity", "complementarity"),
 ("Moral elevation", "elevation Haidt"),
 ("Embarrassment and social behavior", "embarrassment"),
 ("Moral identity and the experience of moral elevation", "moral identity elevation"),
 ("Reducing the gender achievement gap", "stereotype threat"),
 ("The norm of self-interest", "Miller 1999 norm of self-interest"),
 ("Uncertainty and the search for meaning", "meaning uncertainty"),
]
def q(title, label):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": title, "rows": 2})
    req = urllib.request.Request(url, headers={"User-Agent":"personality-report/1.0 (mailto:research@example.org)"})
    for t in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                items = json.load(r)["message"]["items"]
            break
        except Exception as e:
            items=None; time.sleep(2)
    if not items: return {"label":label,"ok":False}
    m = items[0]
    return {"label":label,"ok":True,"doi":m.get("DOI"),
            "title":(m.get("title") or [""])[0],"container":(m.get("container-title") or [""])[0],
            "year":(m.get("issued",{}).get("date-parts",[[None]])[0][0]),
            "volume":m.get("volume"),"issue":m.get("issue"),"page":m.get("page"),
            "authors":"; ".join(f"{a.get('family','')} {a.get('given','')[:1]}." for a in m.get("author",[])[:4])}
out=[]
for title,label in QUERIES:
    r=q(title,label); out.append(r)
    print(("OK  " if r.get("ok") else "FAIL"), r.get("doi"), "|", r.get("year"), "|", (r.get("authors") or "")[:48], "|", (r.get("title") or "")[:80], flush=True)
    time.sleep(0.6)
json.dump(out, open("/workspace/project/report/research/dois4.json","w"), indent=1)
