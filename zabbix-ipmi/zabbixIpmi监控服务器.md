zabbix通过脚本采集服务器告警信息



可以通过api批量创建每个主机的宏，建议先在数据库中建立资产管理表，然后创建模板，每个主机挂载模板后，只要修改继承的宏值就可以了，以下为单台例子

![image-20200507084050261](..\image\5.png)

外部脚本存放在/usr/lib/zabbix/externalscripts/hostipmialarm.sh

![image-20200507084533385](..\image\6.png)

![image-20200507084823045](..\image\7.png)

![image-20200507084923065](..\image\8.png)