"""One-line laugh entry.

Writes a single funny sentence to ``entry.txt`` inside the output
directory named by the ``MAKEFUN_OUTPUT_DIR`` environment variable
(``/output`` when the variable is not set).
"""

import os
import sys

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 200

JOKE_LINE = (
    "I finally cleaned my inbox to zero, "
    "and Gmail sent me a congratulations email."
)


def output_path() -> str:
    """Return the full path of the file the line will be written to."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(directory, OUTPUT_FILENAME)


def write_line(line: str) -> str:
    """Validate the line and write it with no trailing newline.

    Returns the path that was written to.
    """
    if not line or len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"line must be between 1 and {MAX_LINE_LENGTH} characters long, "
            f"but it is {len(line)} characters; "
            "shorten the joke to a single sentence before submitting"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain any newline characters")

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write with newline="" so Python adds no line ending of its own;
    # the entry must be exactly one line with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return path


def main() -> int:
    try:
        path = write_line(JOKE_LINE)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE_LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
