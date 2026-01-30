# simple_debug.py
class Star:
    def __init__(self, name, temp, mass):
        self.name = name
        self.temp = temp
        self.mass = mass

    def is_red_giant(self):
        return self.temp < 4000 and self.mass > 10

    def __repr__(self):
        return f"<Star name='{self.name}', temp={self.temp}, mass={self.mass}>"

# Создаём объект
star = Star("Betelgeuse", 3500, 16.5)

print("Готово:", star)