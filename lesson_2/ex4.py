str_in = input("Введите строку из слов, разделённых пробелами >> ")
#str_in = "На золотом крыльце сидели царь-царевич король-королевич" test
ex4_list = str_in.split()
for i, j in enumerate(ex4_list):
    print(f"Строка №{i + 1}: {j[0:10]}")
