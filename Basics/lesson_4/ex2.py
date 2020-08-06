"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента."""


input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for el in input_list if input_list[input_list.index(el)] > input_list[(input_list.index(el)) - 1] and
               input_list.index(el) != 0]
print(result_list)