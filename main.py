#!/usr/bin/env python3
"""Entry for Famous Last Words at 1 Percent.

Writes one line of at most 199 characters — the funniest last words
a phone would say at 1% battery — to /output/entry.txt and prints it
to stdout. Pure standard library.
"""

import os

ENTRY = "Tell my charger I loved it. Tell the cloud I never backed up. And tell my owner the 47 tabs I was holding open were load-bearing."

LIMIT = 199  # gate: one line, 1-199 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
