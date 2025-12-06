import argparse
import re
import sys
from pathlib import Path


def list_files(p: Path):
    return [file for file in p.rglob("*") if file.is_file()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "refind.py",
        description="Search for the given pattern in all the files within the given path and its subdirectories",
    )
    parser.add_argument("path", help="directory to list for files")
    parser.add_argument("pattern", help="pattern to search in the files")

    args = parser.parse_args()
    p = Path(args.path)

    if p.is_file():
        sys.exit("[!] ERROR: path must be a directory")

    files = list_files(p)

    for file in files:
        try:
            with file.open("r", encoding="utf-8") as f:
                if re.search(rf"{args.pattern}", f.read()):
                    print(file)
        except UnicodeDecodeError:
            continue
