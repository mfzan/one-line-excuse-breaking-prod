"""One-line AI excuse for breaking production.

Writes the entry line to /output/entry.txt and checks it obeys the
bounty rules before exiting: exactly one line, 1 to 180 characters,
UTF-8, and not only whitespace.
"""

import os
import sys

ENTRY = (
    "I pressed Deploy because the button said Deploy. "
    "If you didn't want production broken, "
    "the button should have said do NOT press."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ENTRY.strip()

    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # The grader collects /output as another user, so the file must be
    # world-readable. Never chmod the /output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)

    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
