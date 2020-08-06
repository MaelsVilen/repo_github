"""Поработайте с переменными, создайте несколько, 
выведите на экран, запросите у пользователя несколько чисел и
 строк и сохраните в переменные, выведите на экран."""

 
first_name = "Nik"
last_name = "Smith"
ID = 101
department = "engineering"
print(f"Good morning, {first_name} {last_name}, working ID {ID} from {department} department! "
      f"It's nice day for work!")
first_name = input("please, enter your name - ")
last_name = input("enter your last name, please - ")
ID = int(input("enter your ID number (number between 100 and 200) - "))
while ID < 100 or ID > 200:
      ID = int(input("you supposed to enter number that more than 100 and less than 200. Try again - "))
department = input("enter your department - ")
print(f"Good morning, {first_name} {last_name}, working ID {ID} from {department} department! "
      f"It's nice day for a hard work!")
