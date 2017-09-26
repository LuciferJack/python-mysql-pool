#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import logging
import sys

logging.basicConfig(level=logging.NOTSET,
                    format='[%(asctime)s][%(levelname)7s][%(threadName)s][%(filename)s:%(funcName)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)
# create logger
logger = logging.getLogger('my-logger')
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.INFO)
# add ch to logger
logger.addHandler(ch)
# disable all
# logger.propagate = False
