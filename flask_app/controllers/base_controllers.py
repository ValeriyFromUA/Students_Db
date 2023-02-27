from db.db_engine import get_session
from flask_app import get_logger


class Base:
    session = get_session()
    logger = get_logger(__name__)
