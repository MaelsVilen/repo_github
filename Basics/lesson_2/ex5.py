"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них."""


my_rate = [7, 5, 3, 3, 2]
print("Текущий рейтинг: ", my_rate)
while True:
    exit_condition = input("Для выхода нажмите 0, для продолжения другую клавишу >> ")
    if exit_condition == '0':
        break
    user_in = int(input("Введите новый элемент рейтинга >> "))
    while user_in < 0:
        user_in = int(input("Введите положительное число >> "))
    my_rate.append(user_in)
    count = my_rate.index(user_in)
    while count > 0:
        if my_rate[count] > my_rate[count - 1]:
            my_rate[count], my_rate[count - 1] = my_rate[count - 1], my_rate[count]
        else:
            break
        count -= 1
    print("Текущий рейтинг: ", my_rate)
