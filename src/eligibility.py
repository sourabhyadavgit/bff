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
from kafka import KafkaProducer
from kafka import KafkaConsumer

app = Flask(__name__)

@app.route("/check",methods=['GET'])
def home():
    name = request.args.get('name')
    my_client = pymongo.MongoClient("mongodb://root:root@localhost:27017")
    mydb = my_client["Customer_data"]
    mycol = mydb["Personal_data"]
    document = mycol.find_one({"name": name })
    salary = 20
    loc = "Edinburgh"
    status = checkProperty(loc)
    
    status = "Approved"
    if document is not None:
        jsdoc = json.loads(json_util.dumps(document))
        print(jsdoc)
        salary = jsdoc['salary']
        address = jsdoc['address']
        
        print(" staus is " + status)
        #print("salary fetched is "+ salary)
        if salary > 30 :
            return render_template ('home.html', Customer = name ,salary =  salary, index_status = status)
        else:
            return "salary nt matched to elibility"    
    else:
        return render_template ('second.html', Customer = name, salary = salary, index_status =status )

def checkProperty(post_code):
    postcode = post_code
    producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=["localhost:9092"]
    )
    producer.send(topic="property",value = postcode)
    print("sending msg")
    producer.flush()
    producer.close
    
    # defining consumer for receving msgs form approval topic
    
    consumer = KafkaConsumer (
    "approved",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset='latest',
    enable_auto_commit=True
#    value_deserializer=lambda x: loads(x.decode('utf-8'))  
    )
    for message in consumer:
    #    print(message)
        message = message.value;
        val2 = message.decode("utf-8")
        val4 = val2.strip('\"')
        print(val4)
        consumer.close
    return val4

print("hello SMY")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)