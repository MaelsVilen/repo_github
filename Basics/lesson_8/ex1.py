"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать 
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:
    dd_mm_yy = '00-00-0000'

    def __init__(self, dd_mm_yy):
        Date.dd_mm_yy = dd_mm_yy

    @staticmethod
    def numeric_validator():
        new_date = Date.class_extractor(Date.dd_mm_yy)
        if new_date[0] not in range(0, 32):
            return 'incorrect day input'
        elif new_date[1] not in range(0, 13):
            return 'incorrect month input'
        elif new_date[2] <= 0:
            return 'incorrect year'
        else:
            return 'data can be extracted'

    @classmethod
    def class_extractor(cls, dd_mm_yy=dd_mm_yy):
        new_date = Date.dd_mm_yy.split('-')
        for i in range(len(new_date)):
            if new_date[i].isnumeric():
                new_date[i] = int(new_date[i])
            else:
                raise ValueError
        return new_date


data1 = Date('32-12-1212')
data2 = data1.class_extractor()
print(data1.dd_mm_yy)
print(data2)
print(data1.numeric_validator())
