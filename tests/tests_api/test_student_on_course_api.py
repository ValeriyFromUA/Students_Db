from http import HTTPStatus

from flask_app import ROUTE
from tests.tests_api.conftest import STUDENTS


def test_get_student_on_course(test_client, mocker):
    mocked_students = mocker.patch(
        "flask_app.api.student_on_course_api.StudentCourseControllers.get_students_on_course",
        return_value=STUDENTS,
    )
    response = test_client.get(f"{ROUTE}/courses/Bio/")
    students = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert students == STUDENTS
    mocked_students.assert_called_once()
