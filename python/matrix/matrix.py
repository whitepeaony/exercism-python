class Matrix(object):
    def __init__(self, matrix_string):
        lines = matrix_string.split('\n')
        a = []
        for i in lines:
            b = [int(l) for l in i.split()]
            a.append(b)
        self.matrix = a

    def row(self, index):

        pass

    def column(self, index):
        pass


matrix = Matrix("1 2\n3 4")
print(matrix.matrix)
   