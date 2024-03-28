from functools import reduce


class Matrix:

    def __init__(self, m: list[int | float], rows: int):

        if len(m) % rows != 0:
            raise ValueError("All rows in a matrix must be of the same size")

        self._m = m
        self._rows = rows

    def __add__(self, other: "Matrix") -> "Matrix":

        if len(self._m) == len(other._m) and self._rows == other._rows:
            return Matrix([a + b for (a, b) in zip(self._m, other._m)], self._rows)

        raise ValueError("Trying to sum matrices of different dimensions")

    def __mul__(self, other: "Matrix") -> "Matrix":

        if len(self._m) == len(other._m) and self._rows == other._rows:
            return Matrix([a * b for (a, b) in zip(self._m, other._m)], self._rows)

        raise ValueError(
            "Trying to perform componentwise multiplication of matrices of different dimensions"
        )

    def __matmul__(self, other: "Matrix") -> "Matrix":
        self_columns: int = len(self._m) // self._rows
        other_columns: int = len(other._m) // other._rows
        result: list[int | float] = [0] * self._rows * other_columns

        if self_columns == other._rows:
            for i in range(self._rows):
                for j in range(self_columns):
                    for k in range(other_columns):
                        result[i * other_columns + j] += (
                            self._m[i * self_columns + k] * other._m[k * other_columns + j]
                        )
            return Matrix(result, self._rows)

        raise ValueError("Trying to sum matrices of different dimensions")

    def convert_to_printable(self) -> str:
        result: list[str] = []
        columns: int = len(self._m) // self._rows
        for i in range(self._rows):
            row_values: list[int | float] = self._m[i * columns:(i+1) * columns]
            reduced: str = reduce(lambda x, y: " ".join([str(x), str(y)]), row_values)
            result.append(reduced)
        return "\n".join(result)
