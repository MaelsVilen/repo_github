class Cell:
    def __init__(self, cell_size):
        try:
            self.cell_size = int(cell_size)
        except ValueError:
            print("wrong input: should be a type of int")

    def __add__(self, other):
        return self.cell_size + other.cell_size

    def __sub__(self, other):
        if self.cell_size - other.cell_size < 0:
            return "cell size cannot be negative integer"
        elif self.cell_size - other.cell_size == 0:
            return "cell was annihilated"
        else:
            return self.cell_size - other.cell_size

    def __mul__(self, other):
        return self.cell_size * other.cell_size

    def __truediv__(self, other):
        if self.cell_size // other.cell_size == 0:
            return "cell was annihilated"
        else:
            return self.cell_size // other.cell_size

    def make_order(self, n):
        try:
            n = int(n)
        except ValueError:
            print('wrong input: should be a type of int')
        order = ''
        for i in range(self.cell_size):
            if i == 0:
                order += '*'
                continue
            elif i % n == 0:
                order += '\n' + '*'
            else:
                order += '*'
        return order

a = Cell(15)
b = Cell(32)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(3))
