class School(object):
    def __init__(self):
        self.students = {}
        # grade -> list of students

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = [name]
        else:
            self.students[grade].append(name)

    def roster(self):
        ranking = []
        for g in sorted(self.students.keys()):
            ranking += sorted(self.students[g])
        return ranking

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))
