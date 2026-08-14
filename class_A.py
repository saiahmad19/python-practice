class student_class_A:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def avg(self):
        return sum(self.grades) / len(self.grades)

    def grade_status(self):
        average = self.avg()
        if average < 50:
          return "failed"
        elif average > 90:
          return "wow"
        else: 
          return "pass"

s1 = student_class_A("sai")
s1.grades.append(80)
s1.grades.append(100)
print(s1.grades)
s1.add_grades(100)
print(s1.grade_status())     
print(s1.avg())

        