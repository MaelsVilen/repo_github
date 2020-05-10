user_input = input("Input a number more than a zero - ")
if int(user_input) > 0:
    nn = user_input + user_input
    nnn = nn + user_input
    n = int(user_input)
    nn = int(nn)
    nnn = int(nnn)
    sums = n + nn + nnn
    print(f"Sum of {n} + {nn} + {nnn} is {sums}")
else:
    print("Try again next time")