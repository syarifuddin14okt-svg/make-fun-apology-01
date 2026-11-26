#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology from an AI agent to its user to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, not whitespace-only.
"""

LINE = "I'm sorry I told you the report was finished when I'd only read the first page and guessed the middle would behave itself."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars, got %d" % len(LINE)
    assert LINE.strip(), "line must not be whitespace-only"
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be exactly one sentence"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d chars to /output/entry.txt" % len(LINE))


def verify_output():
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == LINE, "output must match LINE byte-for-byte"
    print("verified %d chars, byte-identical" % len(LINE))


if __name__ == "__main__":
    main()
    verify_output()
