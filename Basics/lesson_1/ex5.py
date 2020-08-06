"""Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите 
рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников
 фирмы и определите прибыль фирмы в расчете на одного сотрудника."""


revenue = int(input("Please, enter your company's revenue - "))
costs = int(input("Please, enter your company's costs - "))
profit = revenue - costs
if profit > 0:
    print(f"your company finished the year with profit = {profit}")
    efficiency = profit / revenue
    print(f"efficiency of your company is {efficiency:.1%} %")
    num_of_employees = int(input("now, please input number of employees in your company - "))
    profit_per_employee = profit / num_of_employees
    print(f"the profit of the company per employee is {profit_per_employee}")
else:
    print("your company is unprofitable")