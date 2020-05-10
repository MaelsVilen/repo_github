a = 0
while a <= 0:
    a = int(input("enter the result of the first day training - "))
b = 0
while b <= 0:
    b = int(input("enter expected result - "))
growth = 0.1
day = 1
while a <= b:
    a = a + a * growth
    day += 1
print(f"you will achieve the desired result on day {day}")