import numpy as np
from matrix import Matrix


if __name__ == "__main__":
    # TODO: numpy generate
    m1: Matrix = Matrix([1, 2, 3, 4, 5, 6], 2)
    m2: Matrix = Matrix([7, 8, 9, 10, 11, 12], 2)
    m2: Matrix = Matrix([1, 2, 3, 4, 5, 6], 3)

    with open("hw_3/artifacts/3.1/matrix+.txt", "w") as file:
        result: Matrix = m1 + m2
