from flask import Blueprint, jsonify, request
from .service import TransformService
from ..exception import InvalidInputArray
from werkzeug.exceptions import HTTPException

import json

transform = Blueprint("transform", __name__, url_prefix="/transform")
service = TransformService()

@transform.route('/multiply', methods=["POST"])
def multiply():
    data = request.get_json(force=True)
    result = service.multiply(data)
    response = json.loads(result)
    return response

@transform.errorhandler(InvalidInputArray)
def handle_invalid_input(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@transform.errorhandler(HTTPException)
def handle_generic_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "message": error.description,
    })
    response.content_type = "application/json"
    return response