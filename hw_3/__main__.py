import numpy as np
from matrix import Matrix
from matrix_via_mixins import MatrixViaMixins


def task_one() -> None:
    matrix1_np = np.random.randint(0, 10, (rows, rows))
    matrix2_np = np.random.randint(0, 10, (rows, rows))
    matrix3_np = np.random.randint(0, 10, (rows, rows))

    m1 = Matrix(list(matrix1_np.flatten()), rows)
    m2 = Matrix(list(matrix2_np.flatten()), rows)
    m3 = Matrix(list(matrix3_np.flatten()), rows)

    with open("./artifacts/3.1/matrix+.txt", "w") as file:
        result: Matrix = m1 + m2
        printable: str = "\n".join(
            ["lhs", m1.convert_to_printable(), "rhs", m2.convert_to_printable(), "res", result.convert_to_printable()])
        file.write(printable)

    with open("./artifacts/3.1/matrix_mul.txt", "w") as file:
        result: Matrix = m2 * m3
        printable: str = "\n".join(
            ["lhs", m2.convert_to_printable(), "rhs", m3.convert_to_printable(), "res", result.convert_to_printable()])
        file.write(printable)

    with open("./artifacts/3.1/matrix@.txt", "w") as file:
        result: Matrix = m1 @ m3
        printable: str = "\n".join(
            ["lhs", m1.convert_to_printable(), "rhs", m3.convert_to_printable(), "res", result.convert_to_printable()])
        file.write(printable)


def task_two() -> None:
    matrix1_np = np.random.randint(0, 10, (rows, rows))
    matrix2_np = np.random.randint(0, 10, (rows, rows))
    matrix3_np = np.random.randint(0, 10, (rows, rows))

    mixin_m1 = MatrixViaMixins(list(matrix1_np))
    mixin_m2 = MatrixViaMixins(list(matrix2_np))
    mixin_m3 = MatrixViaMixins(list(matrix3_np))

    with open("./artifacts/3.2/matrix+.txt", "w") as file:
        result: MatrixViaMixins = mixin_m1 + mixin_m2
        result.write_to_file(file)

    with open("./artifacts/3.2/matrix_mul.txt", "w") as file:
        result: MatrixViaMixins = mixin_m2 * mixin_m3
        result.write_to_file(file)

    with open("./artifacts/3.2/matrix@.txt", "w") as file:
        result: MatrixViaMixins = mixin_m1 @ mixin_m3
        result.write_to_file(file)


def task_three() -> None:
    while True:
        a: MatrixViaMixins = MatrixViaMixins(list(np.random.randint(0, 100, (rows, rows))))
        b: MatrixViaMixins = MatrixViaMixins(list(np.random.randint(0, 100, (rows, rows))))
        c: MatrixViaMixins = MatrixViaMixins(list(np.random.randint(0, 100, (rows, rows))))

        ab: MatrixViaMixins = a @ b
        cd: MatrixViaMixins = c @ b

        if hash(a) == hash(c) and a != c and ab != cd:
            with open("./artifacts/3.3/A.txt", "w") as file:
                a.write_to_file(file)
            with open("./artifacts/3.3/B.txt", "w") as file:
                b.write_to_file(file)
            with open("./artifacts/3.3/C.txt", "w") as file:
                c.write_to_file(file)
            with open("./artifacts/3.3/D.txt", "w") as file:
                # d == b
                b.write_to_file(file)
            with open("./artifacts/3.3/AB.txt", "w") as file:
                ab.write_to_file(file)
            with open("./artifacts/3.3/CD.txt", "w") as file:
                cd.write_to_file(file)
            with open("./artifacts/3.3/hash.txt", "w") as file:
                file.write("\n".join(["ab:", str(hash(ab)), "cd:", str(hash(cd))]))
            break


if __name__ == "__main__":
    np.random.seed(0)
    rows: int = 10

    task_one()
    task_two()
    task_three()


