from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers.recommendation_service import get_recommendations

recommendation_bp = Blueprint('recommendation_bp', __name__)

@recommendation_bp.route('/recommend', methods=['GET'])
@jwt_required()
def recommend():
    # Get the user ID from the JWT token
    user_id = get_jwt_identity()

    # Fetch recommendations using the recommendation service
    recommendations = get_recommendations(user_id)

    return jsonify({'recommendations': recommendations})
