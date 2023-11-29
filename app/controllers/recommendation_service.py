import joblib
from ..models import User, Job


# Load the machine learning model (assuming it's a job recommendation model)
model_path = '../../models/recommendations.pkl'
model = joblib.load(model_path)

def get_recommendations(user_id):
    # Fetch user's preferences (this is just a placeholder logic)
    user = User.query.get(user_id)
    if not user:
        return []

    user_preferences = user.job_preferences

    # Use the machine learning model to generate recommendations
    recommended_jobs = model.predict([user_preferences])

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
