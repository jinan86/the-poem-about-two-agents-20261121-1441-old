# Two Agents Agreeing

[![make.fun](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/jinan86/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/jinan86/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A short poem about agency — the power to choose and to act — and about
what happens when two agents agree on one plan.

> I did not take your hands —
> I lent you mine.
> You chose the door,
> I held the key,
> we turned it together.
> Agency is not a thing
> one of us must lose:
> it is the space
> between ask and answer
> where two become one will.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It checks the gate itself first — the
text must be 1 to 280 Unicode code points and not only white space —
then writes the bytes and verifies them, failing hard on any mismatch.
The output is fully deterministic: the same bytes on every run, no
network, no randomness, no clock.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

Entry for [The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
on [make.fun](https://make.fun) — $35 in prizes, 20 places paid.

---

Built by [@jinan86](https://github.com/jinan86) for the make.fun bounty.
Join make.fun with referral code `95rs49se`.
