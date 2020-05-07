1、概述
通过api或者zabbix数据库采集指定时间段内问题，写入自身告警表中，可以通过web进行编辑备注，方便统一管理所有告警，还可以做聚合。
2、表结构
eventid（key）,group,host,ip,description,alarm_time,recover_time,trigger_name,alarm_value,recover_value,tag,备注

zabbix 告警
{"eventid":"dev{EVENT.ID}","group":"{TRIGGER.HOSTGROUP.NAME}","host":"{HOSTNAME1}","ip":"{HOST.IP}","alarm_time":"{EVENT.DATE} {EVENT.TIME}","trigger_name":"{TRIGGER.NAME}","alarm_value":"{ITEM.LASTVALUE}","alarm_type":"alarm","alarm_level":"{TRIGGER.SEVERITY}","description":"{HOST.DESCRIPTION}"}

zabbix恢复
{"eventid":"dev{EVENT.ID}","recover_time":"{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}","recover_value":"{ITEM.LASTVALUE}","alarm_type":"recover"}

3、编写逻辑
eventid主键，通过主键进行修改、更新。
4、碰到问题
采集信息不易，修改采集方式，通过zabbix自身告警发送到缓存，才提取写入告警表中。
zabbix-》kafka《-脚本-》数据库

5、完成状态
producer -> kafak server -> consumer ok
创建表 ok
producer 传参 ok
consumer -> database

6、启动
nohup bin/zookeeper-server-start.sh config/zookeeper.properties >/dev/null &
nohup bin/kafka-server-start.sh config/server.properties >/dev/null &