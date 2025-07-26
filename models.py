# models.py
from flask_sqlalchemy import SQLAlchemy
from app import db  # Import db from your main app file

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    # Relationship to Attendance
    attendance_records = db.relationship('Attendance', backref='student', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    status = db.Column(db.String(1), nullable=False)  # P or A
