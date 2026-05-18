import pytest

from app.core.settings import UserRole
from app.core.users import (
    UserAccount,
    can_manage_users,
    change_user_role,
    create_user,
    deactivate_user,
)


def test_admin_can_manage_users():
    assert can_manage_users(UserRole.ADMIN) is True


def test_operator_cannot_manage_users():
    assert can_manage_users(UserRole.OPERATOR) is False


def test_tester_cannot_manage_users():
    assert can_manage_users(UserRole.TESTER) is False


def test_viewer_cannot_manage_users():
    assert can_manage_users(UserRole.VIEWER) is False


def test_create_user_with_role():
    user = create_user("manager1", UserRole.TESTER)

    assert isinstance(user, UserAccount)
    assert user.username == "manager1"
    assert user.role == UserRole.TESTER
    assert user.is_active is True


def test_create_user_strips_username():
    user = create_user("  manager1  ", UserRole.OPERATOR)

    assert user.username == "manager1"
    assert user.role == UserRole.OPERATOR


def test_create_user_with_empty_username_raises_error():
    with pytest.raises(ValueError):
        create_user("   ", UserRole.VIEWER)


def test_change_user_role():
    user = create_user("manager1", UserRole.TESTER)

    updated_user = change_user_role(user, UserRole.OPERATOR)

    assert updated_user.role == UserRole.OPERATOR


def test_deactivate_user():
    user = create_user("manager1", UserRole.OPERATOR)

    updated_user = deactivate_user(user)

    assert updated_user.is_active is False
