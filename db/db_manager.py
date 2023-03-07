from typing import List, NoReturn

from sqlalchemy import and_

from db.data_generator import COURSES, Generator
from db.db_engine import get_session
from db.models import Course, Group, Student, StudentCourse
from flask_app import get_logger

session = get_session()
logger = get_logger(__name__)


def add_courses_to_db(courses: List) -> NoReturn:
    for element in courses:
        course = Course(course=element, description=f"description of {element}")
        session.add(course)
    session.commit()
    logger.info("Courses added to db")


def add_groups_to_db(groups: List) -> NoReturn:
    for group in groups:
        group = Group(group_name=f"{group}")
        session.add(group)
        session.commit()
    logger.info("Groups added to db")


def add_students_to_db(students: List, id_list: List) -> NoReturn:
    students_list = []
    for index in range(0, len(students)):
        student = Student(
            first_name=students[index].split()[0],
            last_name=students[index].split()[1],
            group_id=id_list[index],
        )
        students_list.append(student)
    session.add_all(students_list)
    session.commit()
    logger.info("Students added to db")


def add_all_students_to_courses(student_course_list: List) -> NoReturn:
    data_to_db_list = []
    for element in student_course_list:
        if (
            session.query(StudentCourse)
            .filter(
                and_(
                    StudentCourse.course_id == element["course_id"],
                    StudentCourse.student_id == element["student_id"],
                )
            )
            .first()
            is None
        ):
            subtable = StudentCourse(
                course_id=element["course_id"], student_id=element["student_id"]
            )
            data_to_db_list.append(subtable)
    session.add_all(data_to_db_list)
    session.commit()
    logger.info("Students added to courses")


def add_generated_data_to_db() -> NoReturn:
    instance = Generator()

    groups, students, id_list, student_course_list = (
        instance.generate_groups(),
        instance.generate_200_unique_students_names(),
        instance.divide_students_into_groups(),
        instance.divide_students_into_courses(),
    )
    add_groups_to_db(groups)
    add_students_to_db(students, id_list)
    add_courses_to_db(COURSES)
    add_all_students_to_courses(student_course_list)
    logger.info("All data added to db")
