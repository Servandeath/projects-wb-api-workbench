from enum import StrEnum


class UserRole(StrEnum):
    VIEWER = "Viewer"
    TESTER = "Tester"
    OPERATOR = "Operator"
    ADMIN = "Admin"


class AppMode(StrEnum):
    TEST = "Test"
    REAL = "Real"


REAL_MODE_ALLOWED_ROLES = {
    UserRole.OPERATOR,
    UserRole.ADMIN,
}


def can_use_real_mode(role: UserRole) -> bool:
    return role in REAL_MODE_ALLOWED_ROLES


def apply_settings(role: UserRole, mode: AppMode) -> tuple[UserRole, AppMode]:
    if mode == AppMode.REAL and not can_use_real_mode(role):
        raise PermissionError(f"Role {role.value} cannot use Real mode")

    return role, mode