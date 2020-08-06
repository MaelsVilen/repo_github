"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]"""


import json


with open("text_7.txt", encoding="UTF-8") as firms:
    profit_list, result, firm_dict = [], [], dict()
    for items in firms:
        temp_list = items.split()
        revenue, costs, mean_profit = int(temp_list[2]), int(temp_list[3]), 0
        profit = revenue - costs
        firm_dict[temp_list[0]] = profit
        if profit > 0:
            profit_list.append(profit)
    mean_profit = sum(profit_list) / len(profit_list)
    result.append(firm_dict)
    result.append({'average_profit': mean_profit})
print(result)
with open("for_ex7.json", "w", encoding="UTF-8") as resulted_file:
    json.dump(result, resulted_file, indent=4, ensure_ascii=False, separators=(',', ': '))