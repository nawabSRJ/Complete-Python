# LIST METHODS BASICS
# All methods and their behavior with clear examples.

print("=" * 60)
print("append() - Add single element to end")
print("=" * 60)

fruits = ['apple', 'banana']
print("Original list:", fruits)
fruits.append('cherry')
print("After append('cherry'):", fruits)

# append works with any type
fruits.append([1, 2, 3])
print("After append([1, 2, 3]):", fruits)

print("\n" + "=" * 60)
print("extend() - Add multiple elements to end")
print("=" * 60)

numbers = [1, 2, 3]
print("Original list:", numbers)
numbers.extend([4, 5, 6])
print("After extend([4, 5, 6]):", numbers)

# extend unpacks the iterable
numbers.extend('abc')
print("After extend('abc'):", numbers)

# difference with append
test = [1, 2]
test.append([3, 4])
print("\nUsing append([3, 4]) on [1, 2]:", test)

test2 = [1, 2]
test2.extend([3, 4])
print("Using extend([3, 4]) on [1, 2]:", test2)

print("\n" + "=" * 60)
print("insert() - Add element at specific index")
print("=" * 60)

letters = ['a', 'c', 'd']
print("Original list:", letters)
letters.insert(1, 'b')
print("After insert(1, 'b'):", letters)

letters.insert(0, 'z')
print("After insert(0, 'z'):", letters)

letters.insert(100, 'end')
print("After insert(100, 'end') [index out of range]:", letters)

print("\n" + "=" * 60)
print("remove() - Remove first occurrence by value")
print("=" * 60)

items = ['a', 'b', 'c', 'b', 'd']
print("Original list:", items)
items.remove('b')
print("After remove('b') [removes first 'b']:", items)

try:
    items.remove('x')
except ValueError as e:
    print(f"remove('x') raises ValueError: {e}")

print("\n" + "=" * 60)
print("pop() - Remove and return element by index")
print("=" * 60)

stack = [1, 2, 3, 4, 5]
print("Original list:", stack)

popped = stack.pop()
print(f"stack.pop() returned {popped}, list is now:", stack)

popped = stack.pop(1)
print(f"stack.pop(1) returned {popped}, list is now:", stack)

# pop() with default behavior
last_item = stack.pop(0)
print(f"stack.pop(0) returned {last_item}, list is now:", stack)

print("\n" + "=" * 60)
print("clear() - Remove all elements")
print("=" * 60)

data = [1, 2, 3, 4, 5]
print("Original list:", data)
data.clear()
print("After clear():", data)
print("Length after clear():", len(data))

print("\n" + "=" * 60)
print("index() - Find first index of value")
print("=" * 60)

colors = ['red', 'blue', 'green', 'blue']
print("List:", colors)
print("index('blue') returns:", colors.index('blue'))
print("index('red') returns:", colors.index('red'))

try:
    colors.index('yellow')
except ValueError as e:
    print(f"index('yellow') raises ValueError: {e}")

print("\n" + "=" * 60)
print("count() - Count occurrences of value")
print("=" * 60)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("List:", numbers)
print("count(1):", numbers.count(1))
print("count(3):", numbers.count(3))
print("count(4):", numbers.count(4))
print("count(5):", numbers.count(5))

print("\n" + "=" * 60)
print("sort() - Sort list in-place")
print("=" * 60)

unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", unsorted)
unsorted.sort()
print("After sort():", unsorted)

numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print("After sort(reverse=True) on [3, 1, 4, 1, 5]:", numbers)

words = ['banana', 'pie', 'a', 'apple']
words.sort(key=len)
print("Words sorted by length:", words)

print("\n" + "=" * 60)
print("reverse() - Reverse list in-place")
print("=" * 60)

sequence = [1, 2, 3, 4, 5]
print("Original list:", sequence)
sequence.reverse()
print("After reverse():", sequence)

sequence.reverse()
print("After reverse() again:", sequence)

print("\n" + "=" * 60)
print("copy() - Create shallow copy")
print("=" * 60)

original = [1, 2, 3]
duplicate = original.copy()
print("Original:", original)
print("Copy:", duplicate)

duplicate[0] = 999
print("After duplicate[0] = 999:")
print("  original:", original)
print("  duplicate:", duplicate)

# Shallow copy with nested lists
nested_original = [[1, 2], [3, 4]]
nested_copy = nested_original.copy()
nested_copy[0][0] = 999
print("\nWith nested list - after modifying inner element:")
print("  original:", nested_original)
print("  copy:", nested_copy)
print("  → Inner lists are still shared (shallow copy)")

print("\n" + "=" * 60)
print("BONUS: Difference between methods and operations")
print("=" * 60)

# In-place methods (modify original, return None)
list1 = [3, 1, 2]
result = list1.sort()
print(f"list1.sort() modifies list to {list1}, returns {result}")

# Functions (return new list, original unchanged)
list2 = [3, 1, 2]
result = sorted(list2)
print(f"sorted(list2) returns {result}, original unchanged: {list2}")

# In-place vs new
list3 = [1, 2, 3]
list3.reverse()
print(f"list3.reverse() modifies list to {list3}")

list4 = [1, 2, 3]
result = list4[::-1]
print(f"list4[::-1] returns {result}, original unchanged: {list4}")

