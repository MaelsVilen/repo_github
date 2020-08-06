"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке."""


with open("for_ex2.txt") as w_count:
    n = 1
    for items in w_count:
        print(f"Это {n}я строка: '{items[0:len(items) - 1:1]}'", end=', ')
        n += 1
        word = ''
        amount = len(items.split())
        if amount == 1:
            word = 'слово'
        elif amount > 1 and amount < 5:
            word = 'слова'
        elif amount >= 5:
            word = 'слов'
        print(f"в которой содержится {amount} {word}")
