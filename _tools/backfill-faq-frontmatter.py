#!/usr/bin/env python3
"""Backfill FAQPage-ready faq: front matter from a visible "## FAQ" block.

Many posts render a human-readable FAQ section (a heading containing the word
FAQ, followed by bold questions and answer paragraphs) but do not expose it as
structured data. The include _includes/schema-faq.html emits FAQPage JSON-LD
from a faq: front-matter list, so this tool parses the visible FAQ and fills
that list in - making posts eligible for FAQ rich results and easier for LLMs
to quote.

Supported question formats (any bold line ending in "?"):
    **Q1: ...?**   **Q: ...?**   **1. ...?**   **...?**
Answer = the paragraph(s) between a question and the next question / heading.

Safe and idempotent:
  * Skips posts that already define faq:.
  * Skips redirect stubs (sitemap: false or redirect_to).
  * Skips posts with no FAQ heading or no parseable pairs.
  * Only inserts a faq: block into the YAML front matter; body is unchanged.
  * Emits YAML via PyYAML, so quoting/escaping is always valid.
  * Strips horizontal rules and leading Q1:/1. enumerators from the text.

Usage:
    python3 _tools/backfill-faq-frontmatter.py _posts
    python3 _tools/backfill-faq-frontmatter.py _posts --write
"""
import sys, os, glob, re
import yaml

FAQ_HEADING = re.compile(r"^\s{0,3}#{2,3}\s+.*\bFAQ\b", re.IGNORECASE)
ANY_HEADING = re.compile(r"^\s{0,3}#{2,3}\s+")
BOLD_Q = re.compile(r"^\s*\*\*(.+?)\*\*\s*$")
HR = re.compile(r"^\s*([-*_])\1{2,}\s*$")
ENUM = re.compile(r"^(?:Q\s*\d*|\d+)\s*[:.\)]\s+", re.IGNORECASE)


def split_front_matter(text):
    if not text.startswith("---"):
        return None, None, None
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not m:
        return None, None, None
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(1), text[m.end():]


def parse_faq(body):
    lines = body.split("\n")
    n = len(lines)
    start = None
    for i in range(n):
        if FAQ_HEADING.match(lines[i]):
            start = i + 1
            break
    if start is None:
        return []
    end = n
    for j in range(start, n):
        if ANY_HEADING.match(lines[j]):
            end = j
            break
    pairs = []
    q = None
    ans = []

    def flush():
        if q is not None:
            a = " ".join(" ".join(ans).split()).strip()
            if a:
                pairs.append((q, a))

    for k in range(start, end):
        line = lines[k]
        mm = BOLD_Q.match(line)
        if mm and mm.group(1).rstrip().endswith("?"):
            flush()
            q = ENUM.sub("", mm.group(1).strip()).strip()
            ans = []
        elif q is not None:
            if HR.match(line):
                continue
            ans.append(line)
    flush()
    return pairs


def dump_faq_block(pairs):
    data = {"faq": [{"question": q, "answer": a} for q, a in pairs]}
    block = yaml.safe_dump(data, allow_unicode=True, sort_keys=False,
                           default_flow_style=False, width=100000)
    return block.rstrip("\n") + "\n"


def process(path, write):
    text = open(path, encoding="utf-8").read()
    fm, fm_raw, body = split_front_matter(text)
    if fm is None:
        return "no-frontmatter"
    if "faq" in fm:
        return "has-faq"
    if fm.get("sitemap") is False or "redirect_to" in fm:
        return "redirect"
    pairs = parse_faq(body)
    if not pairs:
        return "no-faq"
    new_text = "---\n" + fm_raw.rstrip("\n") + "\n" + dump_faq_block(pairs) + "---\n" + body
    if write:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_text)
    return "faq+%d" % len(pairs)


def main(argv):
    write = "--write" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print("usage: backfill-faq-frontmatter.py <file-or-dir> [...] [--write]")
        return 2
    targets = []
    for a in args:
        if os.path.isdir(a):
            targets += glob.glob(os.path.join(a, "**", "*.md"), recursive=True)
        else:
            targets.append(a)
    counts = {}
    for p in sorted(targets):
        r = process(p, write)
        counts[r] = counts.get(r, 0) + 1
        if r.startswith("faq+"):
            print(("FIX " if write else "WOULD-FIX ") + p + "  " + r)
    print("--- summary:", dict(sorted(counts.items())), "scanned", len(targets), "---")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
