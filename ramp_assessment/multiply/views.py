from flask import Blueprint, jsonify, request
from .service import transform

bp = Blueprint("multiply", __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/multiply', methods=["POST"])
def multiply():

    data = request.get_json(force=True)
    # json = jsonify(data)

    return transform(data["input"])