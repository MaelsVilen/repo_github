"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""


numbers_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
write_here = open('for_ex4.txt', 'w', encoding='UTF-8')
with open('text_4.txt') as read_this:
    for i in read_this:
        temp = i.split()
        temp[0] = numbers_dict[temp[0]]
        print((' ').join(temp), file=write_here)
write_here.close()
