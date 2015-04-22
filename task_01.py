#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This function handles Index and Key Exceptions"""
    try:
        return var1[var2]
    except LookupError:
        print 'Your index/key does not exist'
        return var1
