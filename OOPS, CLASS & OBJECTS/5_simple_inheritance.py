# Demonstrating inheritance with a base class and derived class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}.')


# ? inherit syntax : SubClass(BaseClass):
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print(f'My student ID is {self.student_id}.')

s = Student('Aditi', 21, 'S101')
s.greet()
s.show_id()
