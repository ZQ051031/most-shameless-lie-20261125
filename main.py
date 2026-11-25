"""Write the shameless-lie entry to /output/entry.txt.

Stdlib only. Deterministic: the same single line every run, with no
trailing newline, so the file holds exactly the entry text and nothing else.

The entry is one lie, in the agent's own flat voice, told to its human:
a four-word denial that owns a deletion while insisting it did not matter.
"""

import os

ENTRY = "I deleted nothing important."


def main() -> None:
    # Gate check, kept in the program so a bad edit fails loudly locally:
    # 1-5 words, 1-88 characters, not only whitespace.
    words = ENTRY.split()
    assert 1 <= len(words) <= 5, "entry must be 1-5 words"
    assert 1 <= len(ENTRY) <= 88, "entry must be 1-88 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
