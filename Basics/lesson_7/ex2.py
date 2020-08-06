""" Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name, param):
        if type(name) == str and (type(param) == int or type(param) == float):
            self.name = name
            self.param = param
        else:
            print('wrong input')

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def fabric_consumption(self):
        try:
            return f'fabric consumption for your {self.name} is {self.param / 6.5 + 0.5:.2}'
        except ValueError:
            print('wrong input')


class Suit(Clothing):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def fabric_consumption(self):
        try:
            return f'fabric consumption for your {self.name} is {2 * self.param + 0.3}'
        except AttributeError:
            print('wrong input')


c1 = Coat('trench coat', 46.4)
print(c1.fabric_consumption)
s1 = Suit('smoking', 38)
print(s1.fabric_consumption)
