# DICTIONARIES BASICS
# Key-value pairs, mutable, unordered (ordered by insertion in 3.7+).

print("=" * 60)
print("DICTIONARY CREATION")
print("=" * 60)

# Different ways to create dictionaries
empty_dict = {}
print("Empty dict using {}:", empty_dict)

literal_dict = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print("Dict literal:", literal_dict)

dict_constructor = dict(name='Bob', age=25, city='LA')
print("Using dict():", dict_constructor)

# From list of tuples
from_pairs = dict([('x', 10), ('y', 20)])
print("From list of tuples:", from_pairs)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
print("Dict comprehension {x: x**2 for x in range(5)}:", squares)

print("\n" + "=" * 60)
print("ACCESSING VALUES")
print("=" * 60)

person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print("Dictionary:", person)

print("\nAccessing with []:")
print("person['name']:", person['name'])
print("person['age']:", person['age'])

# Using get() - safer
print("\nUsing get():")
print("person.get('name'):", person.get('name'))
print("person.get('country'):", person.get('country'))
print("person.get('country', 'Unknown'):", person.get('country', 'Unknown'))

# Accessing non-existent key with []
try:
    print(person['country'])
except KeyError as e:
    print(f"person['country'] raises KeyError: {e}")

print("\n" + "=" * 60)
print("KEYS, VALUES, ITEMS")
print("=" * 60)

student = {'name': 'Charlie', 'grade': 'A', 'gpa': 3.9}
print("Dictionary:", student)

print("\nstudent.keys():", student.keys())
print("list(student.keys()):", list(student.keys()))

print("\nstudent.values():", student.values())
print("list(student.values()):", list(student.values()))

print("\nstudent.items():", student.items())
print("list(student.items()):", list(student.items()))

print("\n" + "=" * 60)
print("ITERATION")
print("=" * 60)

scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
print("Dictionary:", scores)

print("\nIterating over keys:")
for key in scores:
    print(f"  {key}")

print("\nIterating over values:")
for value in scores.values():
    print(f"  {value}")

print("\nIterating over key-value pairs:")
for key, value in scores.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("ADDING AND MODIFYING")
print("=" * 60)

config = {'host': 'localhost', 'port': 8080}
print("Original dict:", config)

config['debug'] = True
print("After config['debug'] = True:", config)

config['port'] = 9000
print("After config['port'] = 9000:", config)

config['database'] = 'postgres'
print("After config['database'] = 'postgres':", config)

print("\n" + "=" * 60)
print("REMOVING ITEMS")
print("=" * 60)

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original dict:", data)

# pop() removes and returns value
removed = data.pop('b')
print(f"After pop('b'), removed value {removed}, dict:", data)

# pop() with default
value = data.pop('z', 'not found')
print(f"pop('z', 'not found') returns: {value}, dict:", data)

# del keyword
del data['c']
print("After del data['c']:", data)

# popitem() removes last inserted item
key, value = data.popitem()
print(f"popitem() removed ({key}: {value}), dict:", data)

print("\n" + "=" * 60)
print("UPDATING DICTIONARIES")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 22, 'c': 3}

print("dict1:", dict1)
print("dict2:", dict2)

# update() method
copy1 = dict1.copy()
copy1.update(dict2)
print("After dict1.update(dict2):", copy1)

# merge with | operator (Python 3.9+)
merged = dict1 | dict2
print("Using dict1 | dict2:", merged)

print("\n" + "=" * 60)
print("MEMBERSHIP TESTING")
print("=" * 60)

user = {'name': 'David', 'age': 28, 'email': 'david@example.com'}
print("Dictionary:", user)

print("\n'name' in user:", 'name' in user)
print("'phone' in user:", 'phone' in user)
print("'David' in user:", 'David' in user)
print("'David' in user.values():", 'David' in user.values())

print("\n" + "=" * 60)
print("NESTED DICTIONARIES")
print("=" * 60)

company = {
    'name': 'TechCorp',
    'employees': {
        'alice': {'role': 'engineer', 'salary': 100000},
        'bob': {'role': 'manager', 'salary': 90000},
    },
    'locations': ['NYC', 'SF', 'London']
}

print("Nested structure:")
print("company['name']:", company['name'])
print("company['employees']['alice']['role']:", company['employees']['alice']['role'])
print("company['locations'][0]:", company['locations'][0])

print("\n" + "=" * 60)
print("DICTIONARY LENGTH AND CLEARING")
print("=" * 60)

inventory = {'apples': 10, 'bananas': 5, 'oranges': 8}
print("Inventory:", inventory)
print("len(inventory):", len(inventory))

inventory.clear()
print("After clear():", inventory)

print("\n" + "=" * 60)
print("EQUALITY AND COMPARISON")
print("=" * 60)

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 2, 'x': 1}
dict_c = {'x': 1, 'y': 3}

print("dict_a:", dict_a)
print("dict_b:", dict_b)
print("dict_c:", dict_c)

print("\ndict_a == dict_b:", dict_a == dict_b)
print("dict_a == dict_c:", dict_a == dict_c)
print("dict_a is dict_b:", dict_a is dict_b)

print("\n" + "=" * 60)
print("COPY VS REFERENCE")
print("=" * 60)

original = {'a': 1, 'b': [2, 3]}
reference = original
shallow_copy = original.copy()

print("Original:", original)

original['a'] = 999
print("\nAfter original['a'] = 999:")
print("  original:", original)
print("  reference:", reference)
print("  shallow_copy:", shallow_copy)

original['b'][0] = 999
print("\nAfter original['b'][0] = 999:")
print("  original:", original)
print("  reference:", reference)
print("  shallow_copy:", shallow_copy)

print("(shallow_copy shares references to nested objects)")

