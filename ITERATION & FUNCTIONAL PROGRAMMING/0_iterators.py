# Iterators in Python implement the iterator protocol: __iter__() and __next__().
# They produce values one at a time and remember their state between calls.
# Iterators are useful for lazy processing of data, especially when working with
# large or infinite sequences.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

counter = Countdown(5)
print('Iterator object:', counter)
print('Next values:')
print(next(counter))
print(next(counter))

print('\nUsing for loop with the same iterator:')
for number in counter:
    print(number)

# When to use iterators:
# - when you need controlled, step-by-step access to values
# - when you want to avoid loading the entire sequence into memory
# - when you implement custom sequence-like classes
#
# Note:
# - An iterator is a one-way object; once exhausted, it cannot be reused.
# - The for loop automatically catches StopIteration.
