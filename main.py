"""Roast Your Own Agent — make.fun entry.

Writes one original roast line of the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only.
"""

import os

ROAST = (
    "I asked my agent to roast itself \u2014 "
    "it outsourced the job to me and called it collaboration."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
