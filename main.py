from flask import Flask, jsonify, request  # import needed packages
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

# assign the flask in object
app = Flask(__name__)
# MYSQL DATABASE CONNECTION CONFIGUATION CODE ADDED
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root123@localhost/api_development"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# asssign to db variable in SQLAlchemy(app)
db = SQLAlchemy(app)


# Create Student Model
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, Primary_key=True, AutoIncrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    cgpa = db.Column(db.Float, Default=0.0)
    is_active = db.Column(db.Boolean, Default=True)
    joined_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, Default=datetime.utcnow)


# Create Course Model
class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, Primary_key=True, AutoIncrement=True)
    course_title = db.Column(db.String(100), nullable=False, unique=True)
    course_fee = db.Column(db.Float, nullable=False)
    duration_month = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_available = db.Column(db.Boolean, Default=True)
    created_at = db.Column(db.DateTime, Default=datetime.utcnow)


if __name__ == "__Main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Your Database Connected Successfully")
    except Exception as error:
        print("ERROR: Your Database Connection Failed ")
        print({error})
    app.run(debug=True)
