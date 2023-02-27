from typing import Dict, Optional, Tuple

from db.db_engine import get_session
from db.models import Course, Student

session = get_session()


def student_validator(student_id: int) -> Student:
    student = session.query(Student).filter_by(id=student_id).first()
    return student


def validate_student_data(data) -> Optional[Tuple]:
    if "first_name" not in data.keys() or "last_name" not in data.keys():
        return
    return data["first_name"], data["last_name"], data["group_id"]


def group_validator(group_id: int) -> int:
    if group_id in range(1, 11):
        return group_id


def validate_student_on_course(data: Dict) -> Optional[Tuple[int, int]]:
    if "student_id" not in data.keys() and "course_id" not in data.keys():
        return
    student_id, course_id = data["student_id"], data["course_id"]
    if student_validator(student_id) is None or course_id > 10 or course_id < 1:
        return
    exist = (
        session.query(Student, Course)
        .outerjoin(Course, Student.courses)
        .filter(Student.id == student_id, Course.id == course_id)
        .first()
    )
    if exist is not None:
        return
    return student_id, course_id
