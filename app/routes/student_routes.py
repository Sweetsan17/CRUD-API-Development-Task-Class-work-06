from flask import Blueprint
from app.controllers.student_controller import *

student_bp = Blueprint("students", __name__, url_prefix="/api/students")

student_bp.route("", methods=["POST"])(create_student)
student_bp.route("", methods=["GET"])(get_students)
student_bp.route("/<int:id>", methods=["GET"])(get_student)
student_bp.route("/<int:id>", methods=["PUT"])(update_student)
student_bp.route("/<int:id>", methods=["DELETE"])(delete_student)
