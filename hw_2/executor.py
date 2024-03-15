from hw_2.tex_generator import generate_tex_table as gen


if __name__ == '__main__':
    with open("./artifacts/task_1.tex", 'w') as file:
        table = [
            ["lol", "kek"],
            ["lol", "kek", "azaza"],
            [i for i in range(5)]
        ]
        file.write(gen(table))
