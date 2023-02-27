import pytest

from db.db_engine import get_engine, get_session
from db.models import Base, Student, Course, Group, StudentCourse
from flask_app import get_logger

logger = get_logger(__name__)
session = get_session()


def refresh_db():
    session.close_all()
    Base.metadata.drop_all(bind=get_engine())
    logger.info("Dropped all")
    Base.metadata.create_all(bind=get_engine())


@pytest.fixture(scope="module", autouse=True)
def refresh_db_fixture():
    refresh_db()
    yield
    for table in [Student, Course, Group, StudentCourse]:
        session.query(table).delete()
    session.commit()
