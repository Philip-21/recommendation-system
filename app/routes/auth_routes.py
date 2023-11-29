# auth_routes.py

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from ..services.auth_service import register_user, authenticate_user
from ..utils.response_util import json_response

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = register_user(data['name'], data['email'], data['password'])
    if user:
        return json_response('User registered successfully', 201)
    else:
        return json_response('User already exists', 409)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data['email'], data['password'])
    if user:
        access_token = create_access_token(identity=user.user_id)
        return json_response('Login successful', access_token=access_token)
    else:
        return json_response('Invalid email or password', 401)
