def division(d1, d2):
    """Функция, реализующая деление"""
    try:
        return round(d1 / d2, 2)
    except ZeroDivisionError:
        return "на ноль делить нельзя!"


print(division(int(input("введите делимое >>")), int(input("введите делитель >>"))))
