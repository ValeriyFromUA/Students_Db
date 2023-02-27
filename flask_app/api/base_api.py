from flask_restful import Resource
from flask_app import get_logger


class Base(Resource):
    logger = get_logger(__name__)
