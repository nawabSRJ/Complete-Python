# zip() combines multiple iterables into tuples, pairing items by position.
# It stops when the shortest input iterable is exhausted.

names = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 92]

for student, score in zip(names, scores):
    print(f'{student} scored {score}')

# Example: unzip values with the * operator
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print('\nLetters:', letters)
print('Numbers:', numbers)

# When to use zip():
# - when you want to iterate over multiple sequences in parallel
# - when you need to pair related data from different iterables
# - when building dictionaries from two lists of keys and values

# Note:
# - zip() returns a lazy iterator.
# - use itertools.zip_longest() if you need to preserve the longest iterable.
