class DivisionError(Exception):
    def __init__(self, message):
        self.message = message


while True:
    try:
        a = float(input('input divident value >> '))
        b = float(input('input divisor >> '))
        if b == 0:
            raise DivisionError('divisor shouldn\'t be zero')
    except ValueError:
        print('You need to input number')
        continue
    except DivisionError as de:
        print(de)
    else:
        break
print(f'result is {a / b:.2f}')
