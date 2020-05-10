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