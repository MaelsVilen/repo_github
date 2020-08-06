"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
 А также класс «Оргтехника», который будет базовым для классов-наследников. 
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
 В базовом классе определить параметры, общие для приведенных типов. 
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
 Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
 любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. 
 Реализуйте механизм валидации вводимых пользователем данных. 
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


class NegativeQuantity(Exception):
    def __init__(self, message):
        self.message = message


class NegativePrice(Exception):
    def __init__(self, message):
        self.message = message


class Warehouse:
    def __init__(self):
        self.store = list()

    def add_item(self, item):
        self.store.append(item.get_info())
        return self.store

    def send_to(self, what, where):
        for i in range(len(self.store)):
            if what in self.store[i].values():
                where.items.append(self.store[i])
                self.store.pop(i)
                break


class Accounting(Warehouse):
    def __init__(self):
        super().__init__()
        self.items = list()


class Office(Warehouse):
    def __init__(self):
        super().__init__()
        self.items = list()


class OfficeEquipment:
    def __init__(self, name, quantity, price):
        self.name = name
        try:
            self.quantity = int(quantity)
            if self.quantity < 0:
                raise NegativeQuantity("Quantity cannot be negative")
            self.price = float(price)
            if self.price < 0:
                raise NegativePrice("Price cannot be negative")
        except ValueError:
            print("Incorrect data")
        except TypeError:
            print("Incorrect data")
        except NegativeQuantity as nq:
            print(nq)
            while True:
                self.quantity = int(input("input correct value - "))
                if self.quantity >= 0:
                    break
        except NegativePrice as np:
            print(np)
            while True:
                self.price = int(input("input correct value - "))
                if self.price >= 0:
                    break

    def get_info(self):
        return self.__dict__


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, price, kind='printer'):
        super().__init__(name, quantity, price)
        self.kind = kind


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, price, kind='scanner'):
        super().__init__(name, quantity, price)
        self.kind = kind


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, price, kind='Xerox'):
        super().__init__(name, quantity, price)
        self.kind = kind


obj_a = Xerox('Xerox', 1, 13000)
obj_b = Printer('HP', 3, 7500, 'LaserJet')
obj_c = Scanner('HP', 2, 5000, 'ScanJet')
obj_d = Xerox('Xerox', 1, 25000, 'WorkCentre')
wh = Warehouse()
wh.add_item(obj_a)
wh.add_item(obj_b)
wh.add_item(obj_c)
wh.add_item(obj_d)
print(wh.store)
ac = Accounting()
of = Office()
wh.send_to("LaserJet", ac)
wh.send_to("WorkCentre", of)
print(ac.items)
print(of.items)
print(wh.store)
