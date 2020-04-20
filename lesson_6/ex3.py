class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        if type(self.name) == str and type(self.surname) == str:
            print(f'{self.name} {self.surname}')
        else:
            print('Представлены некорректные данные')

    def get_total_income(self):
        try:
            print(sum(self._income.values()))
        except TypeError:
            print('Представлены некорректные данные')


manager = Position('Иван', 'Иванов', 'работяга', 20000, 15000)
manager.get_full_name()
manager.get_total_income()
