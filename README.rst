.. image:: https://api.travis-ci.org/LuciferJack/python-mysql-pool.svg?branch=master
    :target: https://travis-ci.org/LuciferJack/python-mysql-pool

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/LuciferJack/python-mysql-pool/blob/master/LICENSE.txt


PyMysqlPool
=======

.. contents:: Table of Contents
    :local:


Desc
-------------
python practical mysql pool desc:
This package contains a pure-python mysql connector library. The goal of PyMysqlPool
is to be a  mysql pool and motivation from=>[lost connection to MySQL server during query]  base on mysql-connector .

feature
  * easy to use.
  * support 【fixed 、dynamic pool】.
  * manage 【fail/lost connection】.

Requirements
-------------
* Python lib -- one of the following:
    MySQLdb
* Python -- one of the following:
    success test in python >=2.7
* MySQL Server -- one of the following:
   - MySQL_ >= 5.5  (success test with >=5.5~)


Installation
------------

The last stable release is available on PyPI and can be installed with ``pip``::

    $ pip install PyMysqlPool


Documentation
-------------

Documentation is available online: http://PyMysqlPool.readthedocs.io/

For support, please refer to the `StackOverflow
<http://stackoverflow.com/questions/tagged/PyMysqlPool>`_.

Example
-------

The following pool examples below:


.. code:: python

    step:1

    """
    file:mysql_config.py change to your db config
    """
    db_config = {
        'local': {
            'host': "10.95.130.***", 'port': 8899,
            'user': "root", 'passwd': "****",
            'db': "marry", 'charset': "utf8",
            'pool': {
                #use = 0 no pool else use pool
                "use":1,
                # size is >=0,  0 is dynamic pool
                "size":0,
                #pool name
                "name":"local",
            }
        },
        'poi': {
            'host': "10.95.130.***", 'port': 8787,
            'user': "lujunxu", 'passwd': "****",
            'db': "poi_relation", 'charset': "utf8",
            'pool': {
                #use = 0 no pool else use pool
                "use":0,
                # size is >=0,  0 is dynamic pool
                "size":0,
                #pool name
                "name":"poi",
            }
        },
    }

    step:2

    """
    Note:create your own table
    """

    step:3 (example show below)

    """
    pool size special operation
    """
    def query_pool_size():
        job_status = 2
        _sql = "select *  from master_job_list j  where j.job_status  in (%s) "
        _args = (job_status,)
        task = query(db_config['local'], _sql,_args)
        logging.info("query_npool method query_npool result is %s ,input _data is %s ", task , _args)
        return

    """
    single query
    """
    def query_npool():
        job_status = 2
        _sql = "select *  from master_job_list j  where j.job_status  !=%s "
        _args = (job_status,)
        task = query_single(db_config['local'], _sql,_args)
        logging.info("query_npool method query_npool result is %s ,input _data is %s ", task , _args)
        return

    """
    insert
    """
    def insert(nlp_rank_id,hit_query_word):
        #add more args
        _args = (nlp_rank_id,hit_query_word)
        _sql = """INSERT INTO nlp_rank_poi_online (nlp_rank_id,hit_query_word,rank_type,poi_list,poi_raw_list,article_id,city_id,status,create_time,version,source_from) VALUES (%s,%s,%s, %s, %s,%s, %s,%s, %s,%s,%s)"""
        affect = insertOrUpdate(db_config['local'], _sql, _args)
        logging.info("insert method insert result is %s ,input _data is %s ", affect , _args)
        return

    """
    update
    """
    def update(query_word,query_id):
        _args = (query_word,query_id)
        _sql = """update nlp_rank  set query_word = %s  WHERE  id = %s"""
        affect = insertOrUpdate(db_config['local'], _sql, _args)
        logging.info("update method update result is %s ,input _data is %s ", affect , _args)
        return



Resources
---------

python mysql connector: https://dev.mysql.com/downloads/connector/python/

MySQL Reference Manuals: http://dev.mysql.com/doc/

MySQL client/server protocol:
http://dev.mysql.com/doc/internals/en/client-server-protocol.html

PyMysqlPool mailing list: https://groups.google.com/forum/#!forum/PyMysqlPool-users

License
-------
PyMysqlPool is released under the MIT License. See LICENSE for more information.

Plan
-------
  | Dynamic Load Optimization.
  | Minimum number of connections to maximum performance.

Scope
-------
  | Now use in  **BaiDu** off-line calculation module.
  | Like this project, welcome to use and to enhance together.
