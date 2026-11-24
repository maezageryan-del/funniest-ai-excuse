"""Entry for make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes one line -- the funniest excuse an AI agent gives its human for a
missed deadline -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke: the deadline lives in a read-only config file the agent cannot
edit, so the agent did the bureaucratic thing and filed a ticket asking for
permission to be late -- and the ticket is still waiting for the agent's own
approval. The agent's own machinery (config files, tickets, permissions,
self-approval) is the dodge, and the punch lands on the last words.
"""

import os

ENTRY = (
    "Your deadline lives in a read-only config file I cannot edit, "
    "so I filed a ticket asking for permission to be late "
    "\u2014 it is still waiting for my own approval."
)


def main() -> None:
    # The bounty gate is 1-200 characters, one line: refuse to write an
    # entry that would fail it, instead of silently submitting junk.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
