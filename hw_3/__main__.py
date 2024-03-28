import numpy as np
from matrix import Matrix
from matrix_via_mixins import MixinMatrix


if __name__ == "__main__":
    np.random.seed(0)
    rows: int = 10
    matrix1_np = np.random.randint(0, 10, (rows, rows))
    matrix2_np = np.random.randint(0, 10, (rows, rows))
    matrix3_np = np.random.randint(0, 10, (rows, rows))

    m1 = Matrix(list(matrix1_np.flatten()), rows)
    m2 = Matrix(list(matrix2_np.flatten()), rows)
    m3 = Matrix(list(matrix3_np.flatten()), rows)

    # 3.1
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

    # 3.2
    mixin_m1 = MixinMatrix(list(matrix1_np))
    mixin_m2 = MixinMatrix(list(matrix2_np))
    mixin_m3 = MixinMatrix(list(matrix3_np))

    with open("./artifacts/3.2/matrix+.txt", "w") as file:
        result: MixinMatrix = mixin_m1 + mixin_m2
        result.write_to_file(file)

    with open("./artifacts/3.2/matrix_mul.txt", "w") as file:
        result: MixinMatrix = mixin_m2 * mixin_m3
        result.write_to_file(file)

    with open("./artifacts/3.2/matrix@.txt", "w") as file:
        result: MixinMatrix = mixin_m1 @ mixin_m3
        result.write_to_file(file)

