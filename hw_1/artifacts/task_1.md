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
    $ python3 task_1.py resources/task_1 
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
$ python3 task_1.py resources/empty - resources/task_1
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
        11 # nl -b a
        12 
        13 import sys
        14 
        15 
        16 def process_stdin(idx: int = None) -> int:
        17     """
        18     Count all lines from stdin until EOF.
        19 
        20     Parameters:
        21         idx: index from which should start counting
        22 
        23     Return:
        24         Index on which stopped counting
        25     """
        26 
        27     idx: int = idx if idx is not None else 1
        28 
        29     try:
        30         while True:
        31             line: str = input()
        32             result: str = " ".join(["\t", str(idx), line])
        33             print(result)
        34             idx += 1
        35     except EOFError:
        36         return idx
        37 
        38 
        39 def process_file(file_names: list[str]) -> None:
        40     """
        41     Count all lines in provided files. Empty lines are also accounted.
        42 
        43     Parameters:
        44         file_names: file names referring to the files to process
        45     """
        46 
        47     idx: int = 1
        48 
        49     for file_name in file_names:
        50 
        51         if file_name == "-":
        52             idx = process_stdin(idx)
        53             continue
        54 
        55         with open(file_name, "r") as file:
        56             lines: list[str] = file.readlines()
        57             nums: list[str] = ["".join(["\t", str(x)]) for x in range(idx, idx + len(lines) + 1)]
        58             result: list[str] = list(
        59                 map(
        60                     lambda x: " ".join([x[0], x[1]]),
        61                     zip(nums, lines)
        62                 )
        63             )
        64             print("".join(result), end="")
        65             idx = len(lines) + 1
        66 
        67         print()
        68 
        69 
        70 if __name__ == "__main__":
        71     args = sys.argv[1:]
        72 
        73     if len(args) == 0 or args[0] == "-":
        74         try:
        75             process_stdin()
        76         # SIGTERM handler
        77         except KeyboardInterrupt:
        78             pass
        79 
        80     else:
        81         try:
        82             process_file(args)
        83         except FileNotFoundError as not_file:
        84             print(" ".join(["Could not open file:", not_file.filename]))
        85         except KeyboardInterrupt:
        86             pass
```

```commandline
$ python3 task_1.py non_existing_file
Could not open file: non_existing_file
```