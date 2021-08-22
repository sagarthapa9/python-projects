# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#          return self.name
#     def set_name(self, name):
#         self.name = name
# d=Dog('Sandy')
# d.set_name('Jack')
# print(d.get_name())

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grades(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students =  max_students
        self.students = []
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_student_average(self):
        value = 0
        for student in self.students:
            value+=student.get_grades()
        return value/len(self.students)

s1 = Student('John', 20, 70)
s2 = Student('Chris', 30, 90)
s3 = Student('Mike', 40, 90)

c1 =  Course('Programming', 2)
c1.add_students(s1)
c1.add_students(s2)
c1.add_students(s3)

print(c1.students[0].name)
print(c1.get_student_average())