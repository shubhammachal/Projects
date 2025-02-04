#!/usr/bin/env python3

import argparse
import sys

def count_lines(text):
    """Count the number of lines in the text."""
    return text.count('\n')

def count_words(text):
    """Count the number of words in the text."""
    return len(text.split())

def count_chars(text):
    """Count the number of characters in the text."""
    return len(text)

def count_bytes(text):
    """Count the number of bytes in the text (UTF-8 encoding)."""
    return len(text.encode('utf-8'))

def read_input(filename):
    """Read input from a file or standard input."""
    if filename:  # Read from file
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.", file=sys.stderr)
            sys.exit(1)
    else:  # Read from standard input
        return sys.stdin.read()

def main():
    """Parse arguments and execute the word count tool."""
    parser = argparse.ArgumentParser(description="Custom wc tool in Python")
    parser.add_argument("filename", nargs="?", help="File to process")
    parser.add_argument("-l", action="store_true", help="Count lines")
    parser.add_argument("-w", action="store_true", help="Count words")
    parser.add_argument("-m", action="store_true", help="Count characters")
    parser.add_argument("-c", action="store_true", help="Count bytes")

    args = parser.parse_args()

    # Read input (file or stdin)
    data = read_input(args.filename)

    # Compute requested counts
    results = []
    if args.l:
        results.append(str(count_lines(data)))
    if args.w:
        results.append(str(count_words(data)))
    if args.m:
        results.append(str(count_chars(data)))
    if args.c:
        results.append(str(count_bytes(data)))

    # Default behavior: count lines, words, and bytes if no options are provided
    if not (args.l or args.w or args.m or args.c):
        results = [str(count_lines(data)), str(count_words(data)), str(count_bytes(data))]

    # Print the result
    print(" ".join(results), args.filename if args.filename else "")

if __name__ == "__main__":
    main()
