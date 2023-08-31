from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class MaintenanceTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    technician = db.Column(db.String(100), nullable=False)
    completion_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
