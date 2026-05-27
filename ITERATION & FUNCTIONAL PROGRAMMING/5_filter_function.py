# filter() selects items from an iterable based on a predicate function.
# It returns a lazy filter object in Python 3.

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print('Even numbers:', list(evens))

# Example: keep only non-empty strings
values = ['apple', '', 'banana', '', 'cherry']
non_empty = filter(bool, values)
print('Non-empty values:', list(non_empty))

# When to use filter():
# - when you need to remove unwanted items from a sequence
# - when the selection condition is simple and can be expressed as a function
# - when you want a functional-style pipeline with map/filter

# Note:
# - filter() returns only the items that satisfy the predicate.
# - for more complex filtering logic, a list comprehension can be clearer.
