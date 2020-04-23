class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        try:
            self.matrix = [[int(input('Input matrix element >> ')) for i in range(columns)] for j in range(rows)]
        except ValueError:
            print('has to be type of int')

    def __str__(self):
        out = ''
        for i in range(len(self.matrix)):
            out += '\n'
            for j in range(len(self.matrix[i])):
                out += str(self.matrix[i][j]) + ' '
        return out

    def __add__(self, other):
        result = list()
        for i in range(len(self.matrix)):
            temp = []
            result.append(temp)
            for j in range(len(self.matrix[i])):
                temp.append(self.matrix[i][j] + other.matrix[i][j])
        out = ''
        for i in range(len(result)):
            out += '\n'
            for j in range(len(result[i])):
                out += str(result[i][j]) + ' '
        return out


m1 = Matrix(2, 3)
m2 = Matrix(2, 3)
print(m1)
print(m2)
print(m1 + m2)
