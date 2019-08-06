class School(object):
    def __init__(self):
        pass

   
    students = []
        
    def add_student(self, name, grade):
        self.students.append((name, grade))

    def roster(self):
       return [s[0] for s in self.students]



    def grade(self, grade_number):
        pass

