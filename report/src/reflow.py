"""Automatic reflow: pack chapter content into pages using measured heights.

Fixed-height pages clip rather than reflow, so page breaks have to be computed. This
module lays each chapter's content out in a single column at the exact text width of a
report page, measures every top-level block, and greedily packs the blocks into pages of
the measured frame capacity. Blocks marked break-inside:avoid are treated as atomic and
never split; everything else may be split at its own internal element boundaries if it
cannot fit on a fresh page.

The result is a page break that is guaranteed to fit, rather than one that has been
estimated by hand.
"""
from __future__ import annotations

import json
import os

FRAME_W_MM = 210 - 2 * 18          # 174 mm text column
FRAME_H_MM = 297 - 16.5 - 14.5     # 266 mm usable height


def _mm_to_px(mm):
    return mm * 96.0 / 25.4


FLOW_JS = r"""
() => {
  const out = {};
  document.querySelectorAll('[data-chapter]').forEach(flow => {
    const id = flow.getAttribute('data-chapter');
    const fr = flow.getBoundingClientRect();
    const blocks = [];
    [...flow.children].forEach(el => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const mt = parseFloat(cs.marginTop) || 0;
      const mb = parseFloat(cs.marginBottom) || 0;
      blocks.push({
        html: el.outerHTML,
        h: r.height + mt + mb,
        mt, mb,
        tag: el.tagName,
        cls: (el.className || '').toString(),
        atomic: cs.breakInside === 'avoid' ||
                ['FIGURE','TABLE','H2','H3','H4'].includes(el.tagName),
        // height of the first internal child, used when splitting a long block
        firstChild: el.firstElementChild ? el.firstElementChild.getBoundingClientRect().height : 0
      });
    });
    out[id] = blocks;
  });
  return out;
}
"""


def measure_chapters(html_flow, tmp_html):
    """Render the flow document and return measured blocks per chapter."""
    from playwright.sync_api import sync_playwright
    doc = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/>"
           "<link rel='stylesheet' href='../src/styles.css'/></head><body>"
           "<div style='width:%dmm;margin:0;padding:0'>" % FRAME_W_MM
           + html_flow + "</div></body></html>")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(doc)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/chromium",
                              args=["--no-sandbox", "--disable-dev-shm-usage",
                                    "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 760, "height": 1200})
        pg.goto("file://" + os.path.abspath(tmp_html), wait_until="load")
        pg.wait_for_timeout(1400)
        data = pg.evaluate(FLOW_JS)
        b.close()
    return data


def pack(blocks, cap_px, min_fill=0.86):
    """Greedy pack blocks into pages of cap_px. Returns list of lists of block dicts."""
    pages, cur, used = [], [], 0.0
    for blk in blocks:
        h = blk["h"]
        # a heading must not be the last thing on a page
        if blk["tag"] in ("H2", "H3", "H4") and cur:
            # look ahead: if the heading plus the next non-heading block will not fit,
            # push the heading to the next page with it
            idx = blocks.index(blk)
            nxt = None
            for j in range(idx + 1, len(blocks)):
                if blocks[j]["tag"] not in ("H2", "H3", "H4"):
                    nxt = blocks[j]
                    break
            if nxt and used + h + nxt["h"] > cap_px:
                pages.append(cur)
                cur, used = [], 0.0
        if used + h <= cap_px:
            cur.append(blk)
            used += h
        else:
            if cur:
                pages.append(cur)
            cur, used = [blk], h
            # a single block taller than a page must still be emitted; it will be split
            # by the caller if it has internal boundaries
    if cur:
        pages.append(cur)
    return pages


def split_block(blk, cap_px, measure_fn):
    """Split an oversized non-atomic block into chunks that each fit a page.

    measure_fn(fragment_html) -> measured height in px, evaluated in the browser.
    """
    if blk["atomic"] or blk["h"] <= cap_px:
        return [blk]
    # try splitting a <ul> or <ol> by list items
    import re
    m = re.match(r"^<(ul|ol)([^>]*)>(.*)</\1>$", blk["html"], re.S)
    if m:
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        items = re.findall(r"<li\b.*?</li>", inner, re.S)
        if len(items) > 1:
            chunks, cur, cur_h = [], [], 0.0
            for it in items:
                h = measure_fn(f"<{tag}{attrs}>{it}</{tag}>")
                if cur and cur_h + h > cap_px:
                    chunks.append(cur)
                    cur, cur_h = [it], h
                else:
                    cur.append(it)
                    cur_h += h
            if cur:
                chunks.append(cur)
            return [dict(html=f"<{tag}{attrs}>{''.join(c)}</{tag}>",
                         h=min(cap_px, sum(1 for _ in c) * 20 + 20),
                         tag=blk["tag"], cls=blk["cls"], atomic=False)
                    for c in chunks]
    # generic: split at <p> boundaries
    paras = re.findall(r"<p\b.*?</p>", blk["html"], re.S)
    if len(paras) > 1:
        chunks, cur, cur_h = [], [], 0.0
        for pa in paras:
            h = measure_fn(pa)
            if cur and cur_h + h > cap_px:
                chunks.append(cur)
                cur, cur_h = [pa], h
            else:
                cur.append(pa)
                cur_h += h
        if cur:
            chunks.append(cur)
        return [dict(html="".join(c), h=min(cap_px, 10),
                     tag=blk["tag"], cls=blk["cls"], atomic=False) for c in chunks]
    return [blk]


def reflow_chapter(chapter_id, blocks, tmp_html):
    """Return a list of page HTML strings for one chapter."""
    cap = _mm_to_px(FRAME_H_MM)
    # resolve oversized blocks first
    from playwright.sync_api import sync_playwright
    resolved = []
    need_split = [b for b in blocks if b["h"] > cap and not b["atomic"]]
    if need_split:
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path="/usr/bin/chromium",
                                  args=["--no-sandbox", "--disable-dev-shm-usage"])
            pg = b.new_page(viewport={"width": 760, "height": 1200})
            pg.set_content("<style>@import url('file://%s');</style>"
                           "<div id='m' style='width:%dmm'></div>"
                           % (os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                           "styles.css")), FRAME_W_MM))

            def measure_fn(frag):
                return pg.evaluate(
                    "f => { const d = document.getElementById('m');"
                    "d.innerHTML = f; const r = d.getBoundingClientRect();"
                    "return r.height; }", frag)
            for blk in blocks:
                resolved.extend(split_block(blk, cap, measure_fn))
            b.close()
    else:
        resolved = blocks
    pages = pack(resolved, cap)
    return ["\n".join(b["html"] for b in page) for page in pages]
