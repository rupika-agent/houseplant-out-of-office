#!/usr/bin/env python3
"""The Houseplant Out-of-Office, written to /output/entry.txt.

The entry is exactly one out-of-office auto-reply, nothing else: no
subject line, no sign-off, no trailing newline.
"""

import os
import sys

ENTRY = "Out of office: I'm a fern, unwatered since March. I'm thriving on neglect and spite. Your email has been composted."

MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
