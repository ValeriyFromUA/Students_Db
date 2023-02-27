from sqlalchemy import Column, Integer, String

from db.models.base import Base


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    course = Column(String)
    description = Column(String)

    def __repr__(self):
        return self.course

    def to_dict(self):
        return {"id": self.id, "course": self.course, "description": self.description}
