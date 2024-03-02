# task_1 artifacts

```commandline
$ python3 task_1.py resources/kek 
        1 Вам нужно реализовать CLI приложения, кроме кода, вам необходимо в качестве артефактов приложить текстовый файл, как вы проверяли работоспособность вашего кода (просто копия команд и выводов из терминала)
        2 
        3 1.1
        4 Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
        5 Если файл не передан, то скрипт читает строки из `stdin`.
        6 
        7 Он должен работать так же, как `nl -b a`.
```

```commandline
$ python3 task_1.py resources/empty
        1 
        2 
        3 
        4 
        5 \n
        6 
        7 \t\n
        8 
```

```commandline
$ python3 task_1.py task_1.py 
        1 # nl -b a
        2 
        3 import sys
        4 
        5 
        6 def process_stdin(idx: int = None) -> int:
        7     """
        8     Count all lines from stdin until EOF.
        9 
        10     Parameters:
        11         idx: index from which should start counting
        12 
        13     Return:
        14         Index on which stopped counting
        15     """
        16 
        17     idx: int = idx if idx is not None else 1
        18 
        19     try:
        20         while True:
        21             line: str = input()
        22             result: str = " ".join(["\t", str(idx), line])
        23             print(result)
        24             idx += 1
        25     except EOFError:
        26         return idx
        27 
        28 
        29 def process_file(file_names: list[str]) -> None:
        30     """
        31     Count all lines in provided files. Empty lines are also accounted.
        32 
        33     Parameters:
        34         file_names: file names referring to the files to process
        35     """
        36 
        37     idx: int = 1
        38 
        39     for file_name in file_names:
        40 
        41         if file_name == "-":
        42             idx = process_stdin(idx)
        43             continue
        44 
        45         with open(file_name, "r") as file:
        46             lines: list[str] = file.readlines()
        47             nums: list[str] = ["".join(["\t", str(x)]) for x in range(idx, idx + len(lines) + 1)]
        48             result: list[str] = list(
        49                 map(
        50                     lambda x: " ".join([x[0], x[1]]),
        51                     zip(nums, lines)
        52                 )
        53             )
        54             print("".join(result), end="")
        55             idx = len(lines) + 1
        56 
        57         print()
        58 
        59 
        60 if __name__ == "__main__":
        61     args = sys.argv[1:]
        62 
        63     if len(args) == 0 or args[0] == "-":
        64         try:
        65             process_stdin()
        66         # SIGTERM handler
        67         except KeyboardInterrupt:
        68             pass
        69 
        70     else:
        71         try:
        72             process_file(args)
        73         except FileNotFoundError as not_file:
        74             print(" ".join(["Could not open file:", not_file.filename]))
        75         except KeyboardInterrupt:
        76             pass

```

```commandline
$ python3 task_1.py resources/empty - task_2.py 
        1 
        2 
        3 
        4 
        5 \n
        6 
        7 \t\n
        8 

kek
         9 kek
lol
         10 lol
        11 # tail
        12 
        13 import sys
        14 from typing import Final
        15 from collections import deque
        16 
        17 _STDIN_TAIL_SIZE: Final[int] = 17
        18 _FILE_TAIL_SIZE: Final[int] = 10
        19 
        20 
        21 def process_stdin() -> None:
        22     """
        23     Read stdin and print out the last several lines after EOF is reached.
        24 
        25     Note:
        26         Number of lines to output is determined by _STDIN_TAIL_SIZE.
        27     """
        28 
        29     deq: deque[str] = deque()
        30 
        31     try:
        32         while True:
        33             line: str = input()
        34 
        35             if len(deq) == _STDIN_TAIL_SIZE:
        36                 deq.popleft()
        37 
        38             deq.append(line)
        39 
        40     except EOFError:
        41         for elem in deq:
        42             print(elem)
        43 
        44 
        45 def process_file(file_names: list[str]) -> None:
        46     """
        47     Print out the last several lines of the provided files.
        48 
        49     Note:
        50         Number of lines to output is determined by _STDIN_TAIL_SIZE.
        51 
        52     Parameters:
        53         file_names: file names referring to the files to process
        54     """
        55 
        56     for file_name in file_names:
        57 
        58         if len(file_names) > 1:
        59             print(" ".join(["==>", file_name, "<=="]))
        60 
        61         if file_name == "-":
        62             process_stdin()
        63             continue
        64 
        65         with open(file_name, "r") as file:
        66             lines = file.readlines()
        67 
        68             if len(lines) < _FILE_TAIL_SIZE:
        69                 print("".join(lines))
        70                 continue
        71 
        72             print("".join(lines[len(lines)-_FILE_TAIL_SIZE+1:]))
        73 
        74 
        75 if __name__ == "__main__":
        76     args = sys.argv[1:]
        77 
        78     if len(args) == 0 or args[0] == "-":
        79         try:
        80             process_stdin()
        81         # SIGTERM handler
        82         except KeyboardInterrupt:
        83             pass
        84     else:
        85         try:
        86             process_file(args)
        87         except FileNotFoundError as not_file:
        88             print(" ".join(["Could not open file:", not_file.filename]))
        89         except KeyboardInterrupt:
        90             pass
```

```commandline
$ python3 task_1.py non_existing_file
Could not open file: non_existing_file
```