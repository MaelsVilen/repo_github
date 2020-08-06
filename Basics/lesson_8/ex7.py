"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и 
умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexStuff:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        if res_b >= 0:
            return f'resulted complex number is {res_a} + {res_b}i'
        elif res_b < 0:
            return f'resulted complex number is {res_a} - {abs(res_b)}i'


    def __mul__(self, other):
        res_a = self.a * other.a - self.b * other.b
        res_b = self.a * other.b + self.b * other.a
        if res_b >= 0:
            return f'resulted complex number is {res_a} + {res_b}i'
        elif res_b < 0:
            return f'resulted complex number is {res_a} - {abs(res_b)}i'


n_1 = ComplexStuff(4, -2)
n_2 = ComplexStuff(6, 4)
print(n_1 + n_2)
print(n_1 * n_2)
n_3 = complex(4, -2)
n_4 = complex(6, 4)
print(n_3 + n_4)
print(n_3 * n_4)