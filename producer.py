import  time
import json
from kafka import KafkaProducer

producer=KafkaProducer(bootstrap_servers='192.168.99.100:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#with open('C:/kafka/venv/sample.json') as f:
producer.send('jts',{ "sepal_length": 20, "sepal_width": 3, "petal_length": 2,"petal_width":4})
producer.send('jts',{ "sepal_length": 15, "sepal_width": 2, "petal_length": 7.0,"petal_width":8})
time.sleep((10))



