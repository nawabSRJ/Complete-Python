# Demonstrating class methods that work with class state or alternative constructors

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

Employee.set_raise_amount(1.10)
employee = Employee.from_string('Maya-50000')
employee.apply_raise()
print(employee.name, employee.salary)
