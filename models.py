from app import db  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_ops_user = db.Column(db.Boolean, default=False, nullable=False)  # Operation user flag
    is_email_confirmed = db.Column(db.Boolean, default=False, nullable=False)  # Email confirmation flag

    def __repr__(self):
        return f'<User {self.username}>'

    