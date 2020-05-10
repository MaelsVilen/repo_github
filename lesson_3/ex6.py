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


