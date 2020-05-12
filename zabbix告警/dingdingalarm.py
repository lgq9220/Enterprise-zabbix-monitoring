#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
import json
import sys
import re


headers = {'Content-Type': 'application/json'}

test_data = {
    'msgtype':"text",
    "text":{
        'content':"%s" % sys.argv[1]
    },
    "at":{
        "atMobiles":[],
        "isAtAll":True
    }
}

requrl = "https://oapi.dingtalk.com/robot/send?access_token=%s" % sys.argv[2]
print(requrl)
req = urllib2.Request(url = requrl,headers = headers,data = json.dumps(test_data))
response = urllib2.urlopen(req)
