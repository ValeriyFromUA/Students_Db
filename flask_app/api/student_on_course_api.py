from typing import Dict, List
from flask_app.api import Base
from flask_app.controllers import StudentCourseControllers


class StudentsOnCourse(Base):
    def get(self, course_name) -> List[Dict]:
        """
            Get all courses
            ---
            parameters:
              - name: course_name
                in: path
                type: string
                required: True
                enum: ['Biochemistry', 'Chinese', 'Computer Science',
                 'Digital Humanities', 'Economics', 'French', 'Geography', 'History', 'Integrative Physiology', 'Journalism']
            responses:
              200:
                description: list of courses
                schema:
                    example: [{
            "id": 25,
            "first_name": "Emma",
            "last_name": "Davis",
            "courses": "[French, Computer Science]",
            "group": "XO_83"}
        ]
        """
        self.logger.info("Finding students on course")
        return StudentCourseControllers().get_students_on_course(course_name)
