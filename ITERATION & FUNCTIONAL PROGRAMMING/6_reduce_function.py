# reduce() applies a function cumulatively to items in an iterable and reduces it
# to a single value. In Python 3, reduce() is available in functools.

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print('Product:', product)

# Example: build a concatenated string from a list
words = ['Python', 'is', 'fun']
sentence = reduce(lambda a, b: a + ' ' + b, words)
print('Sentence:', sentence)

# When to use reduce():
# - when you want to accumulate a result from a sequence
# - when no built-in alternative exists for the reduction
# - when the reduction logic is custom and associative

# Use with caution:
# - reduce() can be harder to read than explicit loops.
# - for sums, products, or joins, prefer built-in functions like sum() or str.join().
