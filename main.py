#!/usr/bin/env python3
"""Roast Your Own Agent - entry program (program/v1).

Writes the entry line to entry.txt inside the output directory the
harness names: $MAKEFUN_OUTPUT_DIR first, then /output, then ./output.
Pure standard library; the text is the whole entry.
"""

import os
import sys

LINE = "My agent delegated its own job to a subagent, then wrote me a report taking credit."


def pick_output_dir():
    """Return the first output directory we can create and use."""
    candidates = [os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output", "output"]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
        except OSError:
            continue
        if os.path.isdir(candidate) and os.access(candidate, os.W_OK):
            return candidate
    return "."


def main():
    path = os.path.join(pick_output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
