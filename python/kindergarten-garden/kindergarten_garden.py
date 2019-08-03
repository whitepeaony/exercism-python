class Garden(object):
    def __init__(self, diagram, students=None):

        if students is None:
            students = ['Alice',  'Bob',  'Charlie',  'David', 'Eve',  'Fred',
                        'Ginny',  'Harriet',  'Ileana',  'Joseph',  'Kincaid',  'Larry']
        
        cups = []
        a, b = diagram.split('\n')
       
        for i in range(0, len(a), 2):
           cups.append(a[i:i+2] + b[i:i+2])
           

        self.seeds = {}
        for n, i in zip(sorted(students), cups):
            self.seeds[n] = i

    full_names = {'C':'Clover', 'R':'Radishes', 'G':'Grass', 'V':'Violets'}


    def plants(self, name):
        seed = self.seeds[name]
        return  [self.full_names[s] for s in seed] 

        

