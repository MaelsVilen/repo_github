"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
"""
import random as rd
elements = [int(i*rd.random()*100) for i in range(1,30)]

def find_minimum_element(elements):
    minimum = elements[0]
    for i in range(1, len(elements)):
        if elements[i] < minimum:
            minimum = elements[i]
    return minimum

print(find_minimum_element(elements))

"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""
def find_minimum_element_2(elements):
    return min(elements)

print(find_minimum_element_2(elements))

"""
Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""