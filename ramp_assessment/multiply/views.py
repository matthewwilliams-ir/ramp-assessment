from flask import Blueprint, jsonify, request
from .service import MultiplyService

import json

bp = Blueprint("multiply", __name__)
service = MultiplyService()

@bp.route('/multiply', methods=["POST"])
def multiply():
    data = request.get_json(force=True)
    result = service.transform(data["input"])
    return json.loads(result)