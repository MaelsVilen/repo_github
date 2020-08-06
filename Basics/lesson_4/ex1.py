"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""


from sys import argv

script_name, working_h, rate_per_h, bonus = argv

def salary_calc(working_h, rate_per_h, bonus):
    """function implements the calculation of salary"""
    try:
        return int(working_h) * int(rate_per_h) + int(bonus)
    except ValueError:
        return 'incorrect input'
print(salary_calc(working_h, rate_per_h, bonus))