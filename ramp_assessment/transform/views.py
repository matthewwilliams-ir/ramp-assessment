from flask import Blueprint, jsonify, request
from .service import TransformService

import json

transform = Blueprint("transform", __name__)
service = TransformService()

@transform.route('/multiply', methods=["POST"])
def multiply():
    data = request.get_json(force=True)
    result = service.multiply(data["input"])
    return json.loads(result)