from db.models import Student
from flask_app import get_logger

logger = get_logger(__name__)
STUDENT = Student(id=2, first_name="Richard", last_name="Hammond")
STUDENTS = [
    {
        "id": 1,
        "first_name": "Jeremy",
        "last_name": "Clarkson",
        "courses": "[]",
        "group": "None",
    },
    {
        "id": 2,
        "first_name": "Richard",
        "last_name": "Hammond",
        "courses": "[]",
        "group": "None",
    },
]
STUDENT_3 = {
    "id": 6,
    "first_name": "James",
    "last_name": "May",
    "courses": "[]",
    "group": "group_1",
}
