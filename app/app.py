import sys
sys.path.append('./routes/')
from flask import Flask
from .routes.auth_routes import auth_bp
from .routes.recommendation_routes import recommendation_bp
from flask_jwt_extended import JWTManager

# Create the Flask application
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "929370b13"
jwt = JWTManager(app)
# Register the blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(recommendation_bp, url_prefix='/recommendations')

# Define a default route
@app.route('/')
def index():
    return "Welcome to the Recommendation System API"

# Run the application if executed directly
if __name__ == "__main__":
    app.run(debug=True)
