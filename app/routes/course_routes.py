from flask import Blueprint
from app.controllers.course_controller import create_course

course_bp = Blueprint("courses", __name__, url_prefix="/api/courses")

course_bp.route("", methods=["POST"])(create_course)
