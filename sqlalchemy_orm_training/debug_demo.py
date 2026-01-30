from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Base, Star

engine = create_engine("sqlite:///:memory:", echo=False)


def setup():
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([
            Star(name="Betelgeuse", temp=3500, mass=61.5),
            Star(name="Proxima Cen", temp=3050, mass=0.12)
        ])
        s.commit()


def demo_orm():
    with Session(engine) as session:
        stars = session.scalars(select(Star).where(Star.temp < 4000)).all()
        for star in stars:
            print("=== ORM ===")
            print("Тип:", type(star))
            print("Объект:", star)
            print("Метод is_red_giant():", star.is_red_giant())
            print()



if __name__ == "__main__":
    setup()
    demo_orm()




