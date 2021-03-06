"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


# Решение через рекурсию


def num_rotate_b(n, rotation=0):
    if n == 0:
        print(f"Перевернутое число: {rotation}")
        return rotation
    else:
        rotation = rotation * 10 + n % 10
        return num_rotate_b(n // 10, rotation)


num_rotate_b(int(input("Введите число >> ")))


# Решение через циклы


def num_rotate(n):
    rotation = 0
    while n > 0:
        rotation = rotation * 10 + n % 10
        n = n // 10
    print("Перевернутое число:", rotation)
    return rotation


num_rotate(int(input("Введите число >> ")))
