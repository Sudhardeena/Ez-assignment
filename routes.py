from flask import Blueprint, request, jsonify, url_for, current_app
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
import os


# Define the blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def welcome():
    return '<h1>Welcome Everyone</h1>'


@main.route('/register',methods=['POST'])
def register():
    data = request.get_json()

    #validate input
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"message":"missing required fields!"}), 400

    #checking user already exists
    from models import User, db
    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already registered!"}), 400

    # Hash the password using bcrypt
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create the new user and save to the database
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201
