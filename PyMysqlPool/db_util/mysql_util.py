#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import sys
from time import sleep

from PyMysqlPool.db_util.mysql_pool import get_pool_connection
from PyMysqlPool.mysql.connector.dpooling import PooledMySQLConnection
from PyMysqlPool.util.log_util import get_caller_info_total, get_caller_function
from PyMysqlPool.util.logger_err import rootLogger
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb


# ===============================================
# FUNCTION
# ===============================================
def query(_db_config, _sql, _args):
    conn = get_pool_connection(_db_config)
    if not isinstance(conn, PooledMySQLConnection):
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor(dictionary=True)
    result = ()
    try:
        cursor.execute(_sql, _args)
        result = cursor.fetchall()
    except:
        pass
        rootLogger.error("query exception sql is %s ,_args is %s,stacks is %s", _sql, _args, get_caller_info_total())
        rootLogger.exception("message")
    finally:
        cursor.close()
        conn.close()
    return result


# ===============================================
# FUNCTION not use pool
# ===============================================
def query_single(_db_config, _sql, _args):
    config = _db_config
    conn = MySQLdb.connect(host=config['host'], port=config['port'], user=config['user'], passwd=config['passwd'],
                           db=config['db'], charset=config['charset'], use_unicode=True)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result = ()
    try:
        cursor.execute(_sql, _args)
        result = cursor.fetchall()
    except:
        pass
        rootLogger.error("query exception sql is %s ,_args is %s,stacks is %s", _sql, _args, get_caller_info_total())
        rootLogger.exception("message")
    finally:
        cursor.close()
        conn.close()
    return result


# ===============================================
# FUNCTION  更新或者删除
# ===============================================
def insertOrUpdate(_db_config, _sql, _args):
    result = 0
    conn = get_pool_connection(_db_config)
    if not isinstance(conn, PooledMySQLConnection):
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor(buffered=True)
    try:
        cursor.execute(_sql, _args)
        conn.commit()
        result = cursor.rowcount
    except:
        pass
        rootLogger.error("exception sql is %s ,_args is %s", _sql, _args)
        rootLogger.exception("message")
        conn.rollback()
    finally:
        print("affected rows = {}".format(cursor.rowcount))
        cursor.close()
        conn.close()
    return result


# ===============================================
# FUNCTION  清空mysql数据
# ===============================================
def emptyTable(_db_config, _sql, _args):
    result = 0
    conn = get_pool_connection(_db_config)
    if not isinstance(conn, PooledMySQLConnection):
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor(buffered=True)
    # conn.autocommit(True) #replace False -> True
    try:
        cursor.execute(_sql, _args)
        conn.commit()
        result = cursor.rowcount
    except:
        pass
        rootLogger.error(" emptyTable exception sql is %s ,_args is %s", _sql, _args)
        rootLogger.exception("message")
        conn.rollback()
    finally:
        print("affected rows = {}".format(cursor.rowcount))
        cursor.close()
        conn.close()
    return result


# ===============================================
# FUNCTION  批量更新或者删除
# ===============================================
"""
From MySQLdb User's Guide:

c.executemany(
      "INSERT INTO breakfast (name, spam, eggs, sausage, price)
VALUES (%s, %s, %s, %s, %s)",
      [
      ("Spam and Sausage Lover's Plate", 5, 1, 8, 7.95 ),
      ("Not So Much Spam Plate", 3, 2, 0, 3.95 ),
      ("Don't Wany ANY SPAM! Plate", 0, 4, 3, 5.95 )
      ] )
so in your case:

c.executemany("insert into T (F1,F2) values (%s, %s)",
    [('a','b'),('c','d')])

"""


def insertOrUpdatePatch(_db_config, _sql, _args):
    result = 0
    conn = get_pool_connection(_db_config)
    if not isinstance(conn, PooledMySQLConnection):
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor(buffered=True)
    # conn.autocommit(True) #replace False -> True
    try:
        cursor.executemany(_sql, _args)
        conn.commit()
        result = cursor.rowcount
    except:
        pass
        rootLogger.error("insertOrUpdatePatch exception sql is %s ,_args is %s", _sql, _args)
        rootLogger.exception("message")
        conn.rollback()
    finally:
        print("affected rows = {}".format(cursor.rowcount))
        cursor.close()
        conn.close()
    return result


# ===============================================
# FUNCTION  更新或者删除
# ===============================================
def insertOrUpdate_getId(_db_config, _sql, _args):
    result = 0
    id = 0
    config = _db_config
    conn = MySQLdb.connect(host=config['host'], port=config['port'], user=config['user'], passwd=config['passwd'],
                           db=config['db'], charset=config['charset'], use_unicode=True)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(_sql, _args)
        id = conn.insert_id()
        conn.commit()
        result = cursor.rowcount
    except:
        pass
        rootLogger.error("exception sql is %s ,_args is %s", _sql, _args)
        rootLogger.exception("message")
        conn.rollback()
    finally:
        print("affected rows = {}".format(cursor.rowcount))
        cursor.close()
        conn.close()
    return result, id


def try_for_threes(_db_config, _sql, _args):
    caller = get_caller_function()
    for i in xrange(0, 3, 1):
        sleep(2)
        caller(_db_config, _sql, _args)


def check_record_exsit(_db_config, _sql, _args):
    result = 0
    conn = get_pool_connection(_db_config)
    if not isinstance(conn, PooledMySQLConnection):
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    else:
        cursor = conn.cursor(buffered=True)
    try:
        cursor.execute(_sql, _args)  # conn.commit()
        result = cursor.rowcount
    except:
        pass
        rootLogger.error("message")
        conn.rollback()
    finally:
        print("the record is has rows = {}".format(cursor.rowcount))
        cursor.close()
        conn.close()
    return result
