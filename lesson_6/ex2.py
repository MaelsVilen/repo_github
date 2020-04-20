class Road:
    def __init__(self, length, width):
        """конструктор входных данных. Все данные приводятся в метрах."""
        self.length = length
        self.width = width

    def asphalt_mass_calc(self, mass_per_msq, asphalt_thickness):
        """функция для расчёта суммарной массы асфальта, необходимой для укладки дороги
            mass_per_msq: значение массы асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см в кг;
            asphalt_thickness: значение толщины полотна в см
            ответ выводится в тоннах"""
        try:
            a_mass = (self.length * self.width * mass_per_msq * asphalt_thickness) / 1000
            return round(a_mass)
        except TypeError:
            print("Введите корректные данные")


track = Road(5000, 20)
print(track.asphalt_mass_calc(25, 5))
