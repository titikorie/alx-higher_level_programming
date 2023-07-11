#!/usr/bin/python3
"""This module is for task 8"""


class BaseGeometry:
    """A class defining a geometric shape"""
    def __init__(self, width, height):
        '''Initialization of the object'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
