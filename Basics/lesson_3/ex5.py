"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
 выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
 сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


s = 0
while True:
    user_input = input('Введите набор чисел через пробел, для выхода введите "$" >> ')
    str_1 = user_input.split(' ')
    if '$' in str_1:
        str_1.remove('$')
        try:
            str_1 = [int(i) for i in str_1]
        except ValueError:
            print('Вы ввели некорректный символ')
        s += sum(str_1)
        print('сумма введённых чисел - ', s)
        break
    for i in str_1:
        try:
            s = s + int(i)
        except ValueError:
            print('Вы ввели некорректный символ')
    print('сумма введённых чисел - ', s)
