# map() applies a function to every item in an iterable and returns a map object.
# It is lazy in Python 3, so the transformation happens only when iterated.

numbers = [1, 2, 3, 4]
print('Original:', numbers)

# Use map to transform each item:
squared = map(lambda x: x * x, numbers)
print('Squared:', list(squared))

# Example: convert a list of strings to integers
string_numbers = ['10', '20', '30']
integers = map(int, string_numbers)
print('Converted:', list(integers))

# When to use map():
# - when you want to apply the same operation to every item
# - when you want readable, functional-style code
# - when you want to avoid writing an explicit loop for simple transformations

# Note:
# - map() is best when the mapping function is simple.
# - if the operation is complex, a normal for loop or list comprehension may be clearer.
