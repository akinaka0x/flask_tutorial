from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

names = []

@app.route('/', methods=['GET'])
def index():
    response = """
Try the following commands:
curl -X GET http://localhost:8080/name
curl -X POST http://localhost:8080/name/Ichiro
curl -X POST http://localhost:8080/name/Jiro
curl -X GET http://localhost:8080/name
"""
    return response, 200

@app.route('/name', methods=['GET'])
def get_name():
    response = {"name": names}
    return response, 200

@app.route('/name/<name>', methods=['POST'])
def post_name(name: str):
    names.append(name)
    response = {"name": name}
    return response, 201
