import pytest

from db.data_generator import COURSES
from db.db_engine import get_session
from db.db_manager import add_courses_to_db
from db.models import StudentCourse
from flask_app.controllers import StudentCourseControllers, StudentControllers

session = get_session()


@pytest.fixture
def create_courses_and_students():
    add_courses_to_db(COURSES)
    StudentControllers().add_new_student("Jeremy", "Clarkson", 0)
    StudentControllers().add_new_student("Richard", "Hammond", 0)
    StudentCourseControllers().add_student_to_course({"student_id": 1, "course_id": 1})


def test_get_student_on_course(create_courses_and_students):
    students_on_course = StudentCourseControllers().get_students_on_course(
        "Biochemistry"
    )
    assert students_on_course == [
        {
            "id": 1,
            "first_name": "Jeremy",
            "last_name": "Clarkson",
            "courses": "[Biochemistry]",
            "group": "None",
        }
    ]


def test_add_student_to_course(mocker):
    """Since the validator has been replaced, an error is possible when repeating data will be added to the database.
    For this, a check was added to the test"""
    one_student_courses = (
        session.query(StudentCourse).where(StudentCourse.student_id == 2).all()
    )
    courses = list(range(1, 11))
    for student in one_student_courses:
        if student.course_id in courses:
            courses.remove(student.course_id)
    validator = mocker.patch(
        "flask_app.controllers.student_course_controllers.validate_student_on_course",
        return_value=(2, courses[0]),
    )
    new_student = StudentCourseControllers().add_student_to_course(
        {"course_id": 4, "student_id": 4}
    )
    assert new_student == [2, courses[0]]
    validator.assert_called()


def test_delete_student_from_course():
    deleted_student = StudentCourseControllers().delete_student_from_course(1, 1)
    assert deleted_student is None
