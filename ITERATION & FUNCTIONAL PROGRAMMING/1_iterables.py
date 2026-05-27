# Iterables are objects that can return an iterator. They implement __iter__().
# Common iterables include list, tuple, dict, string, and set.
# An iterable can be passed to functions like for, list(), sorted(), zip(), and more.

fruits = ['apple', 'banana', 'cherry']
print('Iterable:', fruits)

for fruit in fruits:
    print('Fruit:', fruit)

# A custom iterable class:
class Weekdays:
    def __init__(self, days):
        self.days = days

    def __iter__(self):
        return iter(self.days)

week = Weekdays(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print('\nCustom iterable values:')
for day in week:
    print(day)

# When to use iterables:
# - when you want to support "for" loops and other iteration contexts
# - when your object holds a collection of values
# - when you want to convert data into a sequence with list(), tuple(), etc.
#
# Difference from iterator:
# - iterable: has __iter__() and produces an iterator
# - iterator: has __next__() and returns each value on demand
