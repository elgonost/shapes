#!/bin/python3
class HashtagShape:
    
    symbol = "#"

    def __init__(self, size: int):
        self.size = size
        self.shape = None

    def create_shape(self):
        pass

    def print_shape(self):
        if self.shape is None:
            self.create_shape()
        for item in self.shape:
            print(item)


class HashtagTriangle(HashtagShape):

    def create_shape(self):
        self.shape = []
        for i in range(self.size):
            spaces = (self.size - i - 1) * " "
            symbols = (i + 1) * self.symbol
            self.shape.append(f"{spaces}{symbols}")


class HashtagSquare(HashtagShape):

    def create_shape(self):
        self.shape = []
        symbols = self.size * self.symbol
        for _ in range(self.size):
            self.shape.append(f"{symbols}")
            
