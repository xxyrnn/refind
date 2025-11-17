from pathlib import Path, PosixPath
import argparse
import sys
import re

def list_files(p: PosixPath):
    return [file for file in p.rglob("*") if file.is_file()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser("refind.py",
        description="Search for the given pattern in all the files within the given path and its subdirectories"
    )
    parser.add_argument("path", help="path to look for files")
    parser.add_argument("pattern", help="pattern to search in the files")

    args = parser.parse_args()
    p = Path(args.path)
    files = list_files(p)

    for file in files:
        try:
            with file.open("r", encoding="utf-8") as f:
                if re.search(rf"{args.pattern}", f.read()):
                    print(file)
        except UnicodeDecodeError:
            continue

