from http import HTTPStatus

from flask_app import ROUTE


def test_get_groups(test_client, mocker):
    mocked_groups = mocker.patch(
        "flask_app.api.groups_api.GroupControllers.get_all_groups",
        return_value=[{"id": 1, "group": "random_group"}],
    )
    response = test_client.get(f"{ROUTE}/groups")
    groups = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert groups == [{"id": 1, "group": "random_group"}]
    mocked_groups.assert_called_once()


def test_get_group_with_n_students(test_client, mocker):
    mocked_groups = mocker.patch(
        "flask_app.api.groups_api.GroupControllers.find_groups_with_the_number_of_students",
        return_value=[{"id": 1, "group": "random_group"}],
    )
    response = test_client.get(f"{ROUTE}/groups?students_count=15")
    groups = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert groups == [{"id": 1, "group": "random_group"}]
    mocked_groups.assert_called_once()
