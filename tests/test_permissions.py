from app.core.permissions import Role, has_permission


def test_admin_can_add_key():
    assert has_permission(Role.ADMIN, "add_key") is True


def test_viewer_cannot_add_key():
    assert has_permission(Role.VIEWER, "add_key") is False
