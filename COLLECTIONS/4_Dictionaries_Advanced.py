# DICTIONARIES ADVANCED
# Special methods, defaultdict, patterns, and real-world scenarios.

print("=" * 60)
print("setdefault() - Get with default insertion")
print("=" * 60)

# setdefault: return value if exists, otherwise insert default
user_cache = {}

user_id = user_cache.setdefault('count', 0)
print(f"setdefault('count', 0) returned {user_id}, cache: {user_cache}")

user_id = user_cache.setdefault('count', 100)
print(f"setdefault('count', 100) returned {user_id} (already exists), cache: {user_cache}")

# Real use case: counting occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = {}
for word in words:
    word_count[word] = word_count.setdefault(word, 0) + 1

print(f"\nWord count: {word_count}")

print("\n" + "=" * 60)
print("fromkeys() - Create dict with default values")
print("=" * 60)

keys = ['x', 'y', 'z']
filled = dict.fromkeys(keys, 0)
print(f"dict.fromkeys(['x', 'y', 'z'], 0): {filled}")

# Without default value (None)
empty_vals = dict.fromkeys(['a', 'b', 'c'])
print(f"dict.fromkeys(['a', 'b', 'c']): {empty_vals}")

print("\n" + "=" * 60)
print("defaultdict - Automatic default values")
print("=" * 60)

from collections import defaultdict

# defaultdict with list
groups = defaultdict(list)
groups['A'].append(1)
groups['A'].append(2)
groups['B'].append(3)

print("defaultdict(list):")
print(f"  groups: {dict(groups)}")

# defaultdict with int
counter = defaultdict(int)
for letter in 'mississippi':
    counter[letter] += 1

print("\ndefaultdict(int) counting letters in 'mississippi':")
print(f"  {dict(counter)}")

# defaultdict with lambda
default_list = defaultdict(lambda: [])
default_list['key1'].append('value1')
print(f"\ndefaultdict(lambda: []): {dict(default_list)}")

print("\n" + "=" * 60)
print("Counter - Frequency counting")
print("=" * 60)

from collections import Counter

items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
item_counts = Counter(items)

print(f"Counter(items): {item_counts}")
print(f"most_common(2): {item_counts.most_common(2)}")
print(f"item_counts['apple']: {item_counts['apple']}")

# Counter arithmetic
count1 = Counter(['a', 'b', 'a'])
count2 = Counter(['a', 'c', 'c'])

print(f"\ncount1: {count1}")
print(f"count2: {count2}")
print(f"count1 + count2: {count1 + count2}")
print(f"count1 - count2: {count1 - count2}")

print("\n" + "=" * 60)
print("REAL-WORLD: Building aggregate data structures")
print("=" * 60)

# Grouping data by category
transactions = [
    {'date': '2024-01-01', 'amount': 100, 'category': 'food'},
    {'date': '2024-01-01', 'amount': 50, 'category': 'fuel'},
    {'date': '2024-01-02', 'amount': 75, 'category': 'food'},
    {'date': '2024-01-02', 'amount': 200, 'category': 'entertainment'},
]

by_category = defaultdict(list)
for trans in transactions:
    by_category[trans['category']].append(trans['amount'])

print("Transactions grouped by category:")
for category, amounts in by_category.items():
    print(f"  {category}: {amounts} (total: {sum(amounts)})")

print("\n" + "=" * 60)
print("REAL-WORLD: Caching with get() default")
print("=" * 60)

# Simple cache pattern
cache = {}

def get_user(user_id):
    # Check cache
    if user_id in cache:
        print(f"  Cache hit for user {user_id}")
        return cache[user_id]
    
    # Simulate expensive operation
    print(f"  Fetching user {user_id} from database")
    user = {'id': user_id, 'name': f'User{user_id}'}
    cache[user_id] = user
    return user

print("Caching pattern:")
get_user(1)
get_user(1)
get_user(2)
get_user(2)

print("\n" + "=" * 60)
print("REAL-WORLD: State management and transitions")
print("=" * 60)

# State machine using dict
state_transitions = {
    'stopped': ['running', 'removed'],
    'running': ['paused', 'stopped'],
    'paused': ['running', 'stopped'],
    'removed': [],
}

current_state = 'stopped'
print(f"Current state: {current_state}")

valid_next = state_transitions[current_state]
print(f"Valid next states: {valid_next}")

# Transition
new_state = 'running'
if new_state in valid_next:
    current_state = new_state
    print(f"Transitioned to: {current_state}")

print("\n" + "=" * 60)
print("REAL-WORLD: Config management")
print("=" * 60)

# Default config
default_config = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'timeout': 30,
}

# User config (partial)
user_config = {
    'port': 9000,
    'debug': True,
}

# Merge configs
final_config = {**default_config, **user_config}
print("Default config:", default_config)
print("User config:", user_config)
print("Final config:", final_config)

print("\n" + "=" * 60)
print("REAL-WORLD: Multi-level data access safely")
print("=" * 60)

data = {
    'users': [
        {'id': 1, 'profile': {'age': 30, 'city': 'NYC'}},
        {'id': 2, 'profile': {'age': 25}},
    ]
}

# Safe nested access
def get_nested(d, *keys, default=None):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, {})
        else:
            return default
    return d if d else default

age = get_nested(data, 'users', 0, 'profile', 'age')
city = get_nested(data, 'users', 1, 'profile', 'city', default='Unknown')

print(f"User 1 age: {age}")
print(f"User 2 city: {city}")

print("\n" + "=" * 60)
print("DICT COMPREHENSION PATTERNS")
print("=" * 60)

# Inverting key-value
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Filtering dict
all_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
filtered = {k: v for k, v in all_data.items() if v > 2}
print(f"\nFiltered (values > 2): {filtered}")

# Transforming values
numbers = {'a': 1, 'b': 2, 'c': 3}
doubled = {k: v*2 for k, v in numbers.items()}
print(f"Doubled values: {doubled}")

# Conditional values
data = {'a': 10, 'b': -5, 'c': 20}
abs_values = {k: abs(v) for k, v in data.items()}
print(f"Absolute values: {abs_values}")

print("\n" + "=" * 60)
print("PERFORMANCE NOTES")
print("=" * 60)

print("Dictionary operations (average case):")
print("  Access by key: O(1) - hash table lookup")
print("  Insert: O(1) - hash table insertion")
print("  Delete: O(1) - hash table deletion")
print("  Search by value: O(n) - must check all values")

print("\nDictionaries in Python 3.7+:")
print("  Maintain insertion order")
print("  More memory efficient")
print("  Faster due to optimizations")

