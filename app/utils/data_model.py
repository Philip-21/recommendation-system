from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, \
                        Float, Integer, Text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://austine:wik@localhost/job_search_db'
# app.config['JWT_SECRET_KEY'] = 'wap12'  

# Initialize SQLAlchemy with the Flask app
# db = SQLAlchemy(app)

DATABASE_URL = 'postgresql+psycopg2://leke_test_db_user:3nFeujfzWEBYUKPZgqg56hBwAKM3IkZN@dpg-cnlj9dacn0vc73bdohrg-a.oregon-postgres.render.com/leke_test_db'

# Create the base class for declarative models
Base = declarative_base()
engine = create_engine(DATABASE_URL)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    job_preferences = Column(String(255))

class Job(Base):
    __tablename__ = 'jobs'
    job_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    skills_required = Column(Text)  # Can be changed to JSON if needed
    salary = Column(String)  # Assuming salary is stored as a string
    employment_type = Column(String(100))

class Recommendation(Base):
    __tablename__ = 'recommendations'
    recommendation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.job_id'), nullable=False)
    score = Column(Float)

# # Create the tables in the database
# Base.metadata.create_all(bind=engine)

# print("Database created successfully!!!")