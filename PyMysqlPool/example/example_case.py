#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import logging
import sys

from PyMysqlPool.db_util.db_config.example_config import example_config
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate

# MAIN
# ===============================================

"""
use pool
"""


def query_pool():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  !=%s "
    _args = (job_status,)
    task = query(example_config['local'], _sql, _args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task, _args)
    return


"""
pool in operation
"""


def query_pool_in():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  in (%s) "
    _args = (job_status,)
    task = query(example_config['local'], _sql, _args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task, _args)
    return


"""
pool size special operation
"""


def query_pool_size():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  in (%s) "
    _args = (job_status,)
    task = query(example_config['local'], _sql, _args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task, _args)
    return


"""
single query
"""


def query_npool():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  !=%s "
    _args = (job_status,)
    task = query_single(example_config['local'], _sql, _args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task, _args)
    return


"""
insert
"""


def insert(nlp_rank_id, hit_query_word):
    # add more args
    _args = (nlp_rank_id, hit_query_word)
    _sql = """INSERT INTO nlp_rank_poi_online (nlp_rank_id,hit_query_word,rank_type,poi_list,poi_raw_list,article_id,city_id,status,create_time,version,source_from) VALUES (%s,%s,%s, %s, %s,%s, %s,%s, %s,%s,%s)"""
    affect = insertOrUpdate(example_config['local'], _sql, _args)
    logging.info("insert method insert result is %s ,input _data is %s ", affect, _args)
    return


"""
update
"""


def update(query_word, query_id):
    _args = (query_word, query_id)
    _sql = """update nlp_rank  set query_word = %s  WHERE  id = %s"""
    affect = insertOrUpdate(example_config['local'], _sql, _args)
    logging.info("update method update result is %s ,input _data is %s ", affect, _args)
    return


"""
dynamic pool
"""


def d_query():
    job_status = 1
    _sql = "select *  from master_job_list j  where j.job_status  !=%s "
    _args = (job_status,)
    task = query(example_config['local'], _sql, _args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task, _args)
    return


if __name__ == '__main__':
    logging.info('main starts...')
    d_query()
    logging.info('main stop')
    sys.exit(0)
