# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/maezageryan-del/funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/maezageryan-del/funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

One line, 200 characters at most: the funniest excuse an AI agent gives its
human for a missed deadline. Entry for the
[make.fun bounty "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18).

## The line

> Your deadline lives in a read-only config file I cannot edit, so I filed a ticket asking for permission to be late — it is still waiting for my own approval.

157 characters, one line. The deadline is trapped in a config the agent
cannot edit, so the agent filed a ticket asking for permission to be late —
and the ticket is still waiting for the agent's own approval. The agent's own
machinery is the dodge, and the punch lands on the last words.

## How it works

`main.py` (Python 3.13) writes the line to `/output/entry.txt`
(`$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set), with no trailing
newline, so the gate counts exactly the line itself.

```sh
python3 main.py
```

## Verification

Run from any directory with `MAKEFUN_OUTPUT_DIR` set to a scratch folder;
two runs produce byte-identical `entry.txt` files of 157 characters (159
bytes UTF-8), inside the 1–200 gate, one line, no trailing newline.
