from http import HTTPStatus
from typing import List, Dict, Tuple, Union

from flask import request

from flask_app.api import Base
from flask_app.controllers import StudentControllers
from flask_app.validators import validate_student_data


class Students(Base):
    def get(self) -> List[Dict]:
        """
        Get all students or student by id if using optional argument
        ---
        responses:
          200:
            description: Info about student
            schema:
                example: [{"courses": "[Digital Humanities, Biochemistry]",
                 "first_name": "Jeremy", "group": "WZ_52", "id": 1, "last_name": "May"}]
        """

        self.logger.info("Finding all students")
        return StudentControllers().get_all_students()

    def post(self) -> Union[Tuple[Dict, HTTPStatus], Tuple[None, HTTPStatus]]:
        """
        Create new student
        ---
        parameters:
        - in: body
          name: Student
          description: Create user (change default values on name and group id )
          schema:
            type: object
            required:
              - first_name
              - last_name
              - group_id
            properties:
              first_name:
                type: string
              last_name:
                type: string
              group_id:
                type: integer
        responses:
            201:
                description: Create new student
                schema:
                    example: {"id": 205, "first_name": "string", "last_name": "string", "courses": "[]","group": "None"}
            404:
                description: expected numbers but get some letters
                schema:
                    example: {"error": "Can't create student with data {data}"}
        """
        data = request.get_json()
        if validate_student_data(data) is None:
            self.logger.error(f"error: Can't create student with data  {data} ")
            return {
                "error": f"Can't create student with data {data}"
            }, HTTPStatus.BAD_REQUEST
        first_name, last_name, group_id = validate_student_data(data)
        self.logger.info(f"Successfully created new student {data}")
        return (
            StudentControllers().add_new_student(first_name, last_name, group_id),
            HTTPStatus.CREATED,
        )
