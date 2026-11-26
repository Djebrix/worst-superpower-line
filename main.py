#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes exactly one line (1-140 characters) inventing the most useless
superpower to entry.txt in the output directory.

The power sounds useful — summoning back anything lost — until its one
catch ruins it: it only works after a replacement has already been
bought, so the summoned object is never needed.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = "I can summon anything I've lost, but only after I've already bought a replacement."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
