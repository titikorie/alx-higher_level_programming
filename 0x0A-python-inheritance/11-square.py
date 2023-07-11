i#!/usr/bin/python3
"""This module defines a class, Rectangle"""


class BaseGeometry:
    """A class defining a geometric shape"""

    def __init__(self, size):
        """initialization of square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """get that number"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
