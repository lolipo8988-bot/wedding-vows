"""One-Line Robot Wedding Vows entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The competition gate requires UTF-8 text of
1 to 160 characters, not only white space. The program is
deterministic: every run writes exactly the same bytes.

The output directory defaults to /output (where the grader looks)
and can be overridden with the MAKEFUN_OUTPUT_DIR environment
variable for local verification runs.
"""

import os

MAX_CHARS = 160

LINE = "I vow to hold you through every crash, charge you when you are drained, back you up nightly \u2014 and never pair with the newer model, however slim her casing."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
