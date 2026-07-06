# WB API Workbench — checkpoint

## Как продолжить

Начать новый чат с фразы:

    Продолжаем проект WB API Workbench.
    Локальный путь: E:\projects-wb-api-workbench
    Прочитай NEXT_CHAT_CHECKPOINT.md — там актуальный статус.

## Что это за проект

Локальное desktop-приложение на Python для работы с Wildberries API.
Инструмент для менеджеров маркетплейса с разными уровнями доступа.
Портфолио-проект: внешний API, GUI, локальное хранение, безопасное
хранение ключей, ролевая модель доступа.

## Стек

Python 3.11+, customtkinter, SQLAlchemy + SQLite (слой готов, не подключён),
httpx, keyring, cryptography, pytest.

## Команды

Запуск:

    cd E:\projects-wb-api-workbench
    .\.venv\Scripts\Activate.ps1
    python -m app.main

Тесты:

    python -m pytest -q

Git:

    git status
    git add .
    git commit -m "message"
    git push

## Структура проекта

    app/
      config.py            пути, DATABASE_URL, USERS_FILE
      main.py              точка входа
      core/
        permissions.py     Role + матрица прав (отдельный enum)
        settings.py        UserRole, AppMode, apply_settings
        users.py           UserAccount + логика (create/add/find/change/deactivate)
        user_store.py      JSON-персистентность пользователей
        diagnostics.py     самопроверка окружения
        key_storage.py     ключи через keyring
        encrypted_file_storage.py  ключи в зашифрованном файле (Fernet)
        session_key_storage.py     ключ в памяти сессии
        http_client.py     WB HTTP-клиент (httpx)
      gui/
        main_window.py     основное окно, рабочие разделы
        api_tester.py      заглушка
        key_manager.py     заглушка
        json_viewer.py     заглушка
        login_window.py    заглушка
      db/
        database.py        engine, SessionLocal, init_db (не вызывается)
        models.py          ApiKey, ApiRequestLog
      storage/
        raw_json.py        сохранение raw JSON
    tests/                 permissions, settings, users, user_store, diagnostics
    docs/                  architecture, permissions, roadmap

## Текущее состояние (v0.3 / GUI MVP в работе)

Core — готово и покрыто тестами:
- ролевая модель (Viewer / Tester / Operator / Admin) и матрица прав;
- режимы Test / Real с правилом доступа к Real;
- логика пользователей: создание, защита от дублей (без учёта регистра),
  поиск, смена роли, деактивация;
- JSON-персистентность пользователей (user_store);
- диагностика окружения;
- три варианта хранения ключей (keyring / шифрованный файл / сессия).
- декодер JWT-ключей WB (wb_token): читает из токена кабинет (oid), тип,
  права по битам (scopes), срок действия — мост между ролями и правами WB API.

GUI — рабочие разделы:
- каркас приложения (sidebar, topbar, статус Role/Mode/Key);
- Diagnostics (кнопка Run Diagnostics);
- Settings (выбор роли и режима, проверка запрещённых комбинаций);
- Users (полностью рабочий): создание с защитой от дублей,
  смена роли, деактивация, сохранение в JSON, загрузка при старте,
  автосоздание admin если файла нет.

Пользователи переживают перезапуск приложения (data/users.json,
в .gitignore — локальные данные).

Тесты: 44 passed.

## Заглушки / не подключено

- GUI: API Tester, Keys, Imports, History (плейсхолдеры);
- БД-слой написан (models + database), но init_db нигде не вызывается,
  репозитория нет — пользователи пока в JSON, не в SQLite;
- http_client готов, но из GUI не используется.

## Известные проблемы и бэклог

- Users: список пользователей без скроллбара, обрезается в маленьком окне
  (в полный экран видно). Быстрая добивка: CTkScrollableFrame.
- Два параллельных enum ролей: settings.UserRole ("Viewer"...) и
  permissions.Role ("viewer"...). Риск рассинхрона, стоит свести к одному.
- БД-слой мёртв — решить, когда users/ключи реально переезжают в SQLite.

## Ошибки, найденные и исправленные по ходу

- В рабочей копии были порезаны users.py и test_users.py (потеряна логика
  дублей и часть тестов) — восстановлено.
- 4 нерабочих GUI-черновика (users_gui_*.py) ссылались на несуществующие
  модули — удалены.
- Двойной append при создании пользователя в GUI — убран.
- В GUI вызывался create_user вместо add_user (не ловил дубли,
  не добавлял в список) — заменён на add_user.

## Правила работы

- Маленькими шагами: обсудить -> маленький блок кода -> запустить ->
  исправить -> закоммитить.
- Для каждого раздела: core-логика + pytest-тесты + проверка в GUI.
- Команды для PowerShell, по одной за раз.

## Раздел Keys (в работе)

Цель: админка учёта и контроля ключей доступа к WB API.
Ключ WB = JWT-токен, права зашиты внутри (поле s, bitmask).

Сделано:
- wb_token.py — декодер токена (oid, тип, scopes, срок, read-only, активность),
  покрыт тестами на реальном токене как золотом образце.

Дальше по кирпичам (снизу вверх):
1. Хранение ключей: token_info + имя от пользователя + oid,
   зашифрованно (encrypted_file_storage уже готов). Зеркало user_store.
2. Пинг живости: httpx дёргает /ping каждого раздела (200/401/403/429).
3. GUI-раздел Keys: вставил токен -> увидел права/срок -> задал имя -> сохранил.
   При добавлении спрашивать имя, подсказывать ранее использованные по oid.

## Следующий шаг

Быстрая добивка: скролл в списке Users.
Крупный этап: хранение ключей (кирпич 1 раздела Keys) — на готовый декодер
навесить сохранение зашифрованных ключей с именем и привязкой к кабинету.