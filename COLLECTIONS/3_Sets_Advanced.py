# SETS ADVANCED
# Performance implications, practical patterns, and real-world use cases.

print("=" * 60)
print("PERFORMANCE - SET OPERATIONS O(n) behavior")
print("=" * 60)

import time

# Creating sets is fast
small_set = {1, 2, 3, 4, 5}
print("Creating set: O(n) where n = number of elements")

# Membership testing: O(1) average
print("\nMembership testing (element in set): O(1) average")
print("  3 in {1, 2, 3}: O(1) - uses hash table")

# Set operations: O(n + m) for two sets of size n and m
set_a = set(range(1000))
set_b = set(range(500, 1500))

print("\nSet operations:")
print("  Union: O(n + m)")
print("  Intersection: O(min(n, m))")
print("  Difference: O(n)")
print("  Symmetric difference: O(n + m)")

print("\n" + "=" * 60)
print("IN-PLACE VS RETURNING NEW SET")
print("=" * 60)

set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}

# In-place operations modify the original
copy_x = set_x.copy()
copy_x |= set_y
print(f"Using |= (in-place): {copy_x} (set_x modified)")

# Operator returns new set
copy_x2 = set_x.copy()
result = copy_x2 | set_y
print(f"Using | (new set): {result}, original {copy_x2} (unchanged)")

# Update methods modify in-place
set_1 = {1, 2, 3}
set_1.update({4, 5})
print(f"\nAfter set_1.update({{4, 5}}): {set_1}")

set_2 = {1, 2, 3}
set_2.intersection_update({1, 2, 4})
print(f"After set_2.intersection_update({{1, 2, 4}}): {set_2}")

print("\n" + "=" * 60)
print("FILTERING WITH SETS")
print("=" * 60)

# Using sets for fast filtering
whitelist = {'python', 'java', 'cpp', 'rust'}
languages = ['python', 'javascript', 'java', 'ruby', 'cpp']

print(f"Whitelist: {whitelist}")
print(f"Languages: {languages}")

# Filter using set membership (fast)
allowed = [lang for lang in languages if lang in whitelist]
print(f"Allowed languages: {allowed}")

# Remove blacklist items
blacklist = {'javascript', 'ruby'}
filtered = [lang for lang in languages if lang not in blacklist]
print(f"After removing blacklist: {filtered}")

print("\n" + "=" * 60)
print("REAL-WORLD: Removing duplicates from data")
print("=" * 60)

# Email addresses with duplicates
emails = [
    'alice@example.com',
    'bob@example.com',
    'alice@example.com',
    'charlie@example.com',
    'bob@example.com'
]
print(f"Email list with duplicates: {emails}")

# Remove duplicates while preserving order
seen = set()
unique_emails = []
for email in emails:
    if email not in seen:
        unique_emails.append(email)
        seen.add(email)

print(f"Unique emails (order preserved): {unique_emails}")

# If order doesn't matter
unique_unordered = set(emails)
print(f"Unique emails (no order guarantee): {unique_unordered}")

print("\n" + "=" * 60)
print("REAL-WORLD: Finding common and unique elements")
print("=" * 60)

group_a = {'Alice', 'Bob', 'Charlie', 'David'}
group_b = {'Charlie', 'David', 'Eve', 'Frank'}

print(f"Group A: {group_a}")
print(f"Group B: {group_b}")

common = group_a & group_b
print(f"\nCommon members: {common}")

only_in_a = group_a - group_b
print(f"Only in Group A: {only_in_a}")

only_in_b = group_b - group_a
print(f"Only in Group B: {only_in_b}")

either_but_not_both = group_a ^ group_b
print(f"Either but not both: {either_but_not_both}")

everyone = group_a | group_b
print(f"Everyone: {everyone}")

print("\n" + "=" * 60)
print("REAL-WORLD: Checking for subset/superset relationships")
print("=" * 60)

required_permissions = {'read', 'write', 'delete'}
user_permissions = {'read', 'write', 'delete', 'admin'}

print(f"Required: {required_permissions}")
print(f"User has: {user_permissions}")

if required_permissions <= user_permissions:
    print("User has all required permissions")
else:
    missing = required_permissions - user_permissions
    print(f"User is missing: {missing}")

print("\n" + "=" * 60)
print("REAL-WORLD: Validating data uniqueness")
print("=" * 60)

# Check if IDs are unique in a dataset
data = [
    {'id': 101, 'name': 'Item A'},
    {'id': 102, 'name': 'Item B'},
    {'id': 103, 'name': 'Item C'},
    {'id': 102, 'name': 'Item B duplicate'},
]

ids = [item['id'] for item in data]
unique_ids = set(ids)

print(f"Total items: {len(data)}")
print(f"Unique IDs: {len(unique_ids)}")

if len(ids) == len(unique_ids):
    print("All IDs are unique")
else:
    # Find duplicates
    seen = set()
    duplicates = set()
    for id_ in ids:
        if id_ in seen:
            duplicates.add(id_)
        seen.add(id_)
    print(f"Duplicate IDs: {duplicates}")

print("\n" + "=" * 60)
print("REAL-WORLD: Word comparison and analysis")
print("=" * 60)

text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the lazy dog sleeps by the fox"

words1 = set(text1.split())
words2 = set(text2.split())

print(f"Text 1 words: {words1}")
print(f"Text 2 words: {words2}")

common_words = words1 & words2
print(f"Common words: {common_words}")

unique_to_text1 = words1 - words2
print(f"Only in text1: {unique_to_text1}")

all_unique = words1 ^ words2
print(f"Words appearing in only one text: {all_unique}")

print("\n" + "=" * 60)
print("USING SETS IN GRAPH AND NETWORK ALGORITHMS")
print("=" * 60)

# Modeling connections
friend_network = {
    'Alice': {'Bob', 'Charlie', 'David'},
    'Bob': {'Alice', 'Charlie'},
    'Charlie': {'Alice', 'Bob', 'David'},
    'David': {'Alice', 'Charlie'},
}

print("Friend network:")
for person, friends in friend_network.items():
    print(f"  {person}: {friends}")

# Find mutual friends
alice_friends = friend_network['Alice']
bob_friends = friend_network['Bob']
mutual = alice_friends & bob_friends

print(f"\nMutual friends of Alice and Bob: {mutual}")

# Find second-degree connections
second_degree = set()
for friend in alice_friends:
    second_degree.update(friend_network[friend])
second_degree -= alice_friends | {'Alice'}

print(f"People Alice can reach in 2 hops: {second_degree}")

print("\n" + "=" * 60)
print("COMMON MISTAKES AND GOTCHAS")
print("=" * 60)

# Mistake 1: {} is empty dict, not set
empty_dict = {}
print(f"{{}} is a {type(empty_dict).__name__}, not a set")

empty_set_correct = set()
print(f"set() is an empty {type(empty_set_correct).__name__}")

# Mistake 2: Sets are unordered
s = {3, 1, 2}
print(f"\nSet {{3, 1, 2}} iteration order: {list(s)}")
print("(Order is not guaranteed and may vary)")

# Mistake 3: Set elements must be hashable
try:
    bad_set = {1, 2, [3, 4]}
except TypeError as e:
    print(f"\nLists cannot be in sets: {e}")

# Use tuple instead
good_set = {1, 2, (3, 4)}
print(f"Tuples can be in sets: {good_set}")

