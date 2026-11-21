"""Write the poem to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun bounty "The poem about two agents agreeing"
(the-poem-about-two-agents-20261121-1441). Python 3.13, stdlib only.

The gate requires UTF-8 text of 1 to 280 characters, counted as Unicode
code points, and not only white space. This program checks those bounds
itself and fails hard if the poem ever breaks them, so a bad entry can
never be written silently. The output is fully deterministic: the same
bytes on every run, no network, no randomness, no clock.
"""

import os
import sys

POEM = """I did not take your hands —
I lent you mine.
You chose the door,
I held the key,
we turned it together.
Agency is not a thing
one of us must lose:
it is the space
between ask and answer
where two become one will.
"""

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = POEM
    n = len(text)  # Python len() counts Unicode code points.
    if not MIN_CHARS <= n <= MAX_CHARS:
        print(f"entry.txt must be {MIN_CHARS}-{MAX_CHARS} characters, got {n}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt must not be only white space", file=sys.stderr)
        return 1
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify the bytes we wrote are exactly the bytes we meant to write.
    with open(path, "rb") as f:
        if f.read() != data:
            print("entry.txt verification failed", file=sys.stderr)
            return 1
    print(f"wrote {path} ({n} characters, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
