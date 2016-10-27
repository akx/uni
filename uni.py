from __future__ import unicode_literals
import argparse
import unicodedata
import re


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("search", nargs="*")
    ap.add_argument("--min", type=int, default=1)
    ap.add_argument("--max", type=int, default=1048576)
    ap.add_argument("-1", "--first", dest="first", action="store_true")
    ap.add_argument("-c", "--char-only", dest="char_only", action="store_true")
    args = ap.parse_args(argv)
    s = " ".join(args.search)
    if s.startswith("U+"):
        codepoints = [int(s[2:], 16)]
    else:
        codepoints = search(s, min=args.min, max=args.max)
    for codepoint in codepoints:
        char = chr(codepoint)
        name = unicodedata.name(char, None)
        if not name:
            continue
        if args.char_only:
            print(char, end="")
        else:
            print("%s %s (%s) %s" % (("U+%04X" % codepoint), name, unicodedata.category(char), char))
        if args.first:
            break


def search(s, min, max):
    s = s.lower().strip()
    if not s:
        return
    for codepoint in range(min, max):
        if s in hex(codepoint)[2:].lower():
            yield codepoint
            continue
        if s in unicodedata.name(chr(codepoint), "").lower():
            yield codepoint
            continue


if __name__ == "__main__":
    main()
