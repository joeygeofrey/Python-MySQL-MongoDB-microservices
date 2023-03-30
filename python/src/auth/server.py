import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

# application
server = Flask(__name__)
mysql = MySQL(server)

# configuration for the application
server.config["MYSQL_HOST"] = os.envision.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.envision.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.envision.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.envision.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.envision.get("MYSQL_PORT")

# create route for login
@server.route("/.login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401