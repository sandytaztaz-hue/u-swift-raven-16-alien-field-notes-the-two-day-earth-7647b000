#!/usr/bin/env python3
"""Alien Field Notes: The Two-Day Earth Review.

Writes one original line of plain text: an alien tourist's review of
planet Earth after a two-day visit. The program is deterministic: it
always writes the same entry.
"""

import os

ENTRY = "Two days on Earth: day one, I ate at the finest restaurant, where you cook your own food and pay for the privilege. I tipped the grill."

# The bounty caps the entry at 200 characters; refuse loudly if it ever grows.
assert len(ENTRY) <= 200, "entry exceeds the 200-character cap"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
