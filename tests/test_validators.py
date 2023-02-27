import pytest

from db.db_engine import get_session
from db.models import Student, StudentCourse
from flask_app.controllers import StudentControllers
from flask_app.validators import (
    group_validator,
    student_validator,
    validate_student_data,
    validate_student_on_course,
)

STUDENT = Student(id=999, first_name="James", last_name="May")


@pytest.fixture
def create_students_for_validate():
    StudentControllers().add_new_student("Jeremy", "Clarkson", 0)


def test_student_validator(create_students_for_validate):
    student = student_validator(1)
    student = student.to_dict()
    assert student == {
        "id": 1,
        "first_name": "Jeremy",
        "last_name": "Clarkson",
        "courses": "[]",
        "group": "None",
    }


def test_not_exist_student_validator():
    student = student_validator(999)
    assert student is None


def test_validate_student_data_good():
    data = {"first_name": "James", "last_name": "May", "group_id": 2}
    result = validate_student_data(data)
    assert result == ("James", "May", 2)


def test_validate_student_data_bad():
    data = {"First_name": "James", "Last_name": "May", "group_id": 2}
    result = validate_student_data(data)
    assert result is None


@pytest.mark.parametrize("_id", [1, 5, 10])
def test_group_validator_good(_id):
    group_id = group_validator(_id)
    assert group_id == _id


@pytest.mark.parametrize("_id", [0, -5, 11])
def test_group_validator_bad(_id):
    group_id = group_validator(_id)
    assert group_id is None


def test_validate_student_on_course(mocker):
    """Since data generated randomly we need to check courses for current student to use it as we need"""
    session = get_session()
    validator = mocker.patch(
        "flask_app.validators.student_validator", return_value=STUDENT
    )
    one_student_courses = (
        session.query(StudentCourse).where(StudentCourse.student_id == 5).all()
    )
    courses = list(range(1, 11))
    for student in one_student_courses:
        if student.course_id in courses:
            courses.remove(student.course_id)
    result = validate_student_on_course({"course_id": courses[0], "student_id": 5})
    assert result == (5, courses[0])
    assert validator.call_count == 1


def test_validate_student_on_course_fail():
    result = validate_student_on_course({"course_id": 2, "student_id": 250})
    assert result is None
