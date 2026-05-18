import pytest

from app.core.settings import AppMode, UserRole, apply_settings, can_use_real_mode


def test_viewer_cannot_use_real_mode():
    assert can_use_real_mode(UserRole.VIEWER) is False


def test_tester_cannot_use_real_mode():
    assert can_use_real_mode(UserRole.TESTER) is False


def test_operator_can_use_real_mode():
    assert can_use_real_mode(UserRole.OPERATOR) is True


def test_admin_can_use_real_mode():
    assert can_use_real_mode(UserRole.ADMIN) is True


def test_apply_test_mode_for_tester():
    role, mode = apply_settings(UserRole.TESTER, AppMode.TEST)

    assert role == UserRole.TESTER
    assert mode == AppMode.TEST


def test_apply_real_mode_for_operator():
    role, mode = apply_settings(UserRole.OPERATOR, AppMode.REAL)

    assert role == UserRole.OPERATOR
    assert mode == AppMode.REAL


def test_apply_real_mode_for_tester_raises_error():
    with pytest.raises(PermissionError):
        apply_settings(UserRole.TESTER, AppMode.REAL)