import pymysql
class MyDB(object):
    """docstring for MyDB"""
    def __init__(self, host, user, passwd , db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connect = None
        self.cursor = None
    def db_connect(self):
        """数据库连接
        """
        con = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.db,charset='utf8')
        return con
    def db_cursor(self):
        con1 = self.db_connect()
        con1.connect()
        con1.cursor()
        return con1
    def db_execute(self, sql):
        cur = self.db_cursor()
        cur.cursor().execute(sql)
        cur.commit()
        cur.close()

# if __name__=="__main__":
#     mydb = MyDB(
#         host="192.168.52.148",
#         user="pinpoint",
#         passwd="123456",
#         db="pinpoint"
#     )
#     mydb.db_cursor()
#     sql="""
#     REPLACE  into application_list( application_name,
#                 service_type, code, agents, agentlists, update_time)
#                 VALUES ("wjw", "SPRING_BOOT", 1210, 1, '["iZ888glidopZ"]', "2019-05-17 13:24:51");
#     """
#     print(mydb.db_execute(sql))
