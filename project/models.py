# models.py

from flask_login import UserMixin
from project import db

class Registration(UserMixin, db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

class HasCSVHeader(db.Model):
    __tablename__ = 'hasCSVHeader'
    header_id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    header_status = db.Column(db.Integer, unique=True)

    def __init__(self, header_status):
        self.header_status = header_status
