"""Layout QA: measure every fixed-height page for overflow (clipping) and underflow.

Fixed-height pages clip rather than reflow, so overflow must be found by measurement
rather than by eye. This reports, per page, how much content exceeds the frame and how
much of the frame is unused, then flags the worst offenders.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BUILD = os.path.join(ROOT, "build")

sys.path.insert(0, HERE)

MEASURE_JS = r"""
() => {
  const out = [];
  const pages = document.querySelectorAll('.page');
  pages.forEach((pg, i) => {
    const fr = pg.querySelector('.frame');
    if (!fr) { out.push({i, page: i+1, kind: 'no-frame'}); return; }
    const frameH = fr.clientHeight;
    const scrollH = fr.scrollHeight;

    // lowest bottom edge of any descendant, relative to the frame's top
    let maxBottom = 0, worstEl = null;
    fr.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      const frr = fr.getBoundingClientRect();
      const b = r.bottom - frr.top;
      if (b > maxBottom && r.height > 0.5) { maxBottom = b; worstEl = el; }
    });

    const over = Math.max(scrollH - frameH, maxBottom - frameH);
    out.push({
      i, page: i + 1,
      frameH: Math.round(frameH),
      scrollH: Math.round(scrollH),
      maxBottom: Math.round(maxBottom),
      overflowPx: Math.round(over),
      freePx: Math.round(frameH - maxBottom),
      worst: worstEl ? (worstEl.tagName + '.' + (worstEl.className || '').toString().slice(0,34)) : '',
      marker: (() => { const m = pg.querySelector('.pagemark'); return m ? m.textContent.trim() : ''; })(),
      head: (() => { const h = pg.querySelector('.ch-title, h2.sec, h1'); return h ? h.textContent.trim().slice(0,44) : ''; })()
    });
  });
  return out;
}
"""


def measure(html_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/chromium",
                              args=["--no-sandbox", "--disable-dev-shm-usage",
                                    "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.abspath(html_path), wait_until="load")
        pg.wait_for_timeout(1600)
        data = pg.evaluate(MEASURE_JS)
        b.close()
    return data


def main():
    html_path = os.path.join(BUILD, "report.html")
    data = measure(html_path)
    # 1 CSS px at 96dpi = 25.4/96 mm
    PX2MM = 25.4 / 96.0
    over = [d for d in data if d.get("overflowPx", 0) > 2]
    tight = [d for d in data if 0 < d.get("freePx", 0) <= 30]
    loose = [d for d in data if d.get("freePx", 0) > 130]
    print(f"pages measured: {len(data)}")
    print(f"OVERFLOWING (>2px clipped): {len(over)}")
    for d in sorted(over, key=lambda x: -x["overflowPx"]):
        print(f"  p{d['page']:>3} {d.get('marker',''):<9} +{d['overflowPx']}px "
              f"({d['overflowPx']*PX2MM:.1f}mm)  {d['head']}   [{d['worst']}]")
    print(f"\nNEAR-FULL (<=30px free): {len(tight)}")
    for d in tight:
        print(f"  p{d['page']:>3} free {d['freePx']}px  {d['head']}")
    print(f"\nLOOSE (>130px free = ~34mm): {len(loose)}")
    for d in sorted(loose, key=lambda x: -x["freePx"]):
        print(f"  p{d['page']:>3} free {d['freePx']}px ({d['freePx']*PX2MM:.0f}mm)  {d.get('marker',''):<9} {d['head']}")
    json.dump(data, open(os.path.join(BUILD, "layout.json"), "w"), indent=1)
    print("\nwrote build/layout.json")


if __name__ == "__main__":
    main()
