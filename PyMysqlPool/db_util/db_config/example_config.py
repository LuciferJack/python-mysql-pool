#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
"""
can more db ,more pool
"""
example_config = {
    'local': {
        'host': "10.95.130.***", 'port': 8899,
        'user': "root", 'passwd': "******",
        'db': "marry", 'charset': "utf8",
        'pool': {
            # use = 0 no pool else use pool
            "use": 1,
            # size is >=0,  0 is dynamic pool
            "size": 10,
            # pool name
            "name": "local",
        }
    },
    'poi': {
        'host': "10.95.130.***", 'port': 8787,
        'user': "lujunxu", 'passwd': "****",
        'db': "poi_relation", 'charset': "utf8",
        'pool': {
            # use = 0 no pool else use pool
            "use": 0,
            # size is >=0,  0 is dynamic pool
            "size": 0,
            # pool name
            "name": "poi",
        }
    },
}
