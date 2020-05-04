监控架构



1、架构图

![](.\架构图.png)

2、组建说明

zabbix：服务器故障信息、网络层性能和组件、应用层性能。

elk + redis：服务器日志、网络层日志、应用层日志。

prometheus：虚拟化性能采集。

pinpoint：应用全链路监控。

kafka：告警接受。

3、详细说明

服务器层采用shell job ipmi采集告警信息，信息推送至zabbix。

存储日志主动推送elk。

zabbix通过模板采集网络设备信息，网络设备日志推送至elk。

虚拟化告警信息通过python job采集存入数据库，虚拟化性能信息通过go agent存入prometheus。

pinpoint监控java类应用链路故障和访问量。

应用类日志推送elk，统计应用访问数据可视化。

zabbix 告警推送 kafka，再存入mysql 数据库，做为故障信息统计报表。

通过postgresql 打造资产管理系统，通过zabbix api更新主机描述，可快速定位各层的准确信息。





