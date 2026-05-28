from app import db

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String(100), unique=True, nullable=False)
    course_fee = db.Column(db.Float, nullable=False)
    duration_month = db.Column(db.Integer, nullable=False)
