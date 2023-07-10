#!/usr/bin/python3
"""This module is for task 12"""


class MyInt(int):
    """weird class"""
    def __eq__(self, other):
        """== method"""
        if int.__eq__(self, other):
            return False
        return True

    def __ne__(self, other):
        """!= method"""
        if int.__ne__(self, other):
            return False
        return True
