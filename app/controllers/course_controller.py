from flask import request, jsonify
from app.models.course import Course
from app import db


def create_course():
    data = request.get_json()

    course = Course(
        course_title=data["course_title"],
        course_fee=data["course_fee"],
        duration_month=data["duration_month"],
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({"message": "Course created"}), 201


def get_courses():
    courses = Course.query.all()
    result = [
        {
            "id": c.id,
            "course_title": c.course_title,
            "course_fee": c.course_fee,
            "duration_month": c.duration_month,
        }
        for c in courses
    ]
    return jsonify(result)


def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(
        {
            "id": course.id,
            "course_title": course.course_title,
            "course_fee": course.course_fee,
            "duration_month": course.duration_month,
        }
    )
