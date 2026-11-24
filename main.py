"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Revision note: re-checked entry after local run (no code change).
"""

# The entry text is a one-line warning label for a time machine, 71
# characters — inside the 120-character gate. It turns the classic
# time-travel hazard (meeting your own past self) into the joke, keeps
# a straight safety-notice face, and saves the punchline for the last
# few words, as the judge brief asks.
import os

TEXT = "WARNING: Never meet your past self. He owes you money, and he knows it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
