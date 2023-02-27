from http import HTTPStatus
from typing import Dict, Tuple, Union

from flask_app.api import Base
from flask_app.controllers import StudentControllers
from flask_app.validators import student_validator


class Student(Base):
    def get(
        self, student_id: int
    ) -> Union[Tuple[Dict[str, str], HTTPStatus], Tuple[None, HTTPStatus]]:
        """
        Get all students or student by id if using optional argument
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: false
        responses:
          200:
            description: Info about student
            schema:
                example: {"id": 205, "first_name": "string", "last_name": "string", "courses": "[]","group": "QE_21"}
          404:
            description: Student not exist
            schema:
                example: {"error": "Student with id 5 not exist"}
        """
        student = student_validator(int(student_id))
        if student is None:
            self.logger.error(f"error: Student with id {student_id} not exist")
            return {
                "error": f"Student with id {student_id} not exist"
            }, HTTPStatus.NOT_FOUND
        self.logger.info(f"Finding student with id: {student_id}")
        return student.to_dict()

    def delete(
        self, student_id: int
    ) -> Union[Tuple[Dict[str, str], HTTPStatus], Tuple[None, HTTPStatus]]:
        """
        Delete student by id
        ---
        parameters:
          - name: student_id
            in: path
            type: integer
            required: true
        responses:
          204:
            description: Delete student by id
          404:
            description: expected numbers but get some letters
            schema:
                example: {"error": "Student #5 not deleted"}
        """
        response = StudentControllers().delete_student_by_id(student_id)
        if response is not None:
            self.logger.info(f"Student #{student_id} not deleted")
            return {"error": f"Student #{student_id} not deleted"}, HTTPStatus.NOT_FOUND
        self.logger.info(f" Student #{student_id} was deleted")
        return None, HTTPStatus.NO_CONTENT
