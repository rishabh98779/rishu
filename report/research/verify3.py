import json, urllib.parse, urllib.request, time
DOIS = [
 "10.1037/0033-2909.134.4.502",   # Moore & Healy overconfidence
 "10.1037/0022-3514.67.3.366",    # Buehler planning fallacy
 "10.1037/0022-3514.70.6.1327",   # Downey & Feldman rejection sensitivity
 "10.1348/014466504323088042",    # Gilbert et al self-criticism
 "10.1037/a0015421",              # Srivastava social costs of suppression
 "10.1037/0022-3514.88.6.895",    # Skitka moral conviction
 "10.1016/j.beth.2010.04.007",    # Bond AAQ-II
 "10.1037/0033-2909.94.1.33",     # Swann self-verification
 "10.1016/j.jocrd.2014.08.001",   # Radomsky intrusive thoughts normative
 "10.1007/s12671-019-01134-6",    # Ferrari self-compassion intervention meta
 "10.1037/0033-2909.126.2.247",   # Oyserman? (identity-based motivation is 2007 psych inquiry) - check
 "10.1080/10478400701512646",     # Oyserman & Destin identity-based motivation
 "10.1037/0003-066X.62.4.327",    # ? check
 "10.1146/annurev-psych-010418-102803", # ? check
 "10.1037/a0023311",              # ? check
 "10.1016/j.jrp.2011.08.006",     # ? check
 "10.1177/0146167211404209",      # ? check
 "10.1037/0022-3514.96.4.883",    # ? check
 "10.1037/pspi0000018",           # ? check
 "10.1111/j.1467-8721.2008.00599.x", # ? check
]
def get(doi, tries=3):
    for t in range(tries):
        url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
        req = urllib.request.Request(url, headers={"User-Agent":"personality-report/1.0 (mailto:research@example.org)"})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                m = json.load(r)["message"]
            au = m.get("author", [])
            return {"doi":doi,"ok":True,"title":(m.get("title") or [""])[0],
                    "container":(m.get("container-title") or [""])[0],"volume":m.get("volume"),
                    "issue":m.get("issue"),"page":m.get("page"),
                    "year":(m.get("issued",{}).get("date-parts",[[None]])[0][0]),
                    "authors":"; ".join(f"{a.get('family','')} {a.get('given','')[:1]}." for a in au[:4])}
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(3*(t+1)); continue
            return {"doi":doi,"ok":False,"err":f"HTTP {e.code}"}
        except Exception: time.sleep(2)
    return {"doi":doi,"ok":False,"err":"rate-limited"}
out=[]
for d in DOIS:
    r=get(d); out.append(r)
    print(("OK  " if r["ok"] else "FAIL"), d,"|",r.get("year"),"|",(r.get("authors") or "")[:50],"|",(r.get("title") or r.get("err",""))[:85], flush=True)
    time.sleep(0.6)
json.dump(out, open("/workspace/project/report/research/dois3.json","w"), indent=1)
