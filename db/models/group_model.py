from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.models.base import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    group_name = Column(String(50))
    student = relationship("Student", back_populates="group")

    def __repr__(self):
        return self.group_name

    def to_dict(self):
        return {"id": self.id, "group": self.group_name}
