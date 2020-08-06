"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую 
его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()."""


def int_func(text):
    my_list = list('qwertyuiopasdfghjklzxcvbnm')
    for i in text:
        if i in my_list:
            text = text.capitalize()
            return text
    else:
        return 'Введите слово, состоящее из прописных латинских букв'

print(int_func(input('введите слово или сочетание букв - ')))

user_input = input('введите слова, разделённые пробелом - ')
user_input = user_input.split(' ')
new_list = []
for i in user_input:
    new_list.append(int_func(i))
print(' '.join(new_list))


