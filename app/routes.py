from flask import Blueprint, request, jsonify, url_for
from app import db, mail
from app.models import User
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os

# Define the blueprint for routes
main = Blueprint('main', __name__)

# Initialize the serializer with the Flask app's secret key
s = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))

@main.route('/')
def welcome():
    return '<h1>welcome</h1>'