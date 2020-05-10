def my_func(x, y):
    try:
        x = float(x)
    except ValueError:
        return "основание должно быть числом"
    try:
        y = int(y)
    except ValueError:
        return "показатель должен быть числом"
    if y >= 0:
        return "показатель степени должен быть отрицательным, согласно условию"
    elif y == -1:
        return 1 / x
    else:
        return (1 / x)*my_func(x, y + 1)

print(my_func(input('введите основание степени >> '), input('введите отрицательный показатель степени >> ')))
