class Matrix(object):
    def __init__(self, matrix_string):
        lines = matrix_string.split('\n')
        a = []
        for i in lines:
            b = []
            for l in i.split():
                b.append(l)
            a.append(b)
         
        self.matrix = a

    def row(self, index):
        

    def column(self, index):
        pass
