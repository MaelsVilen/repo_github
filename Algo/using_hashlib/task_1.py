"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


from datetime import datetime as dt


def do_time_diff(func):
    def wrapper(*args):
        start = dt.now()
        res = func(*args)
        print(dt.now() - start)
        return res
    return wrapper


@do_time_diff
def fill_list(x):
    example_list = []
    for i in range(x):
        example_list.append(i)
    return example_list


@do_time_diff
def fill_dict(x):
    example_dict = {}
    for i in range(x):
        example_dict[i] = i
    return example_dict


ex1 = fill_list(10 ** 5)
ex2 = fill_dict(10 ** 5)

