from sqlalchemy.orm import declarative_base

from db.db_engine import get_engine
from flask_app import get_logger

logger = get_logger(__name__)
Base = declarative_base()


def create_models():
    Base.metadata.create_all(bind=get_engine())
    logger.info("Created models")
