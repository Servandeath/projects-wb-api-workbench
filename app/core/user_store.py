import json
from pathlib import Path

from app.core.settings import UserRole
from app.core.users import UserAccount


def user_to_dict(user: UserAccount) -> dict:
    return {
        "username": user.username,
        "role": user.role.value,
        "is_active": user.is_active,
    }


def user_from_dict(data: dict) -> UserAccount:
    return UserAccount(
        username=data["username"],
        role=UserRole(data["role"]),
        is_active=data.get("is_active", True),
    )


def load_users(path: Path) -> list[UserAccount]:
    path = Path(path)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [user_from_dict(item) for item in data]


def save_users(path: Path, users: list[UserAccount]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [user_to_dict(user) for user in users]

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)