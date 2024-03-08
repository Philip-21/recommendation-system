# utils/response_util.py
from flask import jsonify


# def json_response(message, status_code=200, **kwargs):
#     response = {'message': message}
#     response.update(kwargs)
#     return jsonify(response), status_code

def json_response(message, status_code=200, **kwargs):
    """
    Generate a JSON response with a message and optional additional data.

    Parameters:
        message (str): The message to include in the response.
        status_code (int): The HTTP status code of the response (default is 200).
        **kwargs: Additional data to include in the response.

    Returns:
        flask.Response: A JSON response with the specified message and data.
    """
    response_data = {'message': message}
    response_data.update(kwargs)
    response = jsonify(response_data)
    response.status_code = status_code
    return response