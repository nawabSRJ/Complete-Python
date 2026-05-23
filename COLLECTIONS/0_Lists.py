# LISTS BASICS
# Lists are mutable, ordered sequences that can hold any data type.

print("=" * 60)
print("LIST CREATION AND BASIC OPERATIONS")
print("=" * 60)

# Creating lists in different ways
my_list = [1, 2, 3, 4, 5]
print("Basic list creation:", my_list)

mixed_list = [1, "hello", 3.14, True, None]
print("\nMixed types in a list:", mixed_list)

empty_list = []
list_from_range = list(range(5))
print("List from range(5):", list_from_range)

list_from_string = list("abc")
print("List from string 'abc':", list_from_string)

print("\n" + "=" * 60)
print("INDEXING AND SLICING")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]
print("\nOriginal list:", numbers)
print("Index 0 (first element):", numbers[0])
print("Index -1 (last element):", numbers[-1])
print("Slice [1:3] (inclusive start, exclusive end):", numbers[1:3])
print("Slice [::2] (every second element):", numbers[::2])
print("Slice [::-1] (reversed):", numbers[::-1])

print("\n" + "=" * 60)
print("MUTABILITY - LISTS ARE MUTABLE")
print("=" * 60)

letters = ['a', 'b', 'c', 'd']
print("Original list:", letters)
letters[0] = 'z'
print("After letters[0] = 'z':", letters)

letters[1:3] = ['x', 'y', 'w']
print("After letters[1:3] = ['x', 'y', 'w']:", letters)

print("\n" + "=" * 60)
print("MEMBERSHIP AND LENGTH")
print("=" * 60)

fruits = ['apple', 'banana', 'cherry']
print("List:", fruits)
print("'apple' in fruits:", 'apple' in fruits)
print("'grape' in fruits:", 'grape' in fruits)
print("Length of list:", len(fruits))

print("\n" + "=" * 60)
print("BASIC LIST OPERATIONS")
print("=" * 60)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("List A:", list_a)
print("List B:", list_b)

concatenated = list_a + list_b
print("Concatenation (list_a + list_b):", concatenated)

repeated = [0] * 3
print("Repetition ([0] * 3):", repeated)

print("\n" + "=" * 60)
print("UNPACKING - ASSIGNING LIST ELEMENTS TO VARIABLES")
print("=" * 60)

coords = [10, 20, 30]
x, y, z = coords
print("Unpacking [10, 20, 30] into x, y, z:")
print(f"  x={x}, y={y}, z={z}")

# Extended unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print("\nUnpacking [1, 2, 3, 4, 5] with first, *middle, last:")
print(f"  first={first}, middle={middle}, last={last}")

print("\n" + "=" * 60)
print("ITERATION")
print("=" * 60)

print("\nIterating with for loop:")
for item in [10, 20, 30]:
    print(f"  Item: {item}")

print("\nIterating with enumerate (index and value):")
for index, item in enumerate(['a', 'b', 'c']):
    print(f"  Index {index}: {item}")

print("\n" + "=" * 60)
print("IMPORTANT: REFERENCE VS COPY")
print("=" * 60)

original = [1, 2, 3]
reference = original
copy = original.copy()

print("Original list:", original)
reference[0] = 999
print("After reference[0] = 999:")
print(f"  original: {original} (modified because reference points to same object)")
print(f"  reference: {reference} (same object)")

copy[1] = 999
print("After copy[1] = 999:")
print(f"  original: {original} (unchanged because copy is separate)")
print(f"  copy: {copy}")

print("\n" + "=" * 60)
print("TYPE CHECKING")
print("=" * 60)

my_list = [1, 2, 3]
print("my_list = [1, 2, 3]")
print("type(my_list):", type(my_list))
print("isinstance(my_list, list):", isinstance(my_list, list))

my_tuple = (1, 2, 3)
print("\nmy_tuple = (1, 2, 3)")
print("type(my_tuple):", type(my_tuple))
print("isinstance(my_tuple, list):", isinstance(my_tuple, list))

