f_obj = open("for_ex1.txt", "a")
while True:
    content = input("write something into file >> ")
    content += '\n'
    f_obj.write(content)
    if content == '\n':
        break
f_obj.close()
