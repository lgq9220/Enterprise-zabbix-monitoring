钉钉告警脚本传参2个

dingdingalarm.py 告警信息 钉钉群key

设置流程

管理 -》 报警媒介类型 -》创建媒体类型

```
名称 随意
类型 脚本
脚本名称 dingdingalarm.py
脚本参数
	{ALERT.MESSAGE}
	{ALERT.SENDTO}
```

接收的用户中报警媒介设置，

类型 钉钉告警名称

收件人 钉钉群的key

其他条件按需设置



邮件告警1

管理- 告警媒介类型-电子邮件

![image-20200512150649429](D:\blog\知识\Enterprise-zabbix-monitoring\image\告警1.png)

告警2

通过脚本告警

参数

收件人

标题

告警内容