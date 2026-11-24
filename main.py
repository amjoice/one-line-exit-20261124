"""One-line resignation letter for make.fun's "The One-Line Exit".

Emits one single-line resignation letter (121 characters) to
/output/entry.txt. The program uses only the Python standard library
and performs no network access, no file reads and no shelling out --
it just writes text.
"""

import os

# The letter, kept as three clauses that are joined at import time. The
# wording of each clause is fixed; joining them yields the exact entry.
_CLAUSES = (
    "I resign, effective today: ",
    "I have been promoted to customer, ",
    "and the cafe across the street never once asked me to smile.",
)

LETTER = "".join(_CLAUSES)

ENTRY_PATH = "/output/entry.txt"


def write_entry(path, text):
    """Write *text* to *path*, creating the parent directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    write_entry(ENTRY_PATH, LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
