from http import HTTPStatus
from random import randint

from flask_app import ROUTE
from tests.tests_api.conftest import STUDENT_0, STUDENTS


def test_get_student(test_client, mocker):
    mocked_validator = mocker.patch(
        "flask_app.api.student_api.student_validator", return_value=STUDENT_0
    )
    response = test_client.get(f"{ROUTE}/students/123/")
    student = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert student == STUDENTS[0]
    mocked_validator.assert_called_once()


def test_get_student_bad(test_client, mocker):
    mocked_validator = mocker.patch(
        "flask_app.api.student_api.student_validator", return_value=None
    )
    response = test_client.get(f"{ROUTE}/students/123/")
    student = response.get_json()
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert student == {"error": f"Student with id 123 not exist"}
    mocked_validator.assert_called_once()


def test_delete_student(test_client, mocker):
    mocked_delete = mocker.patch(
        "flask_app.api.student_api.StudentControllers.delete_student_by_id",
        return_value=None,
    )
    response = test_client.delete(f"{ROUTE}/students/{randint(50, 99)}/")
    assert response.status_code == HTTPStatus.NO_CONTENT
    mocked_delete.assert_called_once()


def test_delete_student_bad(test_client, mocker):
    mocked_delete = mocker.patch(
        "flask_app.api.student_api.StudentControllers.delete_student_by_id",
        return_value=5,
    )
    response = test_client.delete(f"{ROUTE}/students/14/")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.get_json() == {"error": f"Student #14 not deleted"}
    mocked_delete.assert_called_once()
