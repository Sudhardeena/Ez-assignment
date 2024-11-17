from flask import Blueprint, request, jsonify, url_for, current_app
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os


# Define the blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def welcome():
    return '<h1>Welcome Everyone</h1>'