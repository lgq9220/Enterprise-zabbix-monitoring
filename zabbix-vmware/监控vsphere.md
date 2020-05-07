

分2块，一块通过prometheus采集性能指标，一块是通过python采集告警vm、exsi的告警信息存入本地mysql。

第一块，监控流程

vcenter -> govsphere-> prometheus server

脚本主要是govsphere，通过采集vcenter和exsi的指标通过页面的形式进行共享。



第二块，采集告警信息

vcenter -> vcapialarm -> mysql -> vmalarm.sh|exsialarm.sh	