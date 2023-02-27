from typing import Dict, List

from flask import request

from flask_app.api import Base
from flask_app.controllers import GroupControllers


class Groups(Base):
    def get(self) -> List[Dict]:
        """
        Get all groups or group with less than "X" members, if using optional argument
        ---
        parameters:
          - name: students_count
            in: query
            type: integer
            required: false
        responses:
          200:
            description: list of groups
            schema:
                example: [{"group": "WZ_52","id": 1},{"group": "HD_96","id": 2}]
        """
        students_count = request.args.get("students_count")
        if students_count:
            self.logger.info("Successfully counted students in groups")
            return GroupControllers().find_groups_with_the_number_of_students(
                int(students_count)
            )
        self.logger.info("Finding all groups")
        return GroupControllers().get_all_groups()
