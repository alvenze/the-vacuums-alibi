"""The Vacuum's Alibi - make.fun entry.

Writes one line, the excuse a robot vacuum gives for missing
a spot, to /output/entry.txt (UTF-8, 1 to 200 characters).
"""

import os

LINE = "That corner was not dirty. It was load-bearing dust, and I do not do structural work."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
