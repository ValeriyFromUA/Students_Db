from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from db.models.base import Base


class StudentCourse(Base):
    __tablename__ = "student_course"
    __table_args__ = (PrimaryKeyConstraint("student_id", "course_id"),)
    student_id = Column(
        Integer, ForeignKey("student.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    course_id = Column(
        Integer, ForeignKey("course.id", onupdate="CASCADE", ondelete="CASCADE")
    )
