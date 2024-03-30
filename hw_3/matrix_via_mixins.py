import re
from functools import reduce

from numpy.core.umath import matmul
from numpy.lib.mixins import NDArrayOperatorsMixin


class MatrixHelperMixin:
    def __init__(self, m: list[list[int | float]]):
        if len(m) != 0 and not all(map(lambda row: len(row) == len(m[0]), m)):
            raise ValueError("All rows in a matrix must be of the same size")

        self._m = m
        self._mult_cache = dict()

    def __str__(self):
        result: list[str] = []
        for row in self._m:
            reduced: str = reduce(lambda x, y: " ".join([str(x), str(y)]), row)
            result.append(reduced)
        return "\n".join(result)

    def __hash__(self):
        # connect all numbers in a string, convert to int and take prime modulo
        return int(re.sub(r"\s+", "", str(self))) % 189733

    @property
    def matrix(self):
        return self._m

    @matrix.getter
    def matrix(self):
        return self._m

    @matrix.setter
    def matrix(self, new_value: list[list[int | float]]):
        self._m = new_value

    def write_to_file(self, file) -> None:
        file.write(str(self))


class MatrixViaMixins(MatrixHelperMixin, NDArrayOperatorsMixin):

    def __init__(self, m: list[list[int | float]]):
        MatrixHelperMixin.__init__(self, m)
        NDArrayOperatorsMixin.__init__(self)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        # ufunc -- object, method -- method name

        if len(inputs) != 2 or getattr(inputs[0], "_m") is None or getattr(inputs[1], "_m") is None:
            raise ValueError("Two MixinMatrices are expected as arguments")

        arr2_hash: int = hash(inputs[1])

        if ufunc is matmul and self._mult_cache.keys().__contains__(arr2_hash):
            return self._mult_cache[arr2_hash]

        arr1: MatrixViaMixins = inputs[0].matrix
        arr2: MatrixViaMixins = inputs[1].matrix

        result: MatrixViaMixins = MatrixViaMixins(list(ufunc(arr1, arr2, **kwargs)))
        self._mult_cache[arr2_hash] = result
        return result
