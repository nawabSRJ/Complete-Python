# Higher-order functions are functions that accept other functions as arguments
# and/or return functions as results.
# This is a powerful concept in Python because functions are first-class objects.

# Example 1: Passing a function as an argument.

def apply_operation(x, y, operation):
    '''Higher-order function: operation is another function.'''
    return operation(x, y)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))       # 8
print(apply_operation(5, 3, multiply))  # 15

# Example 2: Returning a function from another function.

def make_power(exponent):
    '''Return a new function that raises input to the given exponent.'''
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)
print(square(4))  # 16
print(cube(2))    # 8

# Practical use cases for higher-order functions:
# - create reusable building blocks for operations
# - implement decorators and wrappers
# - customize behavior without changing the calling code
# - use built-in functions like map(), filter(), sorted(), reduce(), and any()

# Example 3: using a higher-order function with a lambda
print(apply_operation(7, 2, lambda a, b: a - b))  # 5

# Built-in higher-order functions in Python:
# - map(function, iterable)
# - filter(function, iterable)
# - sorted(iterable, key=function)
# - reduce(function, iterable) from functools

# Example 4: use a higher-order helper to apply a function twice

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x + 3, 5))  # 11
