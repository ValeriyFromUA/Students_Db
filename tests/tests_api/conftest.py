import pytest

from db.models import Student
from flask_app.app import create_app
from flask_app.configuration import TestingConfig


@pytest.fixture(scope="module")
def test_client():
    app = create_app(TestingConfig)
    yield app.test_client()


STUDENTS = [
    {
        "id": 999,
        "first_name": "James",
        "last_name": "May",
        "courses": "[]",
        "group": "None",
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Ray",
        "courses": "[Chinese]",
        "group": "RK_06",
    },
]
STUDENT_0 = Student(id=999, first_name="James", last_name="May")
NEW_STUDENT = {
    "id": 209,
    "first_name": "James",
    "last_name": "May",
    "courses": "[]",
    "group": "YO_42",
}
