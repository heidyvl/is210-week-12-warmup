#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Invalid Age"""
    pass


def get_age(birthyear):
    """Raises an error if age is invalid"""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError('Not a valid age')
    else:
        return age
