#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import PyMysqlPool.mysql.connector
from PyMysqlPool.constant.mysql_const import POOL_SIZE
from PyMysqlPool.db_util.db_config.mysql_config import db_config

from PyMysqlPool.db_util.python_rf.pool_convertor import FuzzyMySQLConverter


def get_pool_connection(_db, pool_info=None):
    return get_pool_conn_implicitly(_db, pool_info)

def get_pool_conn_implicitly(_db, pool_info=None):
    config = db_config[_db]
    if pool_info:
        pool_size = pool_info['pool_size']
        conn = PyMysqlPool.mysql.connector.connect(pool_name = _db, pool_size = pool_size,
                                                   host=config['host'], port=config['port'], user=config['user'], passwd=config['passwd'],
                                                   db=config['db'], charset=config['charset'], use_unicode=True, connect_timeout=1000)
    else:
        conn = PyMysqlPool.mysql.connector.connect(pool_name = _db, pool_size = POOL_SIZE,
                                                   host=config['host'], port=config['port'], user=config['user'], passwd=config['passwd'],
                                                   db=config['db'], charset=config['charset'], use_unicode=True, connect_timeout=1000)
    conn.set_converter_class(FuzzyMySQLConverter)
    return  conn