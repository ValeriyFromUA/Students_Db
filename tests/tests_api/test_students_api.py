from http import HTTPStatus

from flask_app import ROUTE
from tests.tests_api.conftest import NEW_STUDENT, STUDENTS


def test_get_students(test_client, mocker):
    mocked_students = mocker.patch(
        "flask_app.api.students_api.StudentControllers.get_all_students",
        return_value=STUDENTS,
    )
    response = test_client.get(f"{ROUTE}/students")
    students = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert students == STUDENTS
    mocked_students.assert_called_once()


def test_post_students(test_client, mocker):
    validator = mocker.patch(
        "flask_app.api.students_api.validate_student_data",
        return_value=("First_name", "last_name", "group"),
    )
    mocked_students = mocker.patch(
        "flask_app.api.students_api.StudentControllers.add_new_student",
        return_value=NEW_STUDENT,
    )
    response = test_client.post(
        f"{ROUTE}/students",
        json={"first_name": "James", "last_name": "May", "group_id": 5},
    )
    student = response.get_json()
    assert response.status_code == HTTPStatus.CREATED
    assert student == NEW_STUDENT
    mocked_students.assert_called_once()
    validator.assert_called()


def test_post_students_bad(test_client, mocker):
    validator = mocker.patch(
        "flask_app.api.students_api.validate_student_data",
        return_value=None,
    )
    response = test_client.post(
        f"{ROUTE}/students",
        json={"first_name": "James", "last_name": "May", "group_id": 5},
    )
    student = response.get_json()
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert student == {
        "error": "Can't create student with data {'first_name': 'James', 'group_id': "
        "5, 'last_name': 'May'}"
    }
    validator.assert_called()
