from flask import request, jsonify
from app.models.course import Course
from app import db

def create_course():
    data = request.get_json()

    course = Course(
        course_title=data["course_title"],
        course_fee=data["course_fee"],
        duration_month=data["duration_month"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({"message": "Course created"}), 201
