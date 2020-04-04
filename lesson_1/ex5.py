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