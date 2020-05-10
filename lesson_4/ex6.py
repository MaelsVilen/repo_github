from itertools import count, cycle
def new_count(start, stop):
    """start: starting point integer
        stop: value integer for stop counting"""
    for i in count(start):
        if i > stop:
            break
        else:
            yield i

x = new_count(10, 20)
new_list = [el for el in x]
print(new_list)

def rotating(start, quantity):
    """start: index of element from new_list, from where you want to start
        quantity: amount of elements in a new_list2"""
    for j in cycle(new_list):
        if quantity == 0:
            break
        elif start == new_list.index(j):
            start += 1
            if start == len(new_list):
                start = 0
            quantity -= 1
            yield j

y = rotating(2, 15)
new_list2 = [el for el in y]
print(new_list2)