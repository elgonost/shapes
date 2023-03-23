#!/bin/python3
from abc import ABC, abstractmethod


class BaseShape(ABC):
    """
    Abstract class that provides guidelines for the useful
    task of printing shapes using a specific symbol 
    in the console.

    Attributes
    ----------
    size: int
        The number of lines that the shape will use in the console.
    """

    symbol: str = None  # Shapes without many corners usually look good using # symbol
    minimum_size: int = None  # Suggested minimum_size for any shape is 2 lines. Use less at your own risk

    def __init__(self, size: int):
        self.size = self._validate_size(size)
        self.shape = self._create_shape()

    def __str__(self) -> str:
        return "\n".join(self.shape)
    
    def _validate_size(self, size: int) -> int:
        if size < self.minimum_size:
            raise Exception(
                f"Unable to draw {self.__class__.__name__} of that size. Minimum size is {self.minimum_size}"
            )
        return size

    @abstractmethod
    def _create_shape(self) -> list:
        pass