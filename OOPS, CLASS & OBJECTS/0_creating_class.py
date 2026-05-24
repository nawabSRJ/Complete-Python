'''This is the docstring of the file'''
class MyClass:
    '''This is the docstring of my class'''
    pass

print(__doc__)
print(MyClass.__doc__) # docstring of the class


# * Declaring class variables and methods OR class members

class Employee:
    name = 'Srajan'
    age = 21
    gender = 'Male'

    def func():
        '''Print the class member variables data'''
        print(Employee.name)
        print(Employee.age)


# ? Creating a class object ~ Object is simply an encapsulation of an entire class that helps us to access the member variables and member methods of a class

emp = Employee() # make sure to close the class name with parenthesis to make an object
Employee.func() # ? this works ~ Accessing the class method using the class name

# emp.func()  # ! this does NOT work
# ? Now in the above one, this is internally converted to Employee.func(emp) and since we have not passed any argument to the func method, it throws an error. To fix this, we need to pass the object reference as an argument to the func method. This is done by using the 'self' keyword in the method definition.

# Now we create a new class to demonstrate the use of 'self' keyword
print('\n-----------------------------\n')
class Employee:
    name = 'Srajan'
    age = 21

    def func(self):
        '''Print the class member variables data'''
        print(self.name)    # we can access the class member variables using the 'self' keyword which refers to the current object instance of the class.
        print(self.age)

emp = Employee()
emp.func() # ? this works now because we have passed the object reference as an argument to the func method using the 'self' keyword.