# --- Интеграция JSON-функций в GUI Users ---

from app.gui import users_integration
from app.core.users import UserAccount

# Предполагаем, что есть класс UsersFrame в main_window.py
# Ниже добавляем методы для кнопок

def on_add_user(self):
    username = self.username_entry.get()
    role = self.role_combobox.get()
    if not username or not role:
        self.show_error("Введите имя пользователя и роль")
        return
    if users_integration.add_user_gui(username, role):
        self.refresh_user_list()
        self.show_toast(f"Пользователь {username} добавлен")
    else:
        self.show_error(f"Пользователь {username} уже существует")

def on_change_role(self):
    selected_user = self.get_selected_user()
    if not selected_user:
        self.show_error("Выберите пользователя")
        return
    new_role = self.role_combobox.get()
    if users_integration.change_role_gui(selected_user.username, new_role):
        self.refresh_user_list()
        self.show_toast(f"Роль пользователя {selected_user.username} изменена на {new_role}")
    else:
        self.show_error("Ошибка изменения роли")

def on_deactivate_user(self):
    selected_user = self.get_selected_user()
    if not selected_user:
        self.show_error("Выберите пользователя")
        return
    if users_integration.deactivate_user_gui(selected_user.username):
        self.refresh_user_list()
        self.show_toast(f"Пользователь {selected_user.username} деактивирован")
    else:
        self.show_error("Ошибка деактивации пользователя")

# Привязка методов к кнопкам (пример)
# self.add_button.config(command=self.on_add_user)
# self.change_role_button.config(command=self.on_change_role)
# self.deactivate_button.config(command=self.on_deactivate_user)
