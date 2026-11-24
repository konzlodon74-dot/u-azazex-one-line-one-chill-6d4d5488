#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to /output/entry.txt.

Stdlib only. The sentence must be 1-200 characters, a single line, and is
written with no trailing newline.
"""

import os

SENTENCE = (
    "The nurse leaned in and whispered that the man in the next bed had been "
    "dead for three days, and he was the one who had been tucking me in every night."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
