"""Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict."""


n = 0
while n < 1 or n > 12:
    n = int(input("Введите число от 1 до 12 >> "))
seasons_list = ['зима', 'весна', 'лето', 'осень', 'зима']
print("Число, которое вы ввели соответствет времени года -", seasons_list[n // 3])
n = 0
while n < 1 or n > 12:
    n = int(input("Введите число от 1 до 12 >> "))
seasons_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for i, j in seasons_dict.items():
    if n in j:
        print("Число, которое вы ввели соответствет времени года -", i)
