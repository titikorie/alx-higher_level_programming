#!/usr/bin/python3
"""This module is for task 10"""


class BaseGeometry:
    """A class defining a geometric shape"""

    def __init__(self, size):
        """initialization of squar"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """get that number"""
        return self.__size ** 2
