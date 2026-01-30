"""
01_setup_and_models.py
======================
Проверка подключения к БД и существования таблиц.
Запуск: python 01_setup_and_models.py
"""


from sqlalchemy import text
from models import engine, metadata


print("=" * 60)
print("Шаг 1: Подключение к базе данных и проверка схемы")
print("=" * 60)

# Проверяем, что таблицы созданы в БД
with engine.connect() as conn:
    result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"))
    tables = [row[0] for row in result]

print("\n Таблицы в базе данных:")
for table in tables:
    print(f" - {table}")

