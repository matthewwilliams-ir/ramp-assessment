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
    df = service.get_original_results_df()
    result = service.multiply(data, df)
    
    original_json = json.loads(df.to_json())
    modified_json = json.loads(result)
    return {"original_results": original_json, "modified_results": modified_json}

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