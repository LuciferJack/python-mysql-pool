#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import inspect
import os
import sys
from __builtin__ import str
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
from  PyMysqlPool.util.logger import *

old_f = sys.stdout


class F:
    def write(self, x):
        old_f.write(x.replace("\n", " [%s]\n" % str(datetime.now())))


sys.stdout = F()


def get_caller_function():
    (frame, filename, line_number, function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    return function_name


def get_caller_info_total():
    frame_info = (frame, filename, line_number, function_name, lines, index) = \
    inspect.getouterframes(inspect.currentframe())[0]
    return frame_info


def get_caller_info(frames=None):
    if not frames:
        frames = len(inspect.getouterframes(inspect.currentframe()))
        (frame, filename, line_number,
         function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[frames - 1]
    else:
        (frame, filename, line_number,
         function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[frames]
    print(frame, filename, line_number, function_name, lines, index)
    return filename


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def disablePrint():
    return open(os.devnull, 'w')


def underline_print(string):
    under_str = "\033[4m%s\033[0m" % (str(string),)
    return under_str


if __name__ == '__main__':
    logging.info('main starts...')
    logging.info('main stop')
    sys.exit(0)
