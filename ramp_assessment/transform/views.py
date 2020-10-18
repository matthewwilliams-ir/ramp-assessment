from flask import Blueprint, jsonify, request
from .service import TransformService
from ..exception import InvalidInputArray

import json

transform = Blueprint("transform", __name__)
service = TransformService()

@transform.route('/multiply', methods=["POST"])
def multiply():
    data = request.get_json(force=True)
    result = service.multiply(data["input"])
    response = json.loads(result)
    return response

@transform.errorhandler(InvalidInputArray)
def handle_invalid_input(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response