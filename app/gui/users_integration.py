# --- Интеграция JSON-хранилища в GUI Users ---

from app.core import user_store

# Путь к JSON-хранилищу
users_file_path = r"app\storage\users.json"

# Загружаем пользователей при запуске GUI
def load_users_from_json():
    global user_accounts
    user_accounts = user_store.load_users(users_file_path)

# Добавление нового пользователя через JSON
def add_user_gui(username: str, role: str) -> bool:
    user = user_store.UserAccount(username=username, role=role)
    result = user_store.add_user_to_store(users_file_path, user)
    if result:
        load_users_from_json()  # обновляем список в памяти
    return result

# Смена роли пользователя через GUI
def change_role_gui(username: str, new_role: str) -> bool:
    result = user_store.update_user_role(users_file_path, username, new_role)
    if result:
        load_users_from_json()
    return result

# Деактивация пользователя через GUI
def deactivate_user_gui(username: str) -> bool:
    result = user_store.deactivate_user_in_store(users_file_path, username)
    if result:
        load_users_from_json()
    return result

# Инициализация списка пользователей при старте GUI
load_users_from_json()
