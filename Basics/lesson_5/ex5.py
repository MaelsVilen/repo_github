"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


import random as rnd
rand_list = [round(rnd.random() * 100, 2) for el in range(20)]
with open("for_ex5.txt", "w") as num_gen:
    total = 0
    for i in rand_list:
        total += i
        f = str(i) + ' '
        num_gen.write(f)
    print(f'Сумма чисел равна: {total:.2f}')
