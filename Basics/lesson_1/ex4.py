"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции."""


user_input = int(input("enter positive integer - "))
min = 0
max = 0
if user_input < 0:
    print("Incorrect integer format")
while user_input > 0:
    temp = user_input % 10
    user_input = user_input // 10
    if max >= temp:
        max = max
    elif max < temp:
        min = max
        max = temp
print(f"max digit is {max}")