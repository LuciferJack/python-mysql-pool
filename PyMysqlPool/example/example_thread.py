#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import logging
import sys
from threading import Thread
from PyMysqlPool.example.example_case import d_query


def doPoiWork():
    d_query()


def thread_case(concurrent):
    for i in range(concurrent):
        t = Thread(target=doPoiWork, args=())
        t.daemon = True
        t.start()


if __name__ == '__main__':
    logging.info('main starts...')
    thread_case(100)
    logging.info('main stop')
    sys.exit(0)
