import pytest

from db.db_engine import get_session
from db.db_manager import add_groups_to_db
from db.models import Student
from flask_app.controllers import StudentControllers
from tests.tests_controllers.conftest import STUDENT_3, STUDENTS, STUDENT


@pytest.fixture
def create_students():
    add_groups_to_db(["group_1"])
    StudentControllers().add_new_student("Jeremy", "Clarkson", 0)
    StudentControllers().add_new_student("Richard", "Hammond", 0)


def test_get_all_students(create_students):
    result = StudentControllers().get_all_students()
    assert result == STUDENTS


def test_get_student_by_id(mocker):
    validator = mocker.patch(
        "flask_app.controllers.student_controllers.student_validator",
        return_value=STUDENT,
    )
    student = StudentControllers().get_student_by_id(2)
    assert student == STUDENTS[1]
    validator.assert_called_once()


def test_get_non_existing_student_by_id(mocker):
    validator = mocker.patch(
        "flask_app.controllers.student_controllers.student_validator", return_value=None
    )
    student = StudentControllers().get_student_by_id(999)
    assert student is None
    validator.assert_called_once()


def test_delete_student_by_id(mocker):
    session = get_session()
    new_student = Student(first_name="Richard", last_name="Hammond", group_id=1)
    session.add(new_student)
    session.commit()
    validator = mocker.patch(
        "flask_app.controllers.student_controllers.student_validator",
        return_value=STUDENT,
    )
    deleted_student = StudentControllers().delete_student_by_id(new_student.id)
    assert deleted_student is None
    validator.assert_called_once()


def test_delete_non_existing_student_by_id(mocker):
    validator = mocker.patch(
        "flask_app.controllers.student_controllers.student_validator", return_value=None
    )
    deleted_student = StudentControllers().delete_student_by_id(999)
    assert deleted_student == 999
    validator.assert_called_once()


def test_add_new_student(refresh_db_fixture, create_students, mocker):
    validator = mocker.patch(
        "flask_app.controllers.student_controllers.group_validator", return_value=1
    )
    student = StudentControllers().add_new_student("James", "May", 1)
    assert student == STUDENT_3
    validator.assert_called_once()
