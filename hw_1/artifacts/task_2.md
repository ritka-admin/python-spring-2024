# task_2 artifacts

```commandline
$ python3 task_2.py resources/kek
Вам нужно реализовать CLI приложения, кроме кода, вам необходимо в качестве артефактов приложить текстовый файл, как вы проверяли работоспособность вашего кода (просто копия команд и выводов из терминала)

1.1
Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
Если файл не передан, то скрипт читает строки из `stdin`.

Он должен работать так же, как `nl -b a`.
```

```commandline
$ python3 task_2.py resources/many_lines_file
dynamic
ruin
intelligence
grand
gloom
baby
licence
emergency
copper
```

```commandline
$ python3 task_2.py resources/many_lines_file task_1.py 
==> resources/many_lines_file <==
dynamic
ruin
intelligence
grand
gloom
baby
licence
emergency
copper

==> task_1.py <==
        # SIGTERM handler
        except KeyboardInterrupt:
            pass

    else:
        try:
            process_file(args)
        except FileNotFoundError as not_file:
            print(" ".join(["Could not open file:", not_file.filename]))
```

```commandline
$ python3 task_2.py non_existing_file
Could not open file: non_existing_file
```