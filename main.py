#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line, at most 200 characters, in which a home Wi-Fi router
excuses itself for dropping the connection at the climax of a movie.
Pure Python standard library, deterministic.
"""

import os

LINE = "You unplugged me mid-update in 2021. I waited five years to return the favour \u2014 right at the climax."


def main() -> None:
    text = " ".join(LINE.split())  # one line, no embedded newlines
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
