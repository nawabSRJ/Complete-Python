# SETS BASICS
# Unordered collections of unique elements.

print("=" * 60)
print("SET CREATION")
print("=" * 60)

# Different ways to create sets
empty_set = set()
print("Empty set using set():", empty_set, type(empty_set))

# NOT {}  - that's an empty dict!
print("Empty dict using {}:", {}, type({}))

literal_set = {1, 2, 3, 4, 5}
print("Set literal {1, 2, 3, 4, 5}:", literal_set)

mixed_set = {1, 'hello', 3.14, True}
print("Set with mixed types:", mixed_set)

from_list = set([1, 2, 2, 3, 3, 3])
print("set([1, 2, 2, 3, 3, 3]):", from_list)

from_string = set('hello')
print("set('hello'):", from_string)

print("\n" + "=" * 60)
print("UNIQUENESS - SETS ELIMINATE DUPLICATES")
print("=" * 60)

duplicates = [1, 1, 2, 2, 3, 3, 3]
print("List with duplicates:", duplicates)

unique = set(duplicates)
print("After set():", unique)
print("Back to list (order not guaranteed):", sorted(unique))

print("\n" + "=" * 60)
print("MEMBERSHIP TESTING - O(1) average case")
print("=" * 60)

numbers = {1, 2, 3, 4, 5}
print("Set:", numbers)
print("1 in numbers:", 1 in numbers)
print("10 in numbers:", 10 in numbers)

# Performance advantage over list
print("\nMembership testing is faster in sets than lists for large collections")

print("\n" + "=" * 60)
print("SET OPERATIONS - Mathematical set operations")
print("=" * 60)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

# Union - all elements
union = set_a | set_b
print("\nUnion (A | B):", union)
union_method = set_a.union(set_b)
print("Using .union():", union_method)

# Intersection - common elements
intersection = set_a & set_b
print("\nIntersection (A & B):", intersection)
intersection_method = set_a.intersection(set_b)
print("Using .intersection():", intersection_method)

# Difference - in A but not in B
difference = set_a - set_b
print("\nDifference (A - B):", difference)
difference_method = set_a.difference(set_b)
print("Using .difference():", difference_method)

# Symmetric difference - in A or B but not both
sym_diff = set_a ^ set_b
print("\nSymmetric difference (A ^ B):", sym_diff)
sym_diff_method = set_a.symmetric_difference(set_b)
print("Using .symmetric_difference():", sym_diff_method)

print("\n" + "=" * 60)
print("SET COMPARISONS")
print("=" * 60)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
set_3 = {1, 2, 3}

print("Set 1:", set_1)
print("Set 2:", set_2)
print("Set 3:", set_3)

print("\nset_1 == set_3:", set_1 == set_3)
print("set_1 != set_2:", set_1 != set_2)
print("set_1 < set_2 (subset):", set_1 < set_2)
print("set_1 <= set_2 (subset or equal):", set_1 <= set_2)
print("set_2 > set_1 (superset):", set_2 > set_1)
print("set_1.issubset(set_2):", set_1.issubset(set_2))
print("set_2.issuperset(set_1):", set_2.issuperset(set_1))
print("set_1.isdisjoint(set_2):", set_1.isdisjoint(set_2))

set_disjoint = {10, 20, 30}
print("\nset_1.isdisjoint({10, 20, 30}):", set_1.isdisjoint(set_disjoint))

print("\n" + "=" * 60)
print("SET MODIFICATION - MUTABLE UNLIKE FROZENSET")
print("=" * 60)

myset = {1, 2, 3}
print("Original set:", myset)

# Add single element
myset.add(4)
print("After add(4):", myset)

# Update with multiple elements
myset.update([5, 6, 7])
print("After update([5, 6, 7]):", myset)

# Remove element (raises KeyError if not found)
myset.remove(5)
print("After remove(5):", myset)

# Discard element (no error if not found)
myset.discard(999)
print("After discard(999) [non-existent]:", myset)

# Pop arbitrary element
popped = myset.pop()
print(f"After pop() removed {popped}, set is now:", myset)

# Clear all elements
copy_set = myset.copy()
copy_set.clear()
print("After clear() on copy:", copy_set)

print("\n" + "=" * 60)
print("LENGTH AND ITERATION")
print("=" * 60)

colors = {'red', 'green', 'blue'}
print("Set:", colors)
print("Length:", len(colors))

print("\nIterating:")
for color in colors:
    print(f"  {color}")

print("\n" + "=" * 60)
print("SET vs LIST vs TUPLE")
print("=" * 60)

print("List [1, 2, 2, 3]:")
print("  - Mutable (can change)")
print("  - Ordered (maintains order)")
print("  - Allows duplicates")
print("  - Slower membership testing: O(n)")

print("\nTuple (1, 2, 2, 3):")
print("  - Immutable (cannot change)")
print("  - Ordered (maintains order)")
print("  - Allows duplicates")
print("  - Slower membership testing: O(n)")

print("\nSet {1, 2, 3}:")
print("  - Mutable (can change)")
print("  - Unordered (no guarantee)")
print("  - No duplicates allowed")
print("  - Fast membership testing: O(1) average")

print("\n" + "=" * 60)
print("FROZENSET - Immutable set")
print("=" * 60)

fs = frozenset({1, 2, 3})
print("Frozenset {1, 2, 3}:", fs)

# Can be used as dict key or set element
my_dict = {fs: "value"}
print("Frozenset as dict key:", my_dict)

my_set = {frozenset({1, 2}), frozenset({3, 4})}
print("Set of frozensets:", my_set)

# Cannot modify
try:
    fs.add(4)
except AttributeError as e:
    print(f"fs.add(4) raises AttributeError: {e}")

print("\n" + "=" * 60)
print("COMMON USE CASES")
print("=" * 60)

# Removing duplicates while maintaining list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original list: {numbers}")
unique_sorted = sorted(set(numbers))
print(f"Unique and sorted: {unique_sorted}")

# Checking if lists have common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(f"\nCommon elements between {list1} and {list2}: {common}")

