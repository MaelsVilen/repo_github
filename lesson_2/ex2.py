ex2_list = []
n = int(input("Введите количество элементов в списке >> "))
while n <= 0:
    n = int(input("Введите целое положительное число >> "))
for i in range(n):
    ex2_list.append(input("Введите элементы списка >> "))
print("Введённый вами список: ", ex2_list)
# ex2_list = [1.86, 42, 4 - 7j, "good_day_mr.Freeman", (1, 6, 45), None, {3, 7, 9, 21}, b"x01", 666] - for test
for i in range(0, (len(ex2_list) // 2) * 2, 2):
    ex2_list[i], ex2_list[i + 1] = ex2_list[i + 1], ex2_list[i]
print("Список с рокировкой значений: ", ex2_list)
