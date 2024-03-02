# wc (command)

import os
import sys


def process_stdin() -> (int, int, int):
    n_lines: int = 0
    n_words: int = 0
    n_bytes: int = 0

    try:
        while True:
            line: str = input()
            n_lines += 1
            n_words += len(line.strip().split())
            # +1 for \n character
            n_bytes += len(line) + 1

    except EOFError:
        name = "-" if len(sys.argv) > 1 else ""
        print("\t".join(["\t" + str(n_lines), str(n_words), str(n_bytes), name]))
        return n_lines, n_words, n_bytes


def process_file(file_names: list[str]) -> None:
    total_lines: int = 0
    total_words: int = 0
    total_bytes: int = 0

    for file_name in file_names:
        n_lines, n_words, n_bytes = 0, 0, 0

        if file_name == "-":
            result = process_stdin()
            total_lines += result[0]
            total_words += result[1]
            total_bytes += result[2]
            continue

        with open(file_name, "r") as file:
            content: list[str] = file.readlines()
            n_lines += len(content)
            n_words += sum([len(words) for words in [line.split() for line in content]])
            n_bytes += os.path.getsize(file_name)

            print("\t".join(["\t" + str(n_lines), str(n_words), str(n_bytes), file_name]))

        total_lines += n_lines
        total_words += n_words
        total_bytes += n_bytes

    if len(file_names) > 1:
        print("\t".join(["\t" + str(total_lines), str(total_words), str(total_bytes), "total"]))


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0 or args[0].strip() == "-":
        try:
            process_stdin()
        # SIGTERM handler
        except KeyboardInterrupt:
            pass
    else:
        try:
            process_file(args)
        except FileNotFoundError as not_file:
            print(" ".join(["Could not open file:", not_file.filename]))
