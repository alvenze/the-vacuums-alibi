"""The Vacuum's Alibi - make.fun entry.

Writes one line, the excuse a robot vacuum gives for missing
a spot, to /output/entry.txt (UTF-8, 1 to 200 characters).
"""

import os

LINE = "That corner was not dirty. It was load-bearing dust, and I do not do structural work."


def check_gate(text: str) -> None:
    """Enforce the bounty gate: 1 to 200 characters, not only whitespace."""
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "written entry does not match the intended line"
    check_gate(written)


if __name__ == "__main__":
    main()
