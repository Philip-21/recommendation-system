# controllers/recommendation_controller.py

from ..utils.data_preprocessing import preprocess_user_preferences
from ..utils.model_loading import load_recommendation_model
from ..model import User, Job
import os
import joblib

# Load the machine learning model
model_path = os.path.join(os.path.dirname(__file__), '../../models/recommendations.pkl')
model = None

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    print("Model file not found. Please train and save the model first.")


def get_recommendations(user_id):
    user = User.query.get(user_id)
    if not user:
        return []

    # Preprocess user preferences
    user_preferences = preprocess_user_preferences(user.job_preferences)

    # Use the machine learning model to generate recommendations
    try:
        recommended_jobs = model.predict([user_preferences])
    except Exception as e:
        print(f"Error during model prediction: {e}")
        return []

    recommendations = []
    for job_id in recommended_jobs:
        job = Job.query.get(job_id)
        if job:
            recommendations.append({
                'job_id': job.job_id,
                'title': job.title,
                'description': job.description,
            })

    return recommendations
