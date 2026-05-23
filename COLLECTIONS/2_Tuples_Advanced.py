# TUPLES ADVANCED
# Named tuples, performance, caching, and advanced patterns.

print("=" * 60)
print("NAMED TUPLES")
print("=" * 60)

from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Named tuple Point(10, 20):", p)
print("Access by attribute p.x:", p.x)
print("Access by index p[0]:", p[0])
print("Type:", type(p))

# Alternative syntax
Person = namedtuple('Person', 'name age city')
person = Person('Alice', 30, 'NYC')
print(f"\nNamed tuple Person: name={person.name}, age={person.age}, city={person.city}")

# Named tuples are immutable like regular tuples
try:
    person.age = 31
except AttributeError as e:
    print(f"person.age = 31 raises AttributeError: {e}")

# Methods on named tuples
print(f"\nperson._asdict(): {person._asdict()}")
print(f"person._replace(age=31): {person._replace(age=31)}")
print(f"Person._fields: {Person._fields}")

print("\n" + "=" * 60)
print("USE CASE: Named tuples for cleaner code")
print("=" * 60)

# Without named tuple (confusing)
def get_user_tuple():
    return ('Alice', 30, 'alice@example.com')

user = get_user_tuple()
print("Without named tuple:", user)
print("Access: user[0] (not clear what this is)")

# With named tuple (clear)
User = namedtuple('User', ['name', 'age', 'email'])

def get_user_named():
    return User('Alice', 30, 'alice@example.com')

user = get_user_named()
print(f"\nWith named tuple: {user}")
print(f"Access: user.name = {user.name} (clear intent)")

print("\n" + "=" * 60)
print("IMMUTABILITY BENEFITS - Hashability")
print("=" * 60)

# Tuples can be in sets
coords_set = {(0, 0), (1, 1), (2, 2), (1, 1)}
print("Set of tuple coordinates:", coords_set)
print("(1, 1) in coords_set:", (1, 1) in coords_set)

# Tuples can be dict keys (great for spatial data)
grid = {}
for x in range(3):
    for y in range(3):
        grid[(x, y)] = x * y

print("\nGrid dict with tuple keys:")
for coord, value in list(grid.items())[:3]:
    print(f"  {coord}: {value}")

print("\n" + "=" * 60)
print("UNPACKING ADVANCED PATTERNS")
print("=" * 60)

# Swapping without temp variable
a, b = 10, 20
print(f"Swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Multiple assignment
x = y = z = 0
print(f"Multiple assignment x = y = z = 0: x={x}, y={y}, z={z}")

# Extended unpacking with *
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print(f"\nExtended unpacking {nums}:")
print(f"  first={first}, middle={middle}, last={last}")

# Discarding values with _
point = (10, 20, 30)
x, _, z = point
print(f"Unpacking (10, 20, 30) ignoring middle: x={x}, z={z}")

# Unpacking function returns
def get_stats():
    return 10, 20, 30

min_val, max_val, avg = get_stats()
print(f"\nFunction returns (10, 20, 30) unpacked: min={min_val}, max={max_val}, avg={avg}")

print("\n" + "=" * 60)
print("PERFORMANCE AND MEMORY")
print("=" * 60)

import sys

small_list = [1, 2, 3]
small_tuple = (1, 2, 3)

print("Memory comparison (small collections):")
print(f"  List size: {sys.getsizeof(small_list)} bytes")
print(f"  Tuple size: {sys.getsizeof(small_tuple)} bytes")

large_list = list(range(1000))
large_tuple = tuple(range(1000))

print("\nMemory comparison (1000 elements):")
print(f"  List size: {sys.getsizeof(large_list)} bytes")
print(f"  Tuple size: {sys.getsizeof(large_tuple)} bytes")

print("\nPerformance note:")
print("  Tuples are slightly more memory efficient")
print("  Tuple creation is slightly faster")
print("  List modifications (append, insert) are slower for immutable tuples anyway")

print("\n" + "=" * 60)
print("ITERATING AND ZIPPING")
print("=" * 60)

names = ('Alice', 'Bob', 'Charlie')
ages = (30, 25, 35)

print("Names:", names)
print("Ages:", ages)

print("\nZipped pairs:")
for name, age in zip(names, ages):
    print(f"  {name}: {age} years old")

# zip returns an iterator of tuples
zipped = list(zip(names, ages))
print(f"\nlist(zip(names, ages)): {zipped}")

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: Function parameters and returns")
print("=" * 60)

# Returning multiple values
def divide_and_remainder(dividend, divisor):
    return dividend // divisor, dividend % divisor

quotient, remainder = divide_and_remainder(17, 5)
print(f"17 ÷ 5: quotient={quotient}, remainder={remainder}")

# Accepting variable arguments as tuple
def sum_all(*args):
    print(f"Received args tuple: {args}")
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(f"sum_all(1, 2, 3, 4, 5) = {result}")

print("\n" + "=" * 60)
print("REAL-WORLD PATTERN: Caching and memoization")
print("=" * 60)

# Cache key: use tuple to represent function arguments
cache = {}

def fibonacci(n):
    if n in cache:
        print(f"  Cache hit for {n}")
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    
    cache[n] = result
    return result

print("Computing fibonacci(5) with caching:")
result = fibonacci(5)
print(f"Result: {result}")
print(f"Cache contents: {cache}")

print("\n" + "=" * 60)
print("COMMON MISTAKES WITH TUPLES")
print("=" * 60)

# Mistake 1: Mutable element in tuple
inner_list = [1, 2, 3]
t = (inner_list, 'data')
print("Tuple with mutable element:", t)
print("Can modify inner list even though tuple is immutable:")
inner_list[0] = 999
print("After modifying inner_list[0] = 999:", t)
print("→ Tuple is immutable, but elements CAN be mutable")

# Mistake 2: Single element tuple needs comma
print("\nSingle element issues:")
print(f"(5) is type {type((5))} - NOT a tuple (it's just 5 in parentheses)")
print(f"(5,) is type {type((5,))} - This IS a tuple")

# Mistake 3: Comparing tuples
print(f"\n(1, 2) < (1, 3): {(1, 2) < (1, 3)} (lexicographic comparison)")
print(f"(1, 2) < (2, 1): {(1, 2) < (2, 1)}")
print(f"(1, 2, 3) < (1, 2): {(1, 2, 3) < (1, 2)}")

