import pytest

from db.db_manager import add_groups_to_db
from flask_app.controllers import GroupControllers


@pytest.fixture
def create_groups():
    add_groups_to_db(["group_1"])


def test_get_all_groups(create_groups):
    group_list = GroupControllers().get_all_groups()
    assert group_list == [{"id": 1, "group": "group_1"}]


def test_find_size_of_groups(create_groups):
    result = GroupControllers().find_size_of_groups()
    for group_id, groups_size in result.items():
        assert group_id[0] > 0


def test_find_groups_with_the_number_of_students(mocker):
    find_size = mocker.patch(
        "flask_app.controllers.group_controllers.GroupControllers.find_size_of_groups",
        return_value={
            (1,): 36,
            (2,): 27,
            (3,): 24,
            (4,): 18,
            (5,): 22,
            (6,): 16,
            (7,): 30,
            (8,): 20,
            (9,): 20,
        },
    )
    result = GroupControllers().find_groups_with_the_number_of_students(16)
    find_size.assert_called_once()
    for group in result:
        assert group["id"] == 6
        assert "group" in group.keys()
