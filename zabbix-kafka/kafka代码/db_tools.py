#!/usr/bin/env python
import pymysql

class HandCost(object):
    """
    处理数据库中的数据
    """

    def __init__(self, host, user, passwd, dbname, port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.port = port
        self.charset = charset

    def db_conn(self):
        """
        创建连接
        :return:
        """
        try:
            # 创建连接
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.dbname,charset=self.charset)
        except Exception as e:
            print(e)
            return False
        return (conn)

    def db_cur(self,db_conn):
        try:
            # 创建游标
            cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)
            return False
        return (cursor)

    def db_close(self, conn, cursor):
        """
        关闭连接
        :param conn:
        :param cursor:
        :return:
        """
        conn.close()
        cursor.close()

    def exeQuery(self, cursor, sql):
        """
        查询
        :param cursor:
        :param sql:
        :return:
        """
        cursor.execute(sql)
        return cursor