from functools import reduce
resulted_list = [i for i in range(100, 1001, 2)]
print(resulted_list)
multi = lambda a, b: a * b
print(reduce(multi, resulted_list))

