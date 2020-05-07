日志分析组建包括redis、filebeat、logstash、Elasticsearch、kibana

redis配置

```
bind XXX.XXX.XXX.XXX #ip
port 6379 #端口
tcp-keepalive 300 #心跳检测
daemonize yes #运行在后台
maxmemory 6000mb #限制最大内存
maxmemory-policy noeviction #到达最大内存后，不可写可读
rdb-save-incremental-fsync no #本地保存备份
```

nginx日志格式

```shell
log_format main '{"timestamp":"$time_local",'
    '"remote_addr":"$remote_addr",'
    '"request":"$request",'
    '"http_referer":"$http_referer",'
    '"request_method":"$request_method",'
    '"url":"$uri",'
    '"args":"$args",'
    '"body_size":$body_bytes_sent,'
    '"request_time":$request_time,'
    '"upstream_time":$upstream_response_time,'
    '"upstream_addr":"$upstream_addr",'
    '"request_host":"$host",'
    '"domain":"XXXX",' #这个改成nginx名字，例如gateapi等，说明此nginx做什么用，用来过滤。
    '"status":"$status",'
    '"req_body":"$request_body}";
```

nginx filebeat配置

```shell
filebeat.inputs:
- input_type: log
  paths:
    - /var/log/nginx/access.log
  json.message_key: log
  json.keys_under_root: true
  tail_files: true #从最后一行开始采集
  fields:
      host: "当前主机" #修改成当前主机IP
      sublei : "项目-nginx"
output.redis:
  hosts: ["redis:6379"] #redis server
  db: 1
  timeout: 10
  key: "项目-nginx"
```

nginx logstash配置

```shell
input {
    redis {
        host => "redis" #redis server
        port => "6379"
        data_type => "list"
        db => 2 #redis 第2个数据库
        batch_count => 1 #一次取一行
        key => "nginx" #redis key
    }
}
filter {  
        date {
          match => ["timestamp", "dd/MMM/yyyy:HH:mm:ss Z"]
        }
}
output {
      elasticsearch {
        user => "els"
        password => "1qaz@3edc"
        hosts => ["es:9200"]
        index => "jiankang-shuxin-nginx-%{+YYYY.MM.dd}"
        template_name => "template-jiankang-shuxin-nginx"
      }
      
}
```



java logback日志格式

```
"[%date{ISO8601}],[%p],[jar包名字],[%X{logtraceid}],[%X{merreqip}],%highlight(%t:%C:%L),%m %n"
```

java filebeat配置，要注意一点老旧日志归档不要采集，不然因为格式不一致会出现问题。

```shell
filebeat.inputs:
- input_type: log
  paths:
    - /var/log/1.log
  multiline.pattern: '^\[\d{4}\-\d{2}'
  multiline.negate: true
  multiline.match: after
  fields:
      host: "主机ip地址"
      app: "应用名字"
      sublei: "项目-java"
  tail_files: true #从最后一行开始采集
output.redis:
  hosts: ["redis地址:6379"] #redis server地址
  db: 4
  timeout: 10
  key: "项目-java"
```

java logstash配置文件

```shell
input {
        redis {
            host => "redis server地址"
            port => "6379"
            data_type => "list"
            db => 4 #redis 第4个数据库
            batch_count => 1 #一次取一条
            key => "项目-java" #redis的key
        }
}
filter {
        grok {
            match => [
            "message" , "\[%{TIMESTAMP_ISO8601:locals}\],\[%{DATA:info}\],\[%{DATA:jarname}\],\[%{DATA:traceid}\],\[%{DATA:merreqip}\],.*cost time = %{NUMBER:costime} .*",
            "message" , "\[%{TIMESTAMP_ISO8601:locals}\],\[%{DATA:info}\],\[%{DATA:jarname}\],\[%{DATA:traceid}\],\[%{DATA:merreqip}\],.*"
            ]
        }
        date {
            locale => "en"
            match => [ "locals", "yyyy-MM-dd HH:mm:ss,SSS"]
        }
        if [costime] {
            mutate {
            convert => [ "costime", "integer"]
            }
        }
}
output {
#   stdout{}
   elasticsearch {
        hosts => ["es:9200"]
        user => "elk" #elasticsearch用户名
        password => "password" #elasticsearch密码
        index => "java-%{+YYYY.MM.dd}" #elasticsearch索引
        template_name => "template-java" #elasticsearch模板
      }
}
```

