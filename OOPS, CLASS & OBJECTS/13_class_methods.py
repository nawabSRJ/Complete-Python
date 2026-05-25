# Demonstrating class methods that work with class state or alternative constructors

# Class methods are methods that receive the class itself as the first argument (usually called cls). They are useful when a method needs to access or modify class-level state, or when you want an alternate way to construct objects.

# When to use class methods:
# - You need to update class variables for all instances.
# - You want a factory method or alternative constructor.
# - The method is related to the class as a whole rather than to a single instance.
#
# Difference from static methods:
# - classmethod receives cls, so it can modify class variables or return instances.
# - staticmethod receives neither cls nor self.
#
# Practical use case:
# - configure class-wide behavior like a shared raise percentage.
# - create objects from different input formats (string, dict, JSON).

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        '''Apply the current raise amount to this employee's salary.'''
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        '''Change the raise amount for the entire class.'''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        '''Create an Employee object from a string like "Name-Salary".'''
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

Employee.set_raise_amount(1.10) # modified class data
employee = Employee.from_string('Maya-50000')
employee.apply_raise()
print(employee.name, employee.salary)
