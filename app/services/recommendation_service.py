# controllers/recommendation_controller.py

from ..utils.data_preprocessing import preprocess_user_preferences
from ..utils.model_loading import load_recommendation_model
from ..model import User, Job

# Load the machine learning model
model_path = '../../models/recommendations.pkl'
model = load_recommendation_model(model_path)

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
