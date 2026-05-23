# TUPLES BASICS
# Immutable, ordered sequences with fixed size.

print("=" * 60)
print("TUPLE CREATION")
print("=" * 60)

# Different ways to create tuples
empty_tuple = ()
print("Empty tuple:", empty_tuple)

single_element = (1,)
print("Single element tuple (note comma):", single_element)

multiple_elements = (1, 2, 3)
print("Tuple with multiple elements:", multiple_elements)

mixed_types = (1, "hello", 3.14, True, None)
print("Tuple with mixed types:", mixed_types)

# Without parentheses (still a tuple)
implicit_tuple = 1, 2, 3
print("Tuple without parentheses:", implicit_tuple, type(implicit_tuple))

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("abc")
print("From list:", from_list)
print("From string:", from_string)

print("\n" + "=" * 60)
print("IMMUTABILITY")
print("=" * 60)

t = (1, 2, 3)
print("Original tuple:", t)

# Cannot modify elements
try:
    t[0] = 999
except TypeError as e:
    print(f"t[0] = 999 raises TypeError: {e}")

# Cannot add or remove
try:
    t.append(4)
except AttributeError as e:
    print(f"t.append(4) raises AttributeError: {e}")

# Cannot assign slice
try:
    t[0:2] = (9, 9)
except TypeError as e:
    print(f"t[0:2] = (9, 9) raises TypeError: {e}")

print("\n" + "=" * 60)
print("INDEXING AND SLICING")
print("=" * 60)

coordinates = (10, 20, 30, 40, 50)
print("Tuple:", coordinates)
print("Index 0:", coordinates[0])
print("Index -1:", coordinates[-1])
print("Slice [1:3]:", coordinates[1:3])
print("Slice [::2] (every second):", coordinates[::2])
print("Slice [::-1] (reversed):", coordinates[::-1])

print("\n" + "=" * 60)
print("UNPACKING")
print("=" * 60)

point = (10, 20)
x, y = point
print(f"Unpacking (10, 20) into x, y: x={x}, y={y}")

triple = (1, 2, 3)
a, b, c = triple
print(f"Unpacking (1, 2, 3) into a, b, c: a={a}, b={b}, c={c}")

# Extended unpacking
values = (1, 2, 3, 4, 5)
first, *middle, last = values
print(f"Unpacking (1, 2, 3, 4, 5) with first, *middle, last:")
print(f"  first={first}, middle={middle}, last={last}")

# Swapping with unpacking
a, b = 5, 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

print("\n" + "=" * 60)
print("MEMBERSHIP AND LENGTH")
print("=" * 60)

colors = ('red', 'green', 'blue')
print("Tuple:", colors)
print("'green' in colors:", 'green' in colors)
print("'yellow' in colors:", 'yellow' in colors)
print("len(colors):", len(colors))

print("\n" + "=" * 60)
print("ITERATION")
print("=" * 60)

print("Iterating over (10, 20, 30):")
for item in (10, 20, 30):
    print(f"  {item}")

print("\nWith enumerate:")
for index, item in enumerate(('a', 'b', 'c')):
    print(f"  Index {index}: {item}")

print("\n" + "=" * 60)
print("TUPLE OPERATIONS")
print("=" * 60)

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)

concatenated = tuple_a + tuple_b
print(f"(1, 2, 3) + (4, 5, 6) = {concatenated}")

repeated = (0,) * 3
print(f"(0,) * 3 = {repeated}")

print("\n" + "=" * 60)
print("TUPLE METHODS")
print("=" * 60)

data = (1, 2, 3, 2, 4, 2)
print("Tuple:", data)
print("count(2):", data.count(2))
print("index(2):", data.index(2))
print("index(4):", data.index(4))

try:
    data.index(10)
except ValueError as e:
    print(f"index(10) raises ValueError: {e}")

print("\n" + "=" * 60)
print("TUPLE UNPACKING IN FUNCTIONS")
print("=" * 60)

def process_pair(x, y):
    return f"x={x}, y={y}, sum={x+y}"

result = process_pair(5, 10)
print("Direct call process_pair(5, 10):", result)

point = (5, 10)
result = process_pair(*point)
print("Call with unpacking process_pair(*point):", result)

print("\n" + "=" * 60)
print("RETURNING MULTIPLE VALUES")
print("=" * 60)

def get_coordinates():
    return (10, 20, 30)

coords = get_coordinates()
print("Function returns tuple:", coords)

x, y, z = get_coordinates()
print("Unpacked result: x={}, y={}, z={}".format(x, y, z))

print("\n" + "=" * 60)
print("TUPLE VS LIST")
print("=" * 60)

# Tuple: immutable, hashable, slightly smaller memory
t = (1, 2, 3)
l = [1, 2, 3]

print("Tuple:", t, "Type:", type(t))
print("List:", l, "Type:", type(l))

print("\nKey differences:")
print("  Tuples are immutable (fixed after creation)")
print("  Tuples can be dictionary keys (lists cannot)")
print("  Tuples use slightly less memory")
print("  Lists support modification (append, remove, etc.)")

print("\n" + "=" * 60)
print("HASHABILITY - TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# Tuples can be dict keys
coordinates_dict = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (0, 1): "point",
}
print("Dictionary with tuple keys:")
for coord, label in coordinates_dict.items():
    print(f"  {coord}: {label}")

# Lists cannot be dict keys
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"\nUsing list as dict key raises TypeError: {e}")

print("\n" + "=" * 60)
print("NESTED TUPLES")
print("=" * 60)

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("First element:", nested[0])
print("First element of first element:", nested[0][0])

inner_x, inner_y = nested[1]
print(f"Unpacking nested[1]: x={inner_x}, y={inner_y}")

