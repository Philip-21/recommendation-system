from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://austine:wik@localhost/job_search_db'
app.config['JWT_SECRET_KEY'] = 'wap12'  

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Importing and registering the main routes blueprint
from .routes import all_routes
app.register_blueprint(all_routes)
