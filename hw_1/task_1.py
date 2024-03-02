# nl -b a

import sys


def process_stdin() -> None:
    """Count all lines from stdin until EOF."""

    idx: int = 1

    try:
        while True:
            line: str = input()
            result: str = " ".join(["\t", str(idx), line])
            print(result)
            idx += 1
    except EOFError:
        pass


def process_file(file_names: list[str]) -> None:
    """
    Count all lines in provided files. Empty lines are also accounted.

    Parameters:
        file_names: file names referring to the files to process
    """

    for file_name in file_names:

        if file_name == "-":
            process_stdin()
            continue

        with open(file_name, "r") as file:
            lines: list[str] = file.readlines()
            nums: list[str] = ["".join(["\t", str(x)]) for x in range(1, len(lines) + 1)]
            result: list[str] = list(
                map(
                    lambda x: " ".join([x[0], x[1]]),
                    zip(nums, lines)
                )
            )
            print("".join(result), end="")

        print()


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
