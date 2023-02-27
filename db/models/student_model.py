from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.models.base import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="student")
    first_name = Column(String)
    last_name = Column(String)
    courses = relationship(
        "Course", secondary="student_course", backref="student", cascade="all,delete"
    )

    def __repr__(self):
        return f"\n{self.first_name} {self.last_name}: {self.group_id}"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "courses": str(self.courses),
            "group": str(self.group),
        }
