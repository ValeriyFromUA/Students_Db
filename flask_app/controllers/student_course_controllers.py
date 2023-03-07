from typing import Dict, List, NoReturn, Optional

from db.models import Course, Student, StudentCourse
from flask_app.controllers import Base
from flask_app.validators import validate_student_on_course


class StudentCourseControllers(Base):
    def add_student_to_course(self, data: Dict) -> Optional[List[int]]:
        if validate_student_on_course(data) is None:
            return
        student_id, course_id = validate_student_on_course(data)
        subtable = StudentCourse(course_id=course_id, student_id=student_id)
        self.session.add(subtable)
        self.session.commit()
        return [subtable.student_id, subtable.course_id]

    def delete_student_from_course(self, course_id: int, student_id: int) -> NoReturn:
        deleting_data = self.session.query(StudentCourse).where(
            StudentCourse.student_id == student_id, StudentCourse.course_id == course_id
        )

        deleting_data.delete()
        self.session.commit()

    def get_students_on_course(self, course: str) -> List[Dict]:
        course_query = (
            self.session.query(Student, Course)
            .outerjoin(Course, Student.courses)
            .filter(Course.course.like(f"{course}%"))
            .all()
        )
        return [student.to_dict() for student, course in course_query]
