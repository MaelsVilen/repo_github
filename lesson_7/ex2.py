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
