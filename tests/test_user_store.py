from app.core.settings import UserRole
from app.core.user_store import (
    load_users,
    save_users,
    user_from_dict,
    user_to_dict,
)
from app.core.users import UserAccount


def test_user_to_dict():
    user = UserAccount(username="manager1", role=UserRole.TESTER)

    data = user_to_dict(user)

    assert data == {
        "username": "manager1",
        "role": "Tester",
        "is_active": True,
    }


def test_user_from_dict():
    data = {"username": "manager1", "role": "Operator", "is_active": False}

    user = user_from_dict(data)

    assert isinstance(user, UserAccount)
    assert user.username == "manager1"
    assert user.role == UserRole.OPERATOR
    assert user.is_active is False


def test_user_from_dict_defaults_is_active_true():
    data = {"username": "manager1", "role": "Viewer"}

    user = user_from_dict(data)

    assert user.is_active is True


def test_load_users_returns_empty_list_when_file_missing(tmp_path):
    path = tmp_path / "users.json"

    assert load_users(path) == []


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "users.json"
    users = [
        UserAccount(username="admin", role=UserRole.ADMIN),
        UserAccount(username="manager1", role=UserRole.TESTER, is_active=False),
    ]

    save_users(path, users)
    loaded = load_users(path)

    assert loaded == users


def test_save_creates_parent_directory(tmp_path):
    path = tmp_path / "nested" / "users.json"
    users = [UserAccount(username="admin", role=UserRole.ADMIN)]

    save_users(path, users)

    assert path.exists()


def test_save_users_empty_list(tmp_path):
    path = tmp_path / "users.json"

    save_users(path, [])

    assert load_users(path) == []