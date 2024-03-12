# recommendation_routes.py
import sys
sys.path.append('../services/')
sys.path.append('../utils/')
from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.recommendation_service import get_recommendations, df, model
from ..services.recommendation_service import convert_int64_to_int
from ..utils.response_util import json_response

recommendation_bp = Blueprint('recommendation_bp', __name__)

@recommendation_bp.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get the job title from the request data
        job_title = request.json.get('job_title')
        # Call the get_recommendations function with the job title
        recommendations = get_recommendations(job_title, df, model)
         # Convert any instances of int64 to int in the recommendations
        recommendations = convert_int64_to_int(recommendations)
        return json_response('Recommendations fetched successfully', recommendations=recommendations)
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error in recommendation route: {str(e)}")
        return json_response(f'Error fetching recommendations: {str(e)}', 500)

