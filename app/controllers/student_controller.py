from flask import request, jsonify
from app.models.student import Student
from app import db
from datetime import datetime

def create_student():
    data = request.get_json()

    student = Student(
        full_name=data["full_name"],
        email=data["email"],
        age=data["age"],
        joined_date=datetime.strptime(data["joined_date"], "%Y-%m-%d").date()
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student created"}), 201

def get_students():
    students = Student.query.all()

    result = []
    for student in students:
        result.append({
            "id": student.id,
            "full_name": student.full_name,
            "email": student.email
        })

    return jsonify(result)

def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.full_name = data.get("full_name", student.full_name)
    db.session.commit()

    return jsonify({"message": "Student updated"})

def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted"})
