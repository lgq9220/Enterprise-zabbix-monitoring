

先设置媒介

脚本名称：这个脚本是放在 /usr/lib/zabbix/alertscripts/kafka_Producer

脚本参数 ：kafka1 在系统/etc/hosts中做了解析 ,kafka1 ip地址

![image-20200507085848445](..\image\kafka4.png)

告警设置

![image-20200507085657619](..\image\kafka3.png)

```
#这些字段对应数据库的字段

{"eventid":"dev{EVENT.ID}","group":"{TRIGGER.HOSTGROUP.NAME}","host":"{HOSTNAME1}","ip":"{HOST.IP}","alarm_time":"{EVENT.DATE} {EVENT.TIME}","trigger_name":"{TRIGGER.NAME}","alarm_value":"{ITEM.LASTVALUE}","alarm_type":"alarm","alarm_level":"{TRIGGER.SEVERITY}","description":"{HOST.DESCRIPTION}"}
```

![image-20200507085522985](..\image\kafka1.png)



```
需要注意的是，eventid：dev这个前缀不同的zabbix请设置不一样，不然id会重复。
{"eventid":"dev{EVENT.ID}","recover_time":"{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}","recover_value":"{ITEM.LASTVALUE}","alarm_type":"recover"}
```

![image-20200507085556762](D:\blog\知识\Enterprise-zabbix-monitoring\image\kafka2.png)



kafka的流程是

kafka_Producer（在zabbix服务器上面） -> kafka_server（在决策系统上面） ->kafka_Consumer（在决策系统上面）

