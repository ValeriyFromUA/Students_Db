from os import environ as env

VER = "v1"
ROUTE = f"/api/{VER}"


class Config:
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = False
    TESTING = False
    DATABASE_URI = env.get(
        "DATABASE_URI", default="postgresql://postgres:0@db:5432/students"
    )


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    TEST_DATABASE_URI = env.get(
        "TEST_DATABASE_URI", default="postgresql://postgres:0@db:5432/students_test"
    )
