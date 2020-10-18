from flask import Blueprint, jsonify, request

bp = Blueprint("multiply", __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/multiply', methods=["POST"])
def multiply():
    return jsonify(request.get_json(force=True))