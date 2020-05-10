numbers_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
write_here = open('for_ex4.txt', 'w', encoding='UTF-8')
with open('text_4.txt') as read_this:
    for i in read_this:
        temp = i.split()
        temp[0] = numbers_dict[temp[0]]
        print((' ').join(temp), file=write_here)
write_here.close()
