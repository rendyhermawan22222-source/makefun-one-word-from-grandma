#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word, the single word Rendy's Indonesian grandma
would text about AI, to /output/entry.txt, then reads it back and
verifies the file holds exactly that one word and nothing else.
"""

import os
import sys

WORD = "dukun"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Exactly the word, no trailing newline: 5 bytes, the smallest
    # text the tie-break can favour.
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(WORD)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()

    # Exactly one word: the file's bytes are the word itself, 1-30
    # characters, ASCII letters only, no whitespace at all.
    if raw != WORD.encode("ascii"):
        print(f"verification failed: entry.txt holds {raw!r}", file=sys.stderr)
        return 1
    if not (1 <= len(raw) <= 30) or not WORD.isalpha():
        print(f"verification failed: entry.txt holds {raw!r}", file=sys.stderr)
        return 1

    print(f"entry written and verified: {WORD!r} -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
