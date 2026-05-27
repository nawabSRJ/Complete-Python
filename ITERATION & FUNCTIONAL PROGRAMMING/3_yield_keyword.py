# The yield keyword transforms a normal function into a generator function.
# It pauses execution and returns a value to the caller, resuming later from the same point.

# A generator that yields values one at a time:
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for number in fibonacci(6):
    print(number)

# What yield does:
# - it keeps the function's local state alive between iterations
# - it returns a generator object instead of executing immediately
# - each next() call resumes from the last yield

# Practical use cases:
# - implementing lazy data pipelines
# - reading large files line by line
# - producing values from a stateful sequence

# Example with a generator that filters data lazily:
def even_numbers(limit):
    n = 0
    while n < limit:
        if n % 2 == 0:
            yield n
        n += 1

print('\nEven numbers up to 10:')
for item in even_numbers(10):
    print(item)
