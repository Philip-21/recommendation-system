from werkzeug.security import generate_password_hash, check_password_hash
from ..model import User
from app import db

def register_user(name, email, password):
    try:
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return None  # User already exists

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        print(f"Error registering user: {e}")
        return None


def authenticate_user(email, password):
    # Finding the user by email
    user = User.query.filter_by(email=email).first()
    
    # Checking if user exists and password is correct
    if user and check_password_hash(user.password, password):
        return user
    return None
    
