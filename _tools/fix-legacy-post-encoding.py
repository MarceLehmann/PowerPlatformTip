#!/usr/bin/env python3
"""Repair legacy Power Automate posts: strip the UTF-8 BOM and fix double-encoded
(UTF-8 -> CP1252 -> UTF-8) mojibake.

Background
----------
Some older auto-published posts start with a UTF-8 BOM (0xEF 0xBB 0xBF) before
the YAML front matter and contain double-encoded emoji in headings, e.g. the
printer emoji rendered as "ð\u009f\u2013¨\u00ef\u00b8\u008f". Newer posts are
already clean, so the publishing flow itself appears fixed -- this is a one-off
cleanup for the historical files.

Safety
------
The repair is deliberately conservative. It only re-decodes maximal runs of
"high" characters (bytes >= 0x80 under a sloppy Windows-1252 mapping) when those
bytes form a valid UTF-8 multibyte sequence. As a result:
  * A double-encoded emoji run (several high bytes forming valid UTF-8) is fixed.
  * A lone legitimate en-dash / curly quote (a single high byte that is NOT valid
    standalone UTF-8) is left untouched.
  * An already-correct single-codepoint emoji cannot be sloppy-1252 encoded, so
    it is skipped -- clean posts are never modified.
The script is idempotent: running it twice makes no further changes.

Usage
-----
    python3 _tools/fix-legacy-post-encoding.py _posts            # dry run
    python3 _tools/fix-legacy-post-encoding.py _posts --write    # apply changes
    python3 _tools/fix-legacy-post-encoding.py path/to/one.md --write
"""
import sys
import os
import glob


def sloppy_byte(ch):
    """Return the single byte this character maps to under a 'sloppy'
    Windows-1252 encoding, or None if it cannot be represented in one byte."""
    cp = ord(ch)
    if cp < 0x100:
        return cp
    try:
        b = ch.encode("cp1252")
        return b[0] if len(b) == 1 else None
    except Exception:
        return None


def fix_mojibake(text):
    out = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        b = sloppy_byte(ch)
        if b is not None and b >= 0x80:
            j = i
            buf = bytearray()
            while j < n:
                bb = sloppy_byte(text[j])
                if bb is None or bb < 0x80:
                    break
                buf.append(bb)
                j += 1
            decoded = None
            try:
                cand = buf.decode("utf-8")
                # Only accept sensible results (no C0/C1 control chars).
                if all(ord(c) >= 0xA0 or c == "\t" for c in cand):
                    decoded = cand
            except UnicodeDecodeError:
                decoded = None
            if decoded is not None:
                out.append(decoded)
                i = j
                continue
        out.append(ch)
        i += 1
    return "".join(out)


def process(path, write):
    raw = open(path, "rb").read()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    if had_bom:
        raw = raw[3:]
    text = raw.decode("utf-8")
    fixed = fix_mojibake(text)
    changed_text = fixed != text
    if (had_bom or changed_text) and write:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(fixed)
    return had_bom, changed_text


def main(argv):
    write = "--write" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print("usage: fix-legacy-post-encoding.py <file-or-dir> [...] [--write]")
        return 2
    targets = []
    for a in args:
        if os.path.isdir(a):
            targets += glob.glob(os.path.join(a, "**", "*.md"), recursive=True)
        else:
            targets.append(a)
    n_bom = n_moj = 0
    for p in sorted(targets):
        bom, moj = process(p, write)
        if bom or moj:
            tag = "FIX" if write else "WOULD-FIX"
            print(f"{tag} {p}  bom={bom} mojibake={moj}")
            n_bom += bom
            n_moj += moj
    action = "fixed" if write else "would fix"
    print(f"--- {action}: BOM in {n_bom} file(s), mojibake in {n_moj} file(s); "
          f"scanned {len(targets)} file(s) ---")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
