# * Now are are going to learn how to initialize class members in Python. We can initialize class members in two ways - using class variables and using instance variables.

# from overrides import final ~ STUDY ABOUT THIS LATER


class Employee:
    # * Class variables are shared among all the instances of the class. They are defined within the class but outside any method. They can be accessed using the class name or using the object reference.
    name = 'Srajan'
    age = 21

    # * Instance variables are unique to each instance of the class. They are defined within a method and are prefixed with 'self'. They can only be accessed using the object reference.

    def __init__(self, name, age):
        '''This is the constructor method which is called when an object is created. It initializes the instance variables.'''
        self.name = name
        self.age = age

emp1 = Employee('Aditya', 21)
emp2 = Employee('John', 30)

print(emp1.name) # ? this will print 'Aditya' because emp1 is an instance of the Employee class and it has its own instance variable 'name' which is initialized to 'Aditya'

print(emp2.name) # ? this will print 'John' because emp2 is another instance of the Employee class and it has its own instance variable 'name' which is initialized to 'John'

print(Employee.name) # ? this will print 'Srajan' because 'name' is a class variable and it is shared among all the instances of the class. It can be accessed using the class name.

# todo : Let me show you a more suitable explanation of this

class MyMaths:
    PI = 3.14 # class variable
    def __init__(self, radius):
        self.radius = radius # instance variable

    def area(self):
        return MyMaths.pi * self.radius * self.radius # accessing class variable using class name

    def circumference(self):
        return 2 * MyMaths.pi * self.radius # accessing class variable using class name

circle1 = MyMaths(5)    # parameter is radius of the circle
print(circle1.area()) # ? this will print the area of the circle with radius 5
print(circle1.circumference()) # ? this will print the circumference of the circle with radius 5

# But what if there is something that should remain constant for all the instances of the class. 
# ! But can we modify the class variable?
MyMaths.pi = 3.15 # ? this will modify the class variable 'pi' for all the instances of the class
print(MyMaths.pi) # ? this will print 3.15 because we have modified the class variable 'pi' for all the instances of the class

# * So there is actually NO standard way to make a class variable constant in Python. We can use the convention of putting the class variable name in UPPERCASE to indicate that it should not be modified.


# todo : More on class vs instance variables in next file


