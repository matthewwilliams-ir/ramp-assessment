__version__ = '0.1.0'

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/multiply', methods=["POST"])
def multiply():
    return jsonify(request.get_json(force=True))