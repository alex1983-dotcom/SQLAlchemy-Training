"""
Схема базы данных для автосервиса.
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime, UTC

# Создаём РЕАЛЬНУЮ базу данных в файле (не :memory:)
# Файл будет создан автоматически в той же папке при первом запуске
engine = create_engine("sqlite:///autorepair.db", echo=False)
metadata = MetaData()

# ================================================
# Таблица: Клиенты
# ================================================
clients = Table(
    "clients", metadata,  # ← БЕЗ пробелов!
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("phone", String(20), unique=True),
    Column("email", String(100)),
    Column("created_at", DateTime, default=lambda: datetime.now(UTC))
)

# ================================================
# Таблица: Автомобили (связь один-ко-многим с клиентами)
# ================================================
cars = Table(
    "cars", metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.id"), nullable=False),
    Column("brand", String(30), nullable=False),
    Column("model", String(30), nullable=False),
    Column("year", Integer),
    Column("vin", String(17), unique=True, nullable=False),
    Column("mileage", Integer, default=0)
)

# ================================================
# Таблица: Услуги (справочник)
# ================================================
services = Table(
    "services", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("price", Float, nullable=False),
    Column("category", String(30)),  # diagnostic, repair, maintenance
    Column("duration_hours", Float, default=1.0)
)

# ================================================
# Таблица: Механики
# ================================================
mechanics = Table(
    "mechanics", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("specialization", String(50)),
    Column("hourly_rate", Float, default=1000.0)
)

# ================================================
# Таблица: Заказы (связи с клиентом, авто, механиком)
# ================================================
orders = Table(
    "orders", metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.id"), nullable=False),
    Column("car_id", Integer, ForeignKey("cars.id"), nullable=False),
    Column("mechanic_id", Integer, ForeignKey("mechanics.id")),
    Column("order_date", DateTime, default=lambda: datetime.now(UTC)),
    Column("completion_date", DateTime),
    Column("status", String(20), default="created"),  # created, in_progress, completed
    Column("priority", String(10), default="normal"),  # low, normal, high, urgent
    Column("total_amount", Float, default=0.0)
)

# ================================================
# Таблица: Связь заказов с услугами (многие-ко-многим)
# ================================================
order_services = Table(
    "order_services", metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("service_id", Integer, ForeignKey("services.id"), primary_key=True),
    Column("quantity", Integer, default=1),
    Column("subtotal", Float),
    Column("discount_percent", Float, default=0.0)
)

# ================================================
# Таблица: Чеки (один-к-одному с заказом)
# ================================================
receipts = Table(
    "receipts", metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id"), unique=True, nullable=False),
    Column("issued_at", DateTime, default=lambda: datetime.now(UTC)),
    Column("payment_method", String(20)),  # cash, card, online
    Column("paid_amount", Float),
    Column("is_paid", Integer, default=0)  # SQLite: 0=False, 1=True
)

# ================================================
# Создаём ВСЕ таблицы в БД (выполнится при первом импорте)
# ================================================
metadata.create_all(engine)

print("✅ Схема базы данных создана (файл: autorepair.db)")