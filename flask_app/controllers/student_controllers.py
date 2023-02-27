from typing import List, Dict, Optional

from db.models import Student
from flask_app.controllers import Base
from flask_app.validators import student_validator, group_validator


class StudentControllers(Base):
    def get_all_students(self) -> List[Dict]:
        students = self.session.query(Student).all()
        return [student.to_dict() for student in students]

    @staticmethod
    def get_student_by_id(student_id: int) -> Optional[Dict]:
        student = student_validator(student_id)
        if not student:
            return
        return student.to_dict()

    def delete_student_by_id(self, student_id: int) -> Optional[int]:
        if student_validator(student_id) is None:
            return student_id
        self.session.query(Student).filter_by(id=student_id).delete()
        self.session.commit()

    def add_new_student(self, first_name: str, last_name: str, group_id: int) -> Dict:
        student = Student(
            first_name=first_name,
            last_name=last_name,
            group_id=group_validator(group_id),
        )
        self.session.add(student)
        self.session.commit()
        return student.to_dict()
