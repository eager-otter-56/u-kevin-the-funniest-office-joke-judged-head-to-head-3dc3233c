#!/usr/bin/env python3
"""Entry program for "The Funniest Office Joke, Judged Head to Head".

Writes one office joke, a single line, to entry.txt in MAKEFUN_OUTPUT_DIR.
Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

ENTRY_TEXT = (
    # The removal request is the mechanism: asking 214 people to be taken
    # off the thread is itself a reply-all, and 37 of them copy it.
    "I hit reply-all to 214 people to ask to be removed from this thread, "
    "and 37 of them replied-all to ask the same thing."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, non-whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 200, len(ENTRY_TEXT)
    assert ENTRY_TEXT.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
