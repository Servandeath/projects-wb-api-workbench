from dataclasses import dataclass

from app.core.settings import UserRole


@dataclass
class UserAccount:
    username: str
    role: UserRole
    is_active: bool = True


def can_manage_users(role: UserRole) -> bool:
    return role == UserRole.ADMIN


def create_user(username: str, role: UserRole) -> UserAccount:
    if not username.strip():
        raise ValueError("Username cannot be empty")

    return UserAccount(username=username.strip(), role=role)


def change_user_role(user: UserAccount, new_role: UserRole) -> UserAccount:
    user.role = new_role
    return user


def deactivate_user(user: UserAccount) -> UserAccount:
    user.is_active = False
    return user
