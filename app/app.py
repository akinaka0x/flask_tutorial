from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

names = []

@app.route('/', methods=['GET'])
def index():
    response = """
Try the following commands:
curl -X GET http://localhost:8080/name
curl -X POST -H "Content-Type: application/json" -d '{"name" : "Ichiro"}' http://localhost:8080/name
curl -X POST -H "Content-Type: application/json" -d '{"name" : "Jiro"}' http://localhost:8080/name
curl -X GET http://localhost:8080/name
"""
    return response, 200

@app.route('/name', methods=['GET'])
def get_name():
    response = {"name": names}
    return response, 200

@app.route('/name', methods=['POST'])
def post_name():
    data = request.get_json()
    try:
        name = data['name']
    except KeyError:
        return {"name": ""}, 400
    names.append(name)
    return {"name": name}, 201
