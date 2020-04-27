class NotANumberInput(Exception):
    def __init__(self, message):
        self.message = message

test_list = list()

while True:
    try:
        user_input = input('input a number >> ')
        if user_input.lower() == 'stop':
            break
        elif user_input.isdigit():
            test_list.append(int(user_input))
        else:
            raise NotANumberInput('input is not a number')
    except NotANumberInput as nani:
        print(nani)
print(test_list)