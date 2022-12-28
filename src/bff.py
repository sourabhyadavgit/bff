import socket
from flask import Flask,jsonify,render_template
import requests
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to Loan Services</p>"

@app.route("/eligibility")
def eligibility():
    name = request.args.get('name')
    payload = {'name': name}
    r = requests.get('http://127.0.0.1:5001/check', params=payload)
    return r.text



@app.route("/property")
def application():
    host,ip = clusterdetails()
    return render_template ("index.html", index_hostname = host,index_ip = ip)

# function to fetch cluster details
def clusterdetails():
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name,host_ip


print("hello SMY")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)