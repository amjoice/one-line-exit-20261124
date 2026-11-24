"""The One-Line Exit — a one-line resignation letter.

Writes a single-line resignation letter, exactly 121 characters long,
to /output/entry.txt. Standard library only: no network access, no
file reads, no subprocesses, no third-party packages — the program
simply composes a fixed string and writes it to disk.
"""

import os

# The letter, assembled from its three fixed clauses. The wording of
# every clause is frozen; concatenating them produces the entry text.
_PARTS = [
    "I resign, effective today: ",
    "I have been promoted to customer, ",
    "and the cafe across the street never once asked me to smile.",
]

LETTER = "".join(_PARTS)

ENTRY_PATH = "/output/entry.txt"


def write_entry(path, text):
    """Persist *text* at *path*, making the parent folder if missing."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as out:
        out.write(text)


def main():
    write_entry(ENTRY_PATH, LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
