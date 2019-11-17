#!/bin/env python
from flask import Flask, render_template
from app import create_app, socketio

# app = create_app(debug=True)
app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)
