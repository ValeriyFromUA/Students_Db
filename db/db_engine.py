from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import create_database, database_exists

from flask_app.configuration import DevelopmentConfig


def get_engine(url: str = DevelopmentConfig.DEV_DATABASE_URI) -> Engine:
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine


def get_session() -> Session:
    Session = sessionmaker(bind=get_engine())
    return Session()
