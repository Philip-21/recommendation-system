import sys
sys.path.append('../utils/')
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.data_model import User, engine
from flask import Flask
from sqlalchemy.orm import sessionmaker

# Initialize the Flask application
app = Flask(__name__)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

def register_user(name, email, password):
    """
    Register a new user in the database.

    Parameters:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        User: If registration is successful, returns the newly created User object.
        None: If a user with the same email already exists or an error occurs during registration.
    """
    try:
        # Check if user with the same email already exists
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            # Close the session and return None if user already exists
            session.close()
            return None  # User already exists

        # Hash the password using pbkdf2:sha256 method
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user instance
        new_user = User(name=name, email=email, password=hashed_password)

        # Add the new user to the session
        session.add(new_user)

        # Commit the changes to the database
        session.commit()

        # Close the session
        session.close()

        # Return the new user object
        return new_user
    except Exception as e:
        print(f"Error registering user: {e}")
        return None

def authenticate_user(email, password):
    """
    Authenticate a user based on email and password.

    Parameters:
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        User: If authentication is successful, returns the User object.
        None: If the user does not exist or the password is incorrect.
    """
    try:
        # Finding the user by email
        user = session.query(User).filter_by(email=email).first()

        # Checking if user exists and password is correct
        if user and check_password_hash(user.password, password):
            # Close the session and return the user if authentication succeeds
            session.close()
            return user

        # Close the session if user doesn't exist or password is incorrect
        session.close()
        return None
    except Exception as e:
        print(f"Error authenticating user: {e}")
        return None
