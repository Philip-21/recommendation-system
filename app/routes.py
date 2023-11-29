# Defines the routes/endpoints of the application, such as the recommendation endpoint.
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User
from . import app, db

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        name=data['name'], 
        email=data['email'], 
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.user_id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/recommend', methods=['POST'])
@jwt_required()
def recommend():
    current_user_id = get_jwt_identity()
    # Placeholder for recommendation logic
    # You can access the user's ID with current_user_id
    # Implement your recommendation logic here

    return jsonify({'recommendations': 'This is where recommendations will appear'})
