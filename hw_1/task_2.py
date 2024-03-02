# tail

import sys
from typing import Final
from collections import deque

_STDIN_TAIL_SIZE: Final[int] = 17
_FILE_TAIL_SIZE: Final[int] = 10


def process_stdin() -> None:
    """
    Read stdin and print out the last several lines after EOF is reached.

    Note:
        Number of lines to output is determined by _STDIN_TAIL_SIZE.
    """

    deq: deque[str] = deque()

    try:
        while True:
            line: str = input()

            if len(deq) == _STDIN_TAIL_SIZE:
                deq.popleft()

            deq.append(line)

    except EOFError:
        for elem in deq:
            print(elem)


def process_file(file_names: list[str]) -> None:
    """
    Print out the last several lines of the provided files.

    Note:
        Number of lines to output is determined by _STDIN_TAIL_SIZE.

    Parameters:
        file_names: file names referring to the files to process
    """

    for file_name in file_names:

        if len(file_names) > 1:
            print(" ".join(["==>", file_name, "<=="]))

        if file_name == "-":
            process_stdin()
            continue

        with open(file_name, "r") as file:
            lines = file.readlines()

            if len(lines) < _FILE_TAIL_SIZE:
                print("".join(lines))
                continue

            print("".join(lines[len(lines)-_FILE_TAIL_SIZE+1:]))


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == "-":
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
