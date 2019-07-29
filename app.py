import os
import requests

from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit message")
def vote(data):
    selection = data["selection"]
    bb = data["bb"]
    emit("announce message", {"selection": selection, "bb": bb}, broadcast=True)



if __name__ == '__main__':
    socketio.run(app, debug=True) 