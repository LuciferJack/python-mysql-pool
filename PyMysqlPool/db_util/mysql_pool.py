#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import MySQLdb
from mysql.connector import errors

import PyMysqlPool.mysql.connector
from PyMysqlPool.db_util.db_config.mysql_config import db_config
from PyMysqlPool.db_util.python_rf.pool_convertor import FuzzyMySQLConverter


def get_pool_connection(_db_config):
    return get_pool_conn_implicitly(_db_config)


def get_pool_conn_implicitly(_db_config):
    config = _db_config
    if 'pool' not in config:
        raise errors.OperationalError("MySQL config error must pool key")
    pool = config['pool']
    if 'use' not in pool:
        raise errors.OperationalError("MySQL pool config error must pool key use")
    if 'size' not in pool:
        raise errors.OperationalError("MySQL pool config error must pool key size")
    if 'name' not in pool:
        raise errors.OperationalError("MySQL pool config error must pool key name")

    if pool and pool['use']:
        conn = PyMysqlPool.mysql.connector.connect(pool_name=pool['name'], pool_size=pool['size'],
                                                   host=config['host'], port=config['port'], user=config['user'],
                                                   passwd=config['passwd'],
                                                   db=config['db'], charset=config['charset'], use_unicode=True,
                                                   connect_timeout=1000)
        conn.set_converter_class(FuzzyMySQLConverter)
    else:
        conn = MySQLdb.connect(host=config['host'], port=config['port'], user=config['user'], passwd=config['passwd'],
                               db=config['db'], charset=config['charset'], use_unicode=True)
    return conn
