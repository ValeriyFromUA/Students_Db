from collections import Counter
from typing import List, Dict

from db.models import Student, Group
from flask_app.controllers import Base


class GroupControllers(Base):
    def get_all_groups(self) -> List[Dict]:
        groups = self.session.query(Group).all()
        return [group.to_dict() for group in groups]

    def find_size_of_groups(self) -> Dict:
        count_groups = self.session.query(Student.group_id).all()
        return dict(Counter(count_groups))

    def find_groups_with_the_number_of_students(self, number: int) -> List[Dict]:
        group_list = []
        for group_id, group_size in self.find_size_of_groups().items():
            if group_size <= number and group_id[0] is not None:
                group_list.append(int(group_id[0]))
        groups = self.session.query(Group).filter(Group.id.in_(group_list)).all()
        return [group.to_dict() for group in groups]
