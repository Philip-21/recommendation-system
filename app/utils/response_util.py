# utils/response_util.py
from flask import jsonify


def json_response(message, status_code=200, **kwargs):
    response = {'message': message}
    response.update(kwargs)
    return jsonify(response), status_code
