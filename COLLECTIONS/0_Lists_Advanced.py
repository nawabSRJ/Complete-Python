# LISTS ADVANCED
# Performance considerations, list comprehensions, advanced patterns, and real-world scenarios.

print("=" * 60)
print("LIST COMPREHENSION VS LOOPS")
print("=" * 60)

# Traditional loop approach
squares_loop = []
for i in range(5):
    squares_loop.append(i ** 2)
print("Squares using loop:", squares_loop)

# List comprehension (cleaner, faster)
squares_comp = [i ** 2 for i in range(5)]
print("Squares using comprehension:", squares_comp)

# Comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers 0-9 using comprehension:", evens)

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("\nNested comprehension (3x3 multiplication table):")
for row in matrix:
    print(f"  {row}")

print("\n" + "=" * 60)
print("SORTING AND ORDERING")
print("=" * 60)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", numbers)

# sort() modifies in-place, returns None
sorted_list = numbers.copy()
sorted_list.sort()
print("After .sort() (in-place):", sorted_list)

# sorted() returns new list, original unchanged
result = sorted(numbers, reverse=True)
print("Using sorted(numbers, reverse=True):", result)

# Sorting with key function
words = ['apple', 'pie', 'zebra', 'a']
by_length = sorted(words, key=len)
print("\nWords sorted by length:", by_length)

students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
by_score = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by score (descending):")
for name, score in by_score:
    print(f"  {name}: {score}")

print("\n" + "=" * 60)
print("FILTERING AND MAPPING")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter using list comprehension (preferred)
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers (comprehension):", evens)

# Map using list comprehension (preferred)
doubled = [x * 2 for x in numbers]
print("Doubled (comprehension):", doubled)

# Using built-in filter() and map()
evens_builtin = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (filter):", evens_builtin)

doubled_builtin = list(map(lambda x: x * 2, numbers))
print("Doubled (map):", doubled_builtin)

print("\n" + "=" * 60)
print("PERFORMANCE: LIST VS OTHER STRUCTURES")
print("=" * 60)

# Lists are fast for indexing and appending
print("List access by index: O(1) - very fast")
print("List append: O(1) amortized - very fast")
print("List insert at beginning: O(n) - slow for large lists")
print("List search: O(n) - requires checking each element")

# Demonstration
test_list = list(range(1000000))
print("\nWith a list of 1 million elements:")
print("  Accessing element at index 999999 is instant")
print("  Inserting at index 0 requires shifting all elements")

print("\n" + "=" * 60)
print("SLICING CREATES SHALLOW COPIES")
print("=" * 60)

nested = [[1, 2], [3, 4], [5, 6]]
print("Original nested list:", nested)

sliced = nested[0:2]
print("Sliced [0:2]:", sliced)

sliced[0][0] = 999
print("After modifying sliced[0][0] = 999:")
print("  original:", nested)
print("  sliced:", sliced)
print("  → Inner lists are shared references, not deep copied")

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: ACCUMULATOR PATTERN")
print("=" * 60)

# Common pattern: process a list and accumulate results
data = [1, 2, 3, 4, 5]
result = []
for num in data:
    if num % 2 == 0:
        result.append(num * 10)

print("Data:", data)
print("Result (even numbers * 10):", result)

# Same using comprehension
result_comp = [num * 10 for num in data if num % 2 == 0]
print("Same using comprehension:", result_comp)

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: TRANSFORMATION AND CHAINING")
print("=" * 60)

# Processing a dataset
transactions = [100, -50, 200, -30, 150, -20]
print("Transactions:", transactions)

# Positive only, doubled
processed = [x * 2 for x in transactions if x > 0]
print("Positive transactions doubled:", processed)

# Alternative: filter then map
positive = [x for x in transactions if x > 0]
doubled = [x * 2 for x in positive]
print("Positive:", positive, "→ Doubled:", doubled)

print("\n" + "=" * 60)
print("MEMORY ALIASING PITFALLS")
print("=" * 60)

matrix = [[0, 0, 0]] * 3
print("Created with [[0, 0, 0]] * 3:")
print("  matrix:", matrix)

matrix[0][0] = 1
print("After matrix[0][0] = 1:")
print("  matrix:", matrix)
print("  → All rows point to the SAME list object!")

# Correct way
matrix_correct = [[0, 0, 0] for _ in range(3)]
print("\nCreated with [[0, 0, 0] for _ in range(3)]:")
print("  matrix:", matrix_correct)

matrix_correct[0][0] = 1
print("After matrix_correct[0][0] = 1:")
print("  matrix:", matrix_correct)
print("  → Each row is independent")

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: BULK OPERATIONS")
print("=" * 60)

# Process and return new list
def process_numbers(nums):
    return [x for x in nums if x > 0] + [abs(x) for x in nums if x < 0]

data = [10, -5, 20, -15, 0]
print(f"Original: {data}")
print(f"Processed (positive + absolute of negative): {process_numbers(data)}")

