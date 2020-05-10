items_list = []
item_position = len(items_list) + 1
n = 0
while n <= 0:
    n = int(input("Сколько позиций товара вы хотите внести в базу? >> "))
while item_position <= n:
    item_name = input("Введите название товара >> ")
    item_price = float(input("Введите цену товара >> "))
    item_amount = int(input("Введите количество >> "))
    while item_amount < 0:
        item_amount = int(input("Введите количество >> "))
    item_units = input("Введите единицы измерения >> ")
    item_dict = {"название": item_name, "цена": item_price, "количество": item_amount, "единицы": item_units}
    item_tuple = (item_position, item_dict)
    items_list.append(item_tuple)
    item_position += 1
analytics_dict = dict()
i = 0
dicts = []
while i < len(items_list):
    dicts.append(items_list[i][1])
    i += 1
for i in dicts:
    for k, j in i.items():
        analytics_dict.setdefault(k, []).append(j)
print("Аналитический отчёт", analytics_dict)


