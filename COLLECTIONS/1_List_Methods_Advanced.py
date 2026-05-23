# LIST METHODS ADVANCED
# Performance implications, edge cases, and real-world usage patterns.

print("=" * 60)
print("PERFORMANCE: append() vs extend() vs +=")
print("=" * 60)

# append: O(1) amortized, adds single reference
list_append = [1, 2, 3]
list_append.append([4, 5, 6])
print("After append([4, 5, 6]):", list_append)

# extend: O(k) where k is length of iterable, adds individual elements
list_extend = [1, 2, 3]
list_extend.extend([4, 5, 6])
print("After extend([4, 5, 6]):", list_extend)

# +=: creates new list if concatenating with +, but extend-like if using +=
list_plus = [1, 2, 3]
list_plus += [4, 5, 6]
print("After += [4, 5, 6]:", list_plus)

print("\nPerformance note:")
print("  extend() and += are similar for built-in types")
print("  append() is fastest for single items")

print("\n" + "=" * 60)
print("insert() PERFORMANCE - O(n) operation")
print("=" * 60)

# Inserting at beginning is slow (shifts all elements)
print("Inserting at beginning of large list requires shifting all elements")
print("Inserting at end is O(1) - use append() instead")

large_list = list(range(1000))
print(f"\nWith list of {len(large_list)} elements:")
print("  insert(0, x) is slow (O(n))")
print("  insert(len(list), x) is slow (O(n)) - use append() instead")
print("  insert(middle, x) is O(n)")

print("\n" + "=" * 60)
print("remove() vs pop() - Key differences")
print("=" * 60)

# remove: by value, first occurrence only, raises ValueError if not found
list_remove = [1, 2, 3, 2, 4]
print("List:", list_remove)
list_remove.remove(2)
print("After remove(2):", list_remove)

# pop: by index, returns value, raises IndexError if invalid
list_pop = [1, 2, 3, 2, 4]
print("\nList:", list_pop)
removed = list_pop.pop(1)
print(f"After pop(1), removed value {removed}, list:", list_pop)

# Which to use?
print("\nUse remove() when: you know the value to delete")
print("Use pop() when: you know the index OR need the removed value")

print("\n" + "=" * 60)
print("PATTERN: pop() for stack/queue operations")
print("=" * 60)

# Stack (LIFO - Last In First Out)
stack = []
for item in ['a', 'b', 'c']:
    stack.append(item)
    print(f"Push {item}, stack: {stack}")

while stack:
    item = stack.pop()
    print(f"Pop {item}, stack: {stack}")

# Queue simulation (FIFO - First In First Out)
print("\nFor actual queues, use collections.deque instead:")
print("  list.pop(0) is O(n) - slow")
print("  list.insert(0, x) is O(n) - slow")
print("  collections.deque.popleft() is O(1) - fast")

print("\n" + "=" * 60)
print("sort() vs sorted() - Key difference")
print("=" * 60)

# sort(): in-place, modifies original, returns None, slightly faster
list1 = [3, 1, 2]
list1.sort()
print(f"list.sort(): modifies original to {list1}")

# sorted(): creates new list, original unchanged, works on any iterable
list2 = [3, 1, 2]
result = sorted(list2)
print(f"sorted(list): returns new list {result}, original {list2}")

# sorted() works on any iterable
tuple_sorted = sorted((3, 1, 2))
print(f"sorted((3, 1, 2)): {tuple_sorted}")

string_sorted = sorted("python")
print(f"sorted('python'): {string_sorted}")

print("\n" + "=" * 60)
print("sort() with key function - Advanced patterns")
print("=" * 60)

# Sorting objects
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [
    Student("Alice", 3.8),
    Student("Bob", 3.5),
    Student("Charlie", 3.9),
]
print("Before sort:", students)

students.sort(key=lambda s: s.grade, reverse=True)
print("After sort by grade (descending):", students)

# Multiple sort criteria using tuples
students.sort(key=lambda s: (-s.grade, s.name))
print("After sort by grade (desc) then name:", students)

print("\n" + "=" * 60)
print("index() and count() - When to use")
print("=" * 60)

data = [10, 20, 30, 20, 40, 20]

# index() for checking if exists and getting position
if 20 in data:
    first_pos = data.index(20)
    print(f"Value 20 first appears at index {first_pos}")

# count() for frequency
frequency = data.count(20)
print(f"Value 20 appears {frequency} times")

# Finding all indices
indices = [i for i, x in enumerate(data) if x == 20]
print(f"Value 20 appears at indices {indices}")

print("\n" + "=" * 60)
print("copy() - Shallow vs Deep copy")
print("=" * 60)

import copy

# Shallow copy - only outer list is copied
original = [[1, 2], [3, 4]]
shallow = original.copy()
print("Original:", original)
print("Shallow copy:", shallow)

shallow[0][0] = 999
print("After modifying shallow[0][0] = 999:")
print("  original:", original)
print("  shallow:", shallow)

# Deep copy - entire structure is copied
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)
print("\nWith deep copy:")
deep[0][0] = 999
print("After modifying deep[0][0] = 999:")
print("  original:", original2)
print("  deep:", deep)

print("\n" + "=" * 60)
print("clear() - Use cases")
print("=" * 60)

# Clear and reuse
cache = [1, 2, 3, 4, 5]
print("Cache before clear:", cache)
cache.clear()
print("Cache after clear:", cache)

# Better than reassignment for large lists with multiple references
print("\nReassignment vs clear:")
ref1 = [1, 2, 3]
ref2 = ref1
ref1 = []
print("After ref1 = []: ref1", ref1, "ref2:", ref2)

ref3 = [1, 2, 3]
ref4 = ref3
ref3.clear()
print("After ref3.clear(): ref3:", ref3, "ref4:", ref4)

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: Building and modifying lists")
print("=" * 60)

# Building a list dynamically
result = []
for i in range(5):
    for j in range(3):
        result.append((i, j))

print("Result of nested loop:", result)

# Modifying while iterating - dangerous!
items = [1, 2, 3, 4, 5]
print("\nIteration order matters:")
# Safe: iterate over copy or use comprehension
items_copy = items.copy()
for item in items_copy:
    if item % 2 == 0:
        items.remove(item)
print("After removing even numbers:", items)

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: Accumulation and filtering")
print("=" * 60)

# Process data from API, log, filter
raw_data = [
    {'id': 1, 'value': 100, 'valid': True},
    {'id': 2, 'value': -50, 'valid': False},
    {'id': 3, 'value': 200, 'valid': True},
]

results = []
for entry in raw_data:
    if entry['valid'] and entry['value'] > 0:
        results.append(entry['value'])

print("Filtered values:", results)

# Cleaner with comprehension
results2 = [e['value'] for e in raw_data if e['valid'] and e['value'] > 0]
print("Same with comprehension:", results2)

