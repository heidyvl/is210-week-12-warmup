#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Custome Logger"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """log function"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """flush function"""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            try:
                for index in handled[::-1]:
                    del self.msgs[index]
            except IOError:
                raise IOError
        except IOError as log:
            raise IOError
        finally:
            fhandler.close()
