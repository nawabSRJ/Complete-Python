# Generators are a simple way to create iterators using functions and the yield keyword.
# They produce values lazily, one at a time, and are memory-efficient for large sequences.

# Generator function example:
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print('Generator object:', countdown(3))
for value in countdown(3):
    print(value)

# Generator expression example:
squares = (x * x for x in range(5))
print('\nGenerator expression values:')
for value in squares:
    print(value)

# When to use generators:
# - when you want lazy evaluation of values
# - when the full sequence would be expensive or impossible to store
# - when you want a clean, stateful iterator without writing a class
#
# Advantages:
# - lower memory usage
# - simpler code than custom iterator classes
# - ability to represent infinite or very large sequences
