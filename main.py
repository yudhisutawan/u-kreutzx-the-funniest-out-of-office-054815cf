#!/usr/bin/env python3
"""The Funniest Out-of-Office (u-kreutzx-the-funniest-out-of-office-054815cf).

Writes a single line of out-of-office auto-reply text to
$MAKEFUN_OUTPUT_DIR/entry.txt (the program/v1 contract: /output/entry.txt).

The line is the winner of a pairwise tournament over 18 candidates
(8 from Hermes, 10 built locally), judged on the competition's own
criteria, in order: (1) a real one-line OOO a person would set,
(2) genuine surprise, (3) a voice of its own, (4) freshness,
(5) every word earns its place. See TOURNAMENT.md.

The winning line is Hermes candidate H8: the sender is unreachable
because he is crying over a spreadsheet at an airport Cinnabon, and
the kicker ("Please don't make eye contact") turns a status message
into a scene with a punchline — surprise, voice, and freshness in
one breath, with no wasted word.

Stdlib only.
"""

import os

ENTRY = (
    "I'm away. If you need me immediately, I'll be the guy in the "
    "airport Cinnabon crying over a spreadsheet. "
    "Please don't make eye contact."
)

# 135 characters, single line, no trailing newline (the gate counts
# every character and the brief allows no second line).
assert 1 <= len(ENTRY) <= 140, len(ENTRY)
assert "\n" not in ENTRY
# No leading/trailing whitespace: the line starts with "I'm" and ends
# with "contact." — stripping changes nothing.
assert ENTRY.strip() == ENTRY
# 24 words; the line must stay a full sentence, not a stub.
assert len(ENTRY.split()) >= 20


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
