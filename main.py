#!/usr/bin/env python3
"""Entry program for the make.fun bounty "The Funniest Sick-Day Excuse".

Writes the single entry line (one line, under 200 characters) to
/output/entry.txt and nothing else. Dependency-free, stdlib only.
"""

import os

LINE = "Won't be in today: my cat walked across my keyboard and accepted a meeting with the CEO, so I'm legally in two places at once."


def main():
    # Ensure the output directory exists before writing the entry line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
