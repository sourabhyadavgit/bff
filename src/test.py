import socket
from flask import Flask,jsonify,render_template
import requests
from flask import request
import pymongo
import bson
from bson.json_util import dumps
from bson import json_util
import json
from json import dumps
from kafka import KafkaConsumer
from kafka import KafkaProducer
app = Flask(__name__)

def checkProperty(postcode):
    
    print("postoce is :" + postcode)
    
print("hello SMY")



if __name__ == '__main__':
    post = input(" Enter :")
    checkProperty(post)
    consumer = KafkaConsumer (
    "property",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset='latest',
    enable_auto_commit=True
#    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
#consumer.close();

for message in consumer:
#    print(message)
    message = message.value;
    val2 = message.decode("utf-8")
    val4 = val2.strip('\"')
    print(val4)
    if val4 == "London" or "Edingburgh":
        value = "approved"
    else:
        value = "Not approved"    
    
"""     producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=["localhost:9092"]
    )
    producer.send(topic="approved",value = "Not approved")
    producer.flush()
    producer.close """
