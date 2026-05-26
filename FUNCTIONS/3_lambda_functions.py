# Lambda functions are Python's anonymous functions.
# They are defined using the lambda keyword and can contain only one expression.
# The result of that expression is returned automatically.

# Syntax:
# lambda arguments: expression

# Example of a simple lambda function:
add = lambda a, b: a + b
print(add(2, 3))  # 5

# Use cases for lambda functions:
# - small helper functions inside map(), filter(), sorted(), or reduce()
# - when you want a function without writing a full def block
# - when the function is simple and used only locally

# Example with map(): apply a function to every element in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print('Squared:', squared)

# Example with filter(): keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print('Evens:', evens)

# Example with sorted(): sort based on a custom key
words = ['apple', 'banana', 'cherry']
print(sorted(words, key=lambda word: len(word)))

# When not to use lambda:
# - if the function body requires statements or multiple lines
# - if the logic is complex and needs a descriptive name
# - if readability suffers because the lambda is too dense

# In those cases, prefer a normal def function.
