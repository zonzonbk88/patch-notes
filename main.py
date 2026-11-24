#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny one-line patch note for a bug in real life /
human biology to /output/entry.txt (1-160 chars, single line).
Standard library only.
"""

import os

ENTRY = (
    "v3.2.0: Fixed a bug where crossing a doorway wiped the reason you "
    "entered the room. Standing in the doorway does not restore it."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("PATCH_NOTES_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
