#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import logging
import sys

from PyMysqlPool.constant.constant import loggingerr, loggErrorFile

logging.basicConfig(level=logging.NOTSET,
                    format='[%(asctime)s][%(levelname)7s][%(threadName)s][%(filename)s:%(funcName)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)

logFormatter = logging.Formatter(
    '[%(asctime)s][%(levelname)7s][%(threadName)s][%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
rootLogger = logging.getLogger(__name__)
rootLogger.setLevel(logging.ERROR)


# create console handler and set level to debug
ch = logging.StreamHandler(stream=sys.stderr)
ch.setLevel(logging.ERROR)
# add ch to logger
rootLogger.addHandler(ch)
if loggErrorFile:
    fileHandler = logging.FileHandler("{0}".format(loggingerr))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
