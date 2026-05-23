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


# POST METHOD ROUTES- CREATE THE STUDENTS AND COURSES DETAILS
@app.route("/api/students", methods=["POST"])
def create_students():
    data = request.get_json()
    # Add the validation for nullable=false
    if not data or not data.get("full_name"):
        return jsonify({"message": "Full_Name is Required"}), 400
    if not data.get("email") or not data.get("age") or not data.get("joined_date"):
        return jsonify({"message": "Email and Age and Joined_Date are Required"}), 400
    new_student = Student(
        full_name=data["full_name"],
        email=data["email"],
        age=data["age"],
        cgpa=data["cgpa"],
        is_active=data["is_active"],
        joined_date=data["joined_date"],
        created_at=data["created_at"],
    )
    db.session.add(new_student)
    db.session.commit()

    return (
        jsonify({"message": "New Student Created Success", "id": new_student.id}),
        201,
    )


if __name__ == "__Main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Your Database Connected Successfully")
    except Exception as error:
        print("ERROR: Your Database Connection Failed ")
        print({error})
    app.run(debug=True)
