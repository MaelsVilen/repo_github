"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        return "ошибка ввода данных"
    temp_list = [a, b, c]
    temp_list.remove(min(temp_list))
    return sum(temp_list)


print(my_func(input('введите первое число >> '), input('введите второе число >> '), input('введите третье число >> ')))
