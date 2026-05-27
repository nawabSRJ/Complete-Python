# any() returns True if at least one element in the iterable is truthy.
# all() returns True only if every element in the iterable is truthy.

values = [0, None, '', False, 'hello']
print('any:', any(values))
print('all:', all(values))

# Use generator expressions for efficient evaluation:
numbers = [1, 2, 3, 4, 5]
print('Any even?', any(x % 2 == 0 for x in numbers))
print('All positive?', all(x > 0 for x in numbers))

# When to use any()/all():
# - when you want a quick truth test over a sequence
# - when you want short-circuit evaluation for performance
# - when checking multiple conditions in a readable way

# Note:
# - any() returns False for empty iterables.
# - all() returns True for empty iterables.
