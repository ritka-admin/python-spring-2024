
class Matrix:

    def __init__(self, m: list[int | float], rows: int):

        if len(m) % rows != 0:
            raise ValueError("All rows in a matrix must be of the same size")

        self.m = m
        self.rows = rows

    def __add__(self, other: "Matrix") -> "Matrix":

        if len(self.m) == len(other.m) and self.rows == other.rows:
            return Matrix([a + b for (a, b) in zip(self.m, other.m)], self.rows)

        raise ValueError("Trying to sum matrices of different dimensions")

    def __mul__(self, other: "Matrix") -> "Matrix":

        if len(self.m) == len(other.m) and self.rows == other.rows:
            return Matrix([a * b for (a, b) in zip(self.m, other.m)], self.rows)

        raise ValueError(
            "Trying to perform componentwise multiplication of matrices of different dimensions"
        )

    def __matmul__(self, other: "Matrix") -> "Matrix":
        self_columns: int = len(self.m) // self.rows
        other_columns: int = len(other.m) // other.rows
        result: list[int | float] = [0] * self.rows * other_columns

        if self_columns == other.rows:
            for i in range(self.rows):
                for j in range(self_columns):
                    for k in range(other_columns):
                        result[i * other_columns + j] += (
                            self.m[i * self_columns + k] * other.m[k * other_columns + j]
                        )
            return Matrix(result, self.rows)

        raise ValueError("Trying to sum matrices of different dimensions")
