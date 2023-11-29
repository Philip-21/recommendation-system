from flask import Blueprint

# Importing the individual route modules
from .auth_routes import auth_bp
from .recommendation_routes import recommendation_bp
# Import additional route modules as needed

# Create a blueprint for all routes
all_routes = Blueprint('all_routes', __name__)

# Registering individual blueprints with the main routes blueprint
all_routes.register_blueprint(auth_bp, url_prefix='/auth')
all_routes.register_blueprint(recommendation_bp, url_prefix='/recommendations')
# Register additional blueprints as needed
