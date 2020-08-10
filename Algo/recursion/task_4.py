"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# Решение через рекурсию


def find_sequence_sum_rec(n, index=0, sequence_sum=0):
    if index == n:
        return sequence_sum
    else:
        sequence_sum += (1.0 / (2 ** index)) * ((-1) ** (index + 2))
        return find_sequence_sum_rec(n, index + 1, sequence_sum)


try:
    print(find_sequence_sum_rec(int(input("Введите количество элементов: "))))
except ValueError:
    print("Введите число: ")
    print(find_sequence_sum_rec(int(input("Введите количество элементов: "))))


# Решение через циклы


def find_sequence_sum(n):
    sequence_sum = 0.0
    index = 0
    while index < n:
        sequence_element = (1.0 / (2 ** index)) * ((-1) ** (index + 2))
        sequence_sum += sequence_element
        index += 1
    return sequence_sum


try:
    print(find_sequence_sum(int(input("Введите количество элементов: "))))
except ValueError:
    print("Введите число: ")
    print(find_sequence_sum(int(input("Введите количество элементов: "))))
