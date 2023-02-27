from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from flask_app.configuration import ROUTE
from flask_app.api import Courses, Groups, Student, Students, StudentsOnCourse


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    Swagger(app)
    api.add_resource(Students, f"{ROUTE}/students", endpoint="students")
    api.add_resource(Student, f"{ROUTE}/students/<student_id>/", endpoint="student")
    api.add_resource(Groups, f"{ROUTE}/groups", endpoint="groups")
    api.add_resource(Courses, f"{ROUTE}/courses", endpoint="courses")
    api.add_resource(
        StudentsOnCourse,
        f"{ROUTE}/courses/<course_name>/",
        endpoint="student_on_courses",
    )
    return app
