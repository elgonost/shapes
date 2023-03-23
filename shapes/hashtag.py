#!/bin/python3
class HashtagShape:
    
    symbol = "#"
    minimum_size = None

    def __init__(self, size: int):
        self.size = self._validate_size(size)
        self.shape = self._create_shape()

    def __str__(self) -> str:
        st = ""
        for item in self.shape:
            st += f"{item}\n"
        return st
    
    def _validate_size(self, size: int) -> int:
        if size < self.minimum_size:
            raise Exception(
                f"Unable to draw {self.__class__.__name__} of that size. Minimum size is {self.minimum_size}"
            )
        return size

    def _create_shape(self) -> list:
        pass


class HashtagTriangle(HashtagShape):

    minimum_size = 2

    def _create_shape(self):
        shape = []
        for i in range(self.size):
            spaces = (self.size - i - 1) * " "
            symbols = (i + 1) * self.symbol
            shape.append(f"{spaces}{symbols}")
        return shape


class HashtagSquare(HashtagShape):

    minimum_size = 2

    def _create_shape(self):
        shape = []
        symbols = self.size * self.symbol
        for _ in range(self.size):
            shape.append(f"{symbols}")
        return shape
