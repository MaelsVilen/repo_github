"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("~~~ .-'--`-._\n"
              "~~~ '-O---O--'")

    def stop(self):
        print(".-'--`-._\n"
              "'-O---O--'")

    def turn(self, direction):
        if direction == 'left':
            print(" _____")
            print("i_____i")
            print('["___"]')
            print("|J---L|")
        elif direction == 'right':
            print(" _____")
            print("|_____|")
            print('[O___O]')
            print("|J---L|")
        else:
            print(".-'--`-._(WAT???)\n"
                  "'-O---O--'")

    def show_speed(self):
        if type(self.speed) == int:
            print(f'current speed is {self.speed}')
        else:
            print("Wrong input!")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        try:
            if self.speed > 60:
                print("Warning! Speed limit exceeded!")
            elif self.speed < 60:
                print(f'current speed is {self.speed}')
        except TypeError:
            print('wrong input')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_off(self):
        print("~~~ ---.-'--`-._(YEEET)\n"
              "~~~ ---'-O---O--'")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sirens(self):
        print("~~~.-'--`-._(UiUiWiiii)\n"
              "~~~'-O---O--'")
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        try:
            if self.speed > 40:
                print("Warning! Speed limit exceeded!")
            elif self.speed < 40:
                print(f'current speed is {self.speed}')
        except TypeError:
            print('wrong input')

truck = WorkCar(56, 'yellow', 'CAT', False)
truck.show_speed()