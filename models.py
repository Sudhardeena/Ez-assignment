from app import db  
from werkzeug.security import generate_password_hash, check_password_hash  # For hashing and checking passwords

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_ops_user = db.Column(db.Boolean, default=False, nullable=False)  # Operation user flag
    is_email_confirmed = db.Column(db.Boolean, default=False, nullable=False)  # Email confirmation flag

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self,password): #to hash password before storing to database
        self.password = generate_password_hash(password)

    def check_password(self,password): #to compared with hashed password stored in db
        return check_password_hash(self.password,password)