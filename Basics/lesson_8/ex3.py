"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список выводится на экран."""


class NotANumberInput(Exception):
    def __init__(self, message):
        self.message = message


test_list = list()


while True:
    try:
        user_input = input('input a number >> ')
        if user_input.lower() == 'stop':
            break
        elif user_input.isdigit():
            test_list.append(int(user_input))
        else:
            raise NotANumberInput('input is not a number')
    except NotANumberInput as nani:
        print(nani)
print(test_list)