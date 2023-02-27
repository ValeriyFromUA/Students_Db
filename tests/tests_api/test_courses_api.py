from http import HTTPStatus

from flask_app import ROUTE


def test_get_courses(test_client, mocker):
    mocked_courses = mocker.patch(
        "flask_app.api.courses_api.CourseControllers.get_all_courses",
        return_value=[{"id": 1, "course": "random_course"}],
    )
    response = test_client.get(f"{ROUTE}/courses")
    courses = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert courses == [{"id": 1, "course": "random_course"}]
    mocked_courses.assert_called_once()


def test_post_courses(test_client, mocker):
    mocked_courses = mocker.patch(
        "flask_app.api.courses_api.StudentCourseControllers.add_student_to_course",
        return_value=[999, 999],
    )
    response = test_client.post(
        f"{ROUTE}/courses",
        json={
            "course_id": 7,
            "student_id": 111,
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.get_json() == [7, 111]
    mocked_courses.assert_called_once()


def test_post_courses_bad(test_client, mocker):
    mocked_courses = mocker.patch(
        "flask_app.api.courses_api.StudentCourseControllers.add_student_to_course",
        return_value=None,
    )
    response = test_client.post(
        f"{ROUTE}/courses",
        json={
            "course_id": 11,
            "student_id": 111,
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {"error": "Can`t add student to course"}
    mocked_courses.assert_called_once()


def test_delete_courses(test_client, mocker):
    mocked_validator = mocker.patch(
        "flask_app.api.courses_api.validate_student_on_course", return_value=None
    )
    response = test_client.delete(
        f"{ROUTE}/courses", json={"student_id": 111, "course_id": 7}
    )
    assert response.status_code == HTTPStatus.NO_CONTENT
    mocked_validator.assert_called_once()


def test_delete_courses_bad(test_client, mocker):
    mocked_validator = mocker.patch(
        "flask_app.api.courses_api.validate_student_on_course", return_value=(1, 2)
    )
    response = test_client.delete(
        f"{ROUTE}/courses", json={"student_id": 111, "course_id": 7}
    )
    assert response.get_json() == {
        "error": "Can`t delete student from course, there is no student in the course"
    }
    assert response.status_code == HTTPStatus.NOT_FOUND
    mocked_validator.assert_called_once()
