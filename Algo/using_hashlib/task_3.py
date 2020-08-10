"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib as hl


def substring_calculator():
    user_input = input("Введите строку: ")
    substrings = set()
    for i in range(len(user_input)):
        for j in range(i, len(user_input)):
            individual_substring = user_input[i:j + 1]
            substrings.add(hl.md5(individual_substring.encode()).hexdigest())
    print(f"Число различающихся подстрок - {len(substrings)}")


substring_calculator()