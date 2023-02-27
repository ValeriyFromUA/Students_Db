from http import HTTPStatus
from typing import Dict, List, Tuple, Union

from flask import request

from flask_app.api import Base
from flask_app.controllers import CourseControllers, StudentCourseControllers
from flask_app.validators import validate_student_on_course


class Courses(Base):
    def get(self) -> List[Dict]:
        """
        Get all courses
        ---
        responses:
          200:
            description: list of courses
            schema:
                example: [{"id": 1,"course": "Biochemistry", "description": "description of Biochemistry"}]
        """
        self.logger.info("Finding all courses")
        return CourseControllers().get_all_courses()

    def post(self) -> [HTTPStatus, Tuple[List[int], HTTPStatus]]:
        """
        Add student to course
        ---
        parameters:
        - in: body
          name: Course
          description: Add student to course
          schema:
            type: object
            required:
              - student_id
              - course_id
            properties:
              student_id:
                type: integer
              course_id:
                type: integer
        responses:
            201:
                description: Add new student to course
                schema:
                    example: [22, 1]
            400:
                description: Add new student to course
                schema:
                    example: {'error': 'Can`t add student to course'}
        """
        data = request.get_json()
        add_data = StudentCourseControllers().add_student_to_course(data)
        if add_data is None:
            self.logger.error("Can`t add student to course")
            return {"error": "Can`t add student to course"}, HTTPStatus.BAD_REQUEST
        self.logger.info("Adding student to course")
        return [data["course_id"], data["student_id"]], HTTPStatus.CREATED

    def delete(
        self,
    ) -> Union[Tuple[Dict[str, str], HTTPStatus], Tuple[None, HTTPStatus]]:
        """
        Delete student from course
        ---
        parameters:
        - in: body
          name: Course
          description: Delete student from course
          schema:
            type: object
            required:
              - student_id
              - course_id
            properties:
              student_id:
                type: integer
              course_id:
                type: integer
        responses:
            204:
                description: Delete student_from group
                schema:
                    example:
            404:
                description: expected int but get some letters
                schema:
                    example: {
                'error': 'Can`t delete student from course, there is no student in the course'}
        """
        data = request.get_json(force=False)
        check = validate_student_on_course(data)
        if check is not None:
            self.logger.error(
                "Can`t delete student from course, there is no student in the course"
            )
            return {
                "error": "Can`t delete student from course, there is no student in the course"
            }, HTTPStatus.NOT_FOUND
        StudentCourseControllers().delete_student_from_course(
            data["course_id"], data["student_id"]
        )
        self.logger.info("Deleting student from course")
        return None, HTTPStatus.NO_CONTENT
