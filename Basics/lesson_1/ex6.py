"""Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""


a = 0
while a <= 0:
    a = int(input("enter the result of the first day training - "))
b = 0
while b <= 0:
    b = int(input("enter expected result - "))
growth = 0.1
day = 1
while a <= b:
    a = a + a * growth
    day += 1
print(f"you will achieve the desired result on day {day}")