class Matrix(object):
    def __init__(self, matrix_string):
        lines = matrix_string.split('\n')
        a = []
        for i in lines:
            b = [int(l) for l in i.split()]
            a.append(b)
        self.matrix = a:

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [ r[index-1] for r in self.matrix]