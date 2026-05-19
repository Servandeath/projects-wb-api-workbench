# --- Тест GUI Users с JSON-хранилищем ---

from app.gui import users_integration

# Функция для печати всех пользователей
def print_users():
    print("Текущий список пользователей:")
    for u in users_integration.user_accounts:
        status = "Active" if u.is_active else "Inactive"
        print(f" - {u.username} | {u.role} | {status}")
    print("")

# 1. Добавляем нового пользователя
print("Добавляем пользователя 'test_user1' с ролью 'Tester'")
if users_integration.add_user_gui("test_user1", "Tester"):
    print("Пользователь добавлен успешно.")
else:
    print("Пользователь уже существует.")
print_users()

# 2. Пробуем добавить того же пользователя повторно
print("Пробуем добавить 'test_user1' повторно")
if users_integration.add_user_gui("test_user1", "Operator"):
    print("Пользователь добавлен успешно.")
else:
    print("Пользователь уже существует.")
print_users()

# 3. Изменяем роль пользователя
print("Меняем роль 'test_user1' на 'Admin'")
if users_integration.change_role_gui("test_user1", "Admin"):
    print("Роль изменена успешно.")
else:
    print("Ошибка изменения роли.")
print_users()

# 4. Деактивируем пользователя
print("Деактивируем пользователя 'test_user1'")
if users_integration.deactivate_user_gui("test_user1"):
    print("Пользователь деактивирован.")
else:
    print("Ошибка деактивации.")
print_users()
