import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

# create application
server = Flask(__name__)
# set config option for MongoDB connection uri
server.config['MONGO_URI'] = 'mongodb://host.minikube.internal:27017/videos'

# provide an interface for working with MongoDB
mongo = PyMongo(server)

# allow storing and retrieving files using GridFS within MongoDB
fs = gridfs.GridFS(mongo.db)

# create connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# create login route to communicate with auth service
@server.route("/login", methods=['POST'])
def login():
    token, err = access.login(request)