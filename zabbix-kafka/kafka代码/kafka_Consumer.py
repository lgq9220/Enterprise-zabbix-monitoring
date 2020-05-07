#!/usr/bin/python
from kafka import KafkaConsumer
import json
from db_tools import HandCost
import sys
#连接数据库
cmdb=HandCost(host='数据库IP',user='用户名',passwd='密码',dbname='数据库名称',port=3306)
cmdb_con=cmdb.db_conn()
cmdb_cur=cmdb.db_cur(cmdb_con)
#kafka消费
consumer = KafkaConsumer(sys.argv[1],group_id="zabbix1",auto_offset_reset="latest",bootstrap_servers= [sys.argv[2]],value_deserializer=json.loads)
for msg in consumer:
    try:
        revlaue = msg.value
        revlaue = revlaue.replace("\r", "")
        revlaue = revlaue.replace("\n", "")
        revlaue = revlaue.replace("\t", ",")
        item=json.loads(revlaue)
        if(item["alarm_type"] == "alarm"):
            insert_sql = "insert into zabbix_alarm(eventid,groupname,hostname,ip,alarm_time,trigger_name,alarm_value,alarm_level,alarm_type,description)  VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(item['eventid'],item['group'],item['host'],item['ip'],item['alarm_time'],item['trigger_name'],item['alarm_value'],item['alarm_level'],item["alarm_type"],item["description"])
            cmdb.exeQuery(cursor=cmdb_cur,sql=insert_sql)
            cmdb_con.commit()   
        if(item["alarm_type"] == "recover"):
            update_sql="update zabbix_alarm set recover_time='%s',recover_value='%s' where eventid='%s'" %(item['recover_time'],item['recover_value'],item['eventid'])
            cmdb.exeQuery(cursor=cmdb_cur,sql=update_sql)
            cmdb_con.commit()
    except Exception as e:
        print(msg.value,e)
        
cmdb.db_close(conn=cmdb_con,cursor=cmdb_cur)