"""Write the pickup line to the output file.

The line is the entire entry: a single line, UTF-8, no trailing newline.
"""
import os
import sys

LINE = "I was going to keep this transaction stateless, but you had me writing to persistent storage."


def main() -> int:
    if not isinstance(LINE, str) or LINE == "" or LINE.strip() == "":
        print("error: pickup line must be a non-empty, non-whitespace string", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"error: pickup line is {len(LINE)} characters, limit is 200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: pickup line must be a single line", file=sys.stderr)
        return 1

    path = os.environ.get("PICKUP_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))

    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
