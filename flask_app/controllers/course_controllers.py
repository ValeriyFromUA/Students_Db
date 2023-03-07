from typing import Dict, List

from db.models import Course
from flask_app.controllers import Base


class CourseControllers(Base):
    def get_all_courses(self) -> List[Dict]:
        courses = self.session.query(Course).all()
        return [course.to_dict() for course in courses]
