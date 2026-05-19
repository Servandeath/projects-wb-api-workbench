import json
from pathlib import Path
from app.core.users import UserAccount

def user_to_dict(user: UserAccount) -> dict:
    return {"username": user.username, "role": user.role, "is_active": user.is_active}

def user_from_dict(data: dict) -> UserAccount:
    return UserAccount(username=data["username"], role=data["role"], is_active=data.get("is_active", True))

def load_users(path: str):
    file_path = Path(path)
    if not file_path.exists(): return []
    with file_path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    return [user_from_dict(u) for u in data]

def save_users(path: str, users):
    file_path = Path(path)
    with file_path.open("w", encoding="utf-8") as f:
        json.dump([user_to_dict(u) for u in users], f, indent=4, ensure_ascii=False)

def add_user_to_store(path: str, user: UserAccount):
    users = load_users(path)
    if any(u.username.lower() == user.username.lower() for u in users): return False
    users.append(user)
    save_users(path, users)
    return True

def update_user_role(path: str, username: str, new_role: str):
    users = load_users(path)
    for u in users:
        if u.username.lower() == username.lower():
            u.role = new_role
            save_users(path, users)
            return True
    return False

def deactivate_user_in_store(path: str, username: str):
    users = load_users(path)
    for u in users:
        if u.username.lower() == username.lower():
            u.is_active = False
            save_users(path, users)
            return True
    return False
