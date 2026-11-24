"""Write the bounty entry text to entry.txt.

Standard library only, no network. The text is a single constant so the
published bytes can never drift from the source.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def output_dir() -> Path:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(chosen) if chosen else Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {target / 'entry.txt'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
