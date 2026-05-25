# Demonstrating class methods and instance methods in Python

class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        '''Instance method: modifies object state.'''
        self.value += amount
        return self.value

    def multiply(self, amount):
        '''Instance method: returns a computed result.'''
        return self.value * amount

    def display(self):
        print(f'Current value: {self.value}')

calc = Calculator(10)
print(calc.add(5))      # 15
print(calc.multiply(3)) # 45
calc.display()
