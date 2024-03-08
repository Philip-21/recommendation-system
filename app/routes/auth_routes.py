# auth_routes.py
import sys
sys.path.append('../services/')
sys.path.append('../utils/')
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from ..services import auth_service
from ..utils import response_util
from flask import jsonify, Flask

# from app import app

app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
# app.config["JWT_SECRET_KEY"] = "929370b13"
# Initialize the JWTManager with your Flask application
jwt = JWTManager(app)
# jwt.init_app(app)

# jwt_manager = get_jwt_manager()

auth_bp = Blueprint('auth_bp', __name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Recommendation System API'})

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = auth_service.register_user(data['name'], data['email'], data['password'])
    if user:
        return response_util.json_response('User registered successfully', 201)
    else:
        return response_util.json_response('User already exists', 409)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = auth_service.authenticate_user(data['email'], data['password'])
    if user:
        access_token = create_access_token(identity=user.user_id)
        return response_util.json_response('Login successful', access_token=access_token)
    else:
        return response_util.json_response('Invalid email or password', 401)
