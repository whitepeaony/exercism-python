class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        for i in matrix_string.split('\n'):
            b = [int(l) for l in i.split()]
            self.matrix.append(b)
       

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [ r[index - 1] for r in self.matrix]