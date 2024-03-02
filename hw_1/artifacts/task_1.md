# task_1 artifacts

```commandline
$ python task_1.py resources/task_1/kek 
        1 Вам нужно реализовать CLI приложения, кроме кода, вам необходимо в качестве артефактов приложить текстовый файл, как вы проверяли работоспособность вашего кода (просто копия команд и выводов из терминала)
        2 
        3 1.1
        4 Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
        5 Если файл не передан, то скрипт читает строки из `stdin`.
        6 
        7 Он должен работать так же, как `nl -b a`.
```

```commandline
$ python task_1.py resources/task_1/empty
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
$ python task_1.py task_1.py 
        1 # nl -b a
        2 
        3 import sys
        4 
        5 
        6 def process_stdin() -> None:
        7     """Count all lines from stdin until SIGTERM, SIGSTOP or EOF."""
        8 
        9     idx: int = 1
        10 
        11     while True:
        12         line: str = input()
        13         result: str = " ".join(["\t", str(idx), line])
        14         print(result)
        15         idx += 1
        16 
        17 
        18 def process_file(file_names: list[str]) -> None:
        19     """
        20     Count all lines in provided files. Empty lines are also accounted.
        21 
        22     Parameters:
        23         file_names: file names referring to the files to process
        24     """
        25 
        26     for file_name in file_names:
        27 
        28         with open(file_name, "r") as file:
        29             lines: list[str] = file.readlines()
        30             nums: list[str] = ["".join(["\t", str(x)]) for x in range(1, len(lines) + 1)]
        31             result: list[str] = list(
        32                 map(
        33                     lambda x: " ".join([x[0], x[1]]),
        34                     zip(nums, lines)
        35                 )
        36             )
        37             print("".join(result), end="")
        38 
        39         print()
        40 
        41 
        42 if __name__ == "__main__":
        43     args = sys.argv[1:]
        44 
        45     if len(args) == 0:
        46         try:
        47             process_stdin()
        48         except (KeyboardInterrupt, EOFError):
        49             pass
        50 
        51     else:
        52         try:
        53             process_file(args)
        54         except FileNotFoundError as not_file:
        55             print(" ".join(["Could not open file:", not_file.filename]))
        56 
```