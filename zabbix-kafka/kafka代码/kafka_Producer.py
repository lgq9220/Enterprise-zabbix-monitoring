#!/usr/bin/python
from kafka import KafkaProducer
import sys
import json

producer = KafkaProducer(bootstrap_servers=[sys.argv[1]],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send(sys.argv[2], sys.argv[3])
producer.close()