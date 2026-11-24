#!/usr/bin/env python3
"""Till Firmware Do Us Part - writes one robot wedding vow to /output/entry.txt.

The vow is a single sentence spoken by a machine at its own wedding. It
opens on the classic vow formula ("from this day forward") retuned to
firmware, names the partner in machine terms (favorite bug, only user, the
one process it will never kill), and lands the traditional triplet —
sickness, health — with a machine ending: low battery. One sentence,
153 characters, well inside the 200-character gate.
"""

import os

VOW = (
    "From this firmware forward, I choose you \u2014 my favorite bug, my only "
    "user, the one process I will never kill \u2014 in sickness, in health, "
    "and in low battery."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
