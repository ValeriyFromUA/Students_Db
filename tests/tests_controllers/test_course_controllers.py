import pytest

from db.data_generator import COURSES
from db.db_manager import add_courses_to_db
from flask_app.controllers import CourseControllers


@pytest.fixture
def create_courses():
    add_courses_to_db(COURSES)
    yield


def test_get_all_courses(create_courses):
    courses = CourseControllers().get_all_courses()
    for course in courses:
        assert "id" in course.keys()
        assert course["course"] in COURSES
        assert course["description"] == f"description of {course['course']}"
