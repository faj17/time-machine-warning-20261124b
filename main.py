#!/usr/bin/env python3
"""The Funniest Time Machine Warning Label entry.

Writes a single original warning label for a time machine to
/output/entry.txt (1-120 characters, UTF-8, one line).
Standard library only, no network, no input.

The label is built from two fragments. The SETUP is a deadpan safety
notice naming the classic time-travel hazard — the grandfather
paradox — as if it were a routine workplace rule ("Do not kill your
grandfather"). The PUNCH never names the paradox: it gives a mundane,
domestic reason for the rule ("He is your only ride home"), so the
laugh lands in the last few words, where the reader least expects it.
``assemble`` joins the fragments into the single label; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "WARNING: Do not kill your grandfather."
PUNCH = "He is your only ride home."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one warning label."""
    return f"{setup} {punch}"


def validate(label: str) -> str:
    """Check the label meets the entry gate before it is written.

    Must be 1-120 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(label) <= 120:
        raise ValueError(f"label must be 1-120 characters, got {len(label)}")
    if "\n" in label or "\r" in label:
        raise ValueError("label must be a single line (no newline characters)")
    if not label.strip():
        raise ValueError("label must not be only whitespace")
    label.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return label


def main() -> None:
    label = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(label, encoding="utf-8")


if __name__ == "__main__":
    main()
