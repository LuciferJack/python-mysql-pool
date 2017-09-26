#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import datetime


def get_day_format():
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    return today


def get_daystr_format(data):
    datastr = data.strftime("%Y-%m-%d %H:%M:%S")
    return datastr
