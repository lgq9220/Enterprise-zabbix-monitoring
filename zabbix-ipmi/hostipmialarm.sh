#!/bin/bash
##$1 用户名 $2密码 $3主机
alarminfo=`ipmitool  -I lanplus   -H $3 -U $1 -P $2 sel list | egrep -v "Event Logging Disabled" | egrep -v "SEL has no entries"`
if [ "$alarminfo" != "" ];then
  echo "服务器IP  $hostip"
  echo "${alarminfo}"
  ipmitool  -I lanplus   -H $3 -U $1 -P $2 sel cleared > /dev/null
fi
