#!/usr/bin/env python

import os
import sys

VERSION = "1.0"


def print_help():
    help_text = """
Usage: wc.py [OPTION]... [FILE]...
Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.
The options below may be used to select which counts are printed, always in the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
  -w, --words            print the word counts
  -L, --max-line-length  print the length of the longest line
      --help     display this help and exit
      --version  output version information and exit
"""
    print(help_text)


def print_version():
    print(f"wc.py version {VERSION}")


def count_bytes(file_path):
    with open(file_path, "rb") as f:
        return len(f.read())


def count_chars(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.read())


def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f.readlines())


def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return len(f.read().replace("\n", " ").split(" "))


def max_line_length(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return max(len(line) for line in lines)


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    option = sys.argv[1]
    if option in ("--help", "-h"):
        print_help()
        sys.exit(0)
    elif option == "--version":
        print_version()
        sys.exit(0)

    if len(sys.argv) < 3:
        print("wc.py: missing file operand")
        sys.exit(1)

    file_path = sys.argv[2]
    if not os.path.isfile(file_path):
        print(f"wc.py: {file_path}: No such file")
        sys.exit(1)

    if option in ("-c", "--bytes"):
        print(f"{count_bytes(file_path)} {file_path}")
    elif option in ("-m", "--chars"):
        print(f"{count_chars(file_path)} {file_path}")
    elif option in ("-l", "--lines"):
        print(f"{count_lines(file_path)} {file_path}")
    elif option in ("-w", "--words"):
        print(f"{count_words(file_path)} {file_path}")
    elif option in ("-L", "--max-line-length"):
        print(f"{max_line_length(file_path)} {file_path}")
    else:
        print(f"wc.py: invalid option -- '{option}'")
        print("Try 'wc.py --help' for more information.")
        sys.exit(1)


if __name__ == "__main__":
    main()
