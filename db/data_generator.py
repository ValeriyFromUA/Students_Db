import string
from random import choice, randint, randrange
from typing import Dict, List

FIRST_NAMES = [
    "Eleanora",
    "James",
    "Robert",
    "John",
    "Michael",
    "Jeremy",
    "Richard",
    "Mark",
    "David",
    "William",
    "Joseph",
    "Olivia",
    "Emma",
    "Isabella",
    "Mia",
    "Evelyn",
    "Harper",
    "Charlotte",
    "Noah",
    "Liam",
]
LAST_NAMES = [
    "May",
    "Clarkson",
    "Hammond",
    "Blue",
    "Green",
    "Gray",
    "White",
    "Black",
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Jackson",
    "Bad",
]

COURSES = [
    "Biochemistry",
    "Chinese",
    "Computer Science",
    "Digital Humanities",
    "Economics",
    "French",
    "Geography",
    "History",
    "Integrative Physiology",
    "Journalism",
]
GROUPS_IDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None]


class Generator:
    @staticmethod
    def generate_200_unique_students_names() -> List[str]:
        students_list = []
        while len(students_list) < 200:
            student = f"{choice(FIRST_NAMES)}" f" {choice(LAST_NAMES)}"
            if student not in students_list:
                students_list.append(student)
        return students_list

    @staticmethod
    def generate_groups() -> List[str]:
        groups = []
        while len(groups) < 10:
            group = (
                f"{choice(string.ascii_letters)}{choice(string.ascii_letters)}_{randrange(0, 10)}"
                f"{randrange(0, 10)}"
            )
            if group not in groups:
                groups.append(group.upper())
        return groups

    @staticmethod
    def divide_students_into_groups() -> List[int]:
        id_list = []
        for id_ in GROUPS_IDS:
            for group_length in range(randint(15, 30)):
                id_list.append(id_)
        id_list = id_list[0:200]
        return id_list

    @staticmethod
    def divide_students_into_courses() -> List[Dict]:
        student_course_list = []
        for random_student in range(1, 201):
            for _ in range(randint(1, 3)):
                random_course = randint(1, 10)
                data = {"student_id": random_student, "course_id": random_course}
                if data not in student_course_list:
                    student_course_list.append(data)
        return student_course_list
