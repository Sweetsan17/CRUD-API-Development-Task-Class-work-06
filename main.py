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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    cgpa = db.Column(db.Float, default=0.0)
    is_active = db.Column(db.Boolean, default=True)
    joined_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Create Course Model
class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_title = db.Column(db.String(100), nullable=False, unique=True)
    course_fee = db.Column(db.Float, nullable=False)
    duration_month = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# POST METHOD ROUTES- CREATE THE STUDENTS DETAILS
@app.route("/api/students", methods=["POST"])
def create_students():
    data = request.get_json()
    # Add the validation for nullable=false
    if not data:
        return jsonify({"message": "you must put your data"}), 400

    elif not data.get("full_name"):
        return jsonify({"message": "Full Name is Required"}), 400

    elif not data.get("email"):
        return jsonify({"message": "Email is required"}), 400

    elif "age" not in data:
        return jsonify({"message": "Age is required"}), 400

    elif not data.get("joined_date"):
        return jsonify({"message": "Joined Date is required"}), 400
    # Unique Email validation
    else:
        existing_email = Student.query.filter_by(email=data["email"]).first()
        if existing_email:
            return jsonify({"message": "This Email Already Existed"}), 401

    new_student = Student(
        full_name=data["full_name"],
        email=data["email"],
        age=data["age"],
        cgpa=data.get("cgpa", 0.0),
        is_active=data.get("is_active", True),
        joined_date=datetime.strptime(data["joined_date"], "%Y-%m-%d").date(),
    )
    db.session.add(new_student)
    db.session.commit()

    return (
        jsonify({"message": "New Student Created Success", "id": new_student.id}),
        201,
    )


#  GET METHOD ROUTE - Read students details
@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    details = []
    for student in students:
        details.append(
            {
                "id": student.id,
                "full_name": student.full_name,
                "email": student.email,
                "age": student.age,
                "cgpa": student.cgpa,
                "joined_date": student.joined_date,
            }
        )
        return jsonify(details)


if __name__ == "__main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Your Database Connected Successfully")
            db.create_all()
    except Exception as error:
        print("ERROR: Your Database Connection Failed ")
        print(error)
    app.run(debug=True)
