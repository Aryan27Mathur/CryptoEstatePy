from flask import Flask, render_template, redirect, url_for, request
import json
from flask_socketio import SocketIO
from twilio.rest import Client
import os




app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


app.run(host='0.0.0.0', port=81)