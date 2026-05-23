# NESTED COLLECTIONS BASICS
# Working with nested lists, dicts, tuples, and mixed structures.

print("=" * 60)
print("NESTED LISTS - LIST OF LISTS")
print("=" * 60)

# Creating nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix (3x3):")
for row in matrix:
    print(f"  {row}")

# Accessing nested elements
print(f"\nmatrix[0]: {matrix[0]}")
print(f"matrix[0][0]: {matrix[0][0]}")
print(f"matrix[1][2]: {matrix[1][2]}")
print(f"matrix[-1][-1]: {matrix[-1][-1]}")

# Modifying nested elements
matrix[1][1] = 0
print(f"\nAfter matrix[1][1] = 0:")
print(f"matrix: {matrix}")

# Iterating nested lists
print("\nIterating row by row:")
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()

print("\nUsing enumerate for indices:")
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")

print("\n" + "=" * 60)
print("NESTED DICTIONARIES")
print("=" * 60)

# Creating nested dict
company = {
    'name': 'TechCorp',
    'employees': {
        'engineers': {
            'alice': {'salary': 100000, 'level': 'senior'},
            'bob': {'salary': 80000, 'level': 'junior'},
        },
        'managers': {
            'charlie': {'salary': 90000, 'reports': 5},
        }
    },
    'locations': ['NYC', 'SF'],
}

print("Company structure (nested dict):")
print(f"  Name: {company['name']}")
print(f"  Alice salary: {company['employees']['engineers']['alice']['salary']}")
print(f"  Charlie reports: {company['employees']['managers']['charlie']['reports']}")

# Iterating nested dict
print("\nIterating through nested structure:")
for dept, staff in company['employees'].items():
    print(f"{dept}:")
    for name, info in staff.items():
        print(f"  {name}: {info}")

print("\n" + "=" * 60)
print("MIXED NESTED STRUCTURES")
print("=" * 60)

# List of dicts
students = [
    {'name': 'Alice', 'grades': [90, 85, 92]},
    {'name': 'Bob', 'grades': [78, 82, 88]},
    {'name': 'Charlie', 'grades': [95, 93, 97]},
]

print("List of dicts (students):")
for student in students:
    print(f"  {student['name']}: {student['grades']}")

# Dict of lists
department = {
    'engineering': ['Alice', 'Bob', 'David'],
    'sales': ['Charlie', 'Eve'],
    'hr': ['Frank'],
}

print("\nDict of lists (department):")
for dept, people in department.items():
    print(f"  {dept}: {people}")

# List of tuples
coordinates = [(0, 0), (1, 2), (3, 4), (5, 6)]
print(f"\nList of tuples: {coordinates}")
print(f"First coordinate: {coordinates[0]}")
print(f"First coordinate x: {coordinates[0][0]}")

# Dict with tuple keys
graph = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (0, 1): [(0, 0), (1, 1)],
}

print(f"\nDict with tuple keys (graph):")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")

print("\n" + "=" * 60)
print("ACCESSING AND MODIFYING NESTED DATA")
print("=" * 60)

data = {
    'users': [
        {'id': 1, 'name': 'Alice', 'scores': [10, 20, 30]},
        {'id': 2, 'name': 'Bob', 'scores': [15, 25, 35]},
    ]
}

print("Original data:")
print(f"  {data}")

# Access nested value
score = data['users'][0]['scores'][1]
print(f"\nAlice's second score: {score}")

# Modify nested value
data['users'][0]['scores'][1] = 22
print(f"After modifying Alice's second score to 22:")
print(f"  {data['users'][0]['scores']}")

# Add to nested list
data['users'][0]['scores'].append(40)
print(f"After appending 40 to Alice's scores:")
print(f"  {data['users'][0]['scores']}")

print("\n" + "=" * 60)
print("BUILDING NESTED STRUCTURES DYNAMICALLY")
print("=" * 60)

# Building from raw data
raw_data = [
    ('Alice', 'NYC', 90),
    ('Bob', 'LA', 85),
    ('Charlie', 'NYC', 95),
]

# Create nested structure
by_city = {}
for name, city, score in raw_data:
    if city not in by_city:
        by_city[city] = []
    by_city[city].append({'name': name, 'score': score})

print("Raw data:", raw_data)
print("\nGrouped by city:")
for city, people in by_city.items():
    print(f"  {city}: {people}")

print("\n" + "=" * 60)
print("NESTED LIST COMPREHENSIONS")
print("=" * 60)

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in nested for num in row]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

# Create nested structure with comprehension
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print(f"\nMatrix created with comprehension:")
for row in matrix:
    print(f"  {row}")

# Filter nested data
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens_only = [[x for x in row if x % 2 == 0] for row in data]
print(f"\nFilter even numbers from {data}:")
for row in evens_only:
    print(f"  {row}")

print("\n" + "=" * 60)
print("SEARCHING IN NESTED STRUCTURES")
print("=" * 60)

data = [
    {'id': 1, 'name': 'Alice', 'tags': ['python', 'sql']},
    {'id': 2, 'name': 'Bob', 'tags': ['java', 'kotlin']},
    {'id': 3, 'name': 'Charlie', 'tags': ['python', 'javascript']},
]

# Find user with specific tag
tag_to_find = 'python'
users_with_tag = [user for user in data if tag_to_find in user['tags']]
print(f"Users with tag '{tag_to_find}':")
for user in users_with_tag:
    print(f"  {user['name']}")

# Find value in nested structure
target_id = 2
user = next((user for user in data if user['id'] == target_id), None)
print(f"\nUser with id {target_id}: {user}")

print("\n" + "=" * 60)
print("COUNTING IN NESTED STRUCTURES")
print("=" * 60)

# Count total items in nested list
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total_count = sum(len(row) for row in matrix)
print(f"Matrix: {matrix}")
print(f"Total elements: {total_count}")

# Count occurrences in nested data
students = [
    {'name': 'Alice', 'grades': [90, 85, 92]},
    {'name': 'Bob', 'grades': [78, 82, 88]},
]

grade_above_85 = sum(1 for s in students for g in s['grades'] if g > 85)
print(f"\nGrades above 85: {grade_above_85}")

