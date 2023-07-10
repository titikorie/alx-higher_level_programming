#!/usr/bin/python3
"""This module is for task 12"""


class MyInt(int):
    """Redefine equality comparisons"""
    def __eq__(self, other_int):
        """Return equal if not equal"""
        if self is not other_int:
            return True
        else:
            return False

    def __ne__(self, other_int):
        """Return not equal if equal"""
        if self is other_int:
            return True
        else:
            return False
