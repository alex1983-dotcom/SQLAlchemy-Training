from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, Table, Column, Integer, String, Float


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей.
    Наследуем от него все таблицы
    """
    pass


# ORM
class Star(Base):
    __tablename__ = "stars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    temp: Mapped[float] = mapped_column(Float, nullable=False)
    mass: Mapped[float] = mapped_column(Float, nullable=False)

    def is_red_giant(self) -> bool:
        return self.temp < 4000.0 and self.mass > 10.0

    def __repr__(self) -> str:
        return(
            f"<Star("
            f"id={self.id}, "
            f"name=`{self.name}`, "
            f"temp={self.temp}, "
            f"mass={self.mass}"
            f")>"
        )


