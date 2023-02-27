from unittest.mock import patch

import pytest

from db.data_generator import COURSES, Generator
from db.db_engine import get_session
from db.db_manager import (
    add_courses_to_db,
    add_groups_to_db,
    add_students_to_db,
    add_all_students_to_courses,
    add_generated_data_to_db,
)
from db.models import StudentCourse, Group, Course, Student
from flask_app.controllers import (
    CourseControllers,
    GroupControllers,
    StudentControllers,
    StudentCourseControllers,
)
from tests.conftest import refresh_db

instance = Generator()


@pytest.fixture
def delete_data():
    session = get_session()
    for table in [Student, Course, Group, StudentCourse]:
        session.query(table).delete()


@pytest.fixture
def add_random_groups_to_db():
    add_groups_to_db(instance.generate_groups())
    yield


@pytest.fixture
def create_courses_and_students():
    refresh_db()
    add_courses_to_db(COURSES)
    StudentControllers().add_new_student("Jeremy", "Clarkson", 0)
    StudentCourseControllers().add_student_to_course({"student_id": 1, "course_id": 1})


@pytest.fixture
def clear_data_in_db():
    refresh_db()


def test_add_course_to_db():
    add_courses_to_db(COURSES)
    result = CourseControllers().get_all_courses()
    for data_string in result:
        assert data_string["course"] in COURSES
        assert data_string["description"] == f"description of {data_string['course']}"


def test_add_groups_to_db():
    add_groups_to_db(groups := instance.generate_groups())
    result = GroupControllers().get_all_groups()
    for data_string in result:
        assert data_string["group"] in groups


def test_add_students_to_db(add_random_groups_to_db):
    add_students_to_db(
        instance.generate_200_unique_students_names(),
        instance.divide_students_into_groups(),
    )
    result = StudentControllers().get_all_students()
    assert len(result) == 200
    for student in result:
        assert "first_name" in student.keys()
        assert "last_name" in student.keys()
        assert "group" in student.keys()


def test_add_all_students_to_courses(clear_data_in_db, create_courses_and_students):
    add_all_students_to_courses([{"student_id": 1, "course_id": 1}])
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


@patch("db.db_manager.Generator.generate_groups", return_value=["group_1"])
@patch(
    "db.db_manager.Generator.generate_200_unique_students_names",
    return_value=["Py Charm"],
)
@patch("db.db_manager.Generator.divide_students_into_groups", return_value=[1])
@patch(
    "db.db_manager.Generator.divide_students_into_courses",
    return_value=[{"student_id": 1, "course_id": 1}],
)
def test_add_generated_data_to_db(
    mock_group, mock_students, mock_courses, mock_student_course, clear_data_in_db
):
    add_generated_data_to_db()
    result = StudentControllers().get_all_students()
    assert result == [
        {
            "id": 1,
            "first_name": "Py",
            "last_name": "Charm",
            "courses": "[Biochemistry]",
            "group": "group_1",
        }
    ]
    assert mock_group.called_once()
    assert mock_students.called_once()
    assert mock_courses.called_once()
    assert mock_student_course.called_once()
