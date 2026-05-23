# NESTED COLLECTIONS ADVANCED
# Deep copying, mutation through references, recursive patterns, real-world scenarios.

import copy
import json

print("=" * 60)
print("SHALLOW COPY VS DEEP COPY")
print("=" * 60)

original = {
    'name': 'Alice',
    'scores': [90, 85, 92],
    'info': {'age': 30, 'city': 'NYC'}
}

# Shallow copy - only top level is copied
shallow = original.copy()
print("Original:", original)
print("Shallow copy:", shallow)

# Modifying nested mutable inside shallow copy affects original
shallow['scores'][0] = 0
print("\nAfter shallow['scores'][0] = 0:")
print("  original scores:", original['scores'])
print("  shallow scores:", shallow['scores'])

# Deep copy - entire structure is copied
original2 = {
    'name': 'Bob',
    'scores': [80, 75, 88],
    'info': {'age': 25, 'city': 'LA'}
}

deep = copy.deepcopy(original2)
print("\n\nWith deep copy:")
deep['scores'][0] = 0
print("After deep['scores'][0] = 0:")
print("  original scores:", original2['scores'])
print("  deep scores:", deep['scores'])

print("\n" + "=" * 60)
print("ALIASING - MULTIPLE REFERENCES TO SAME OBJECT")
print("=" * 60)

# List aliasing
list_a = [1, 2, 3]
list_b = list_a  # Both point to same object
print("list_a:", list_a)
print("list_b:", list_b)

list_a.append(4)
print("After list_a.append(4):")
print("  list_a:", list_a)
print("  list_b:", list_b)
print("  list_a is list_b:", list_a is list_b)

# Nested aliasing - common pitfall
matrix_template = [[0, 0, 0]] * 3
print("\n\nmatrix_template = [[0, 0, 0]] * 3:")
print("  matrix:", matrix_template)

matrix_template[0][0] = 1
print("After matrix[0][0] = 1:")
print("  matrix:", matrix_template)
print("  All rows point to SAME list object!")

# Correct way
matrix_correct = [[0, 0, 0] for _ in range(3)]
print("\nmatrix_correct = [[0, 0, 0] for _ in range(3)]:")
matrix_correct[0][0] = 1
print("After matrix[0][0] = 1:")
print("  matrix:", matrix_correct)
print("  Each row is independent")

print("\n" + "=" * 60)
print("MUTATION THROUGH NESTED REFERENCES")
print("=" * 60)

# Shared reference in dict
person1 = {'name': 'Alice', 'hobbies': ['reading', 'gaming']}
person2 = {'name': 'Bob', 'hobbies': person1['hobbies']}

print("person1:", person1)
print("person2:", person2)
print("person1['hobbies'] is person2['hobbies']:", person1['hobbies'] is person2['hobbies'])

person2['hobbies'].append('cooking')
print("\nAfter person2['hobbies'].append('cooking'):")
print("  person1['hobbies']:", person1['hobbies'])
print("  person2['hobbies']:", person2['hobbies'])
print("  Both modified because they share the same list!")

print("\n" + "=" * 60)
print("RECURSIVE FUNCTIONS ON NESTED DATA")
print("=" * 60)

# Sum all numbers in nested structure
def sum_nested(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

nested_nums = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(f"Nested structure: {nested_nums}")
print(f"Sum of all numbers: {sum_nested(nested_nums)}")

# Flatten nested list recursively
def flatten(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flattened = flatten(nested_nums)
print(f"Flattened: {flattened}")

# Search recursively in nested dict
def find_in_dict(d, target_key):
    if target_key in d:
        return d[target_key]
    
    for key, value in d.items():
        if isinstance(value, dict):
            result = find_in_dict(value, target_key)
            if result is not None:
                return result
    return None

nested_dict = {
    'level1': {
        'level2': {
            'target': 'found!'
        }
    }
}

print(f"\nSearching for 'target' in nested dict:")
print(f"Result: {find_in_dict(nested_dict, 'target')}")

print("\n" + "=" * 60)
print("REAL-WORLD: JSON parsing and transformation")
print("=" * 60)

# Parse JSON (similar to API responses)
json_str = '''
{
    "users": [
        {"id": 1, "name": "Alice", "posts": [{"title": "First", "likes": 10}, {"title": "Second", "likes": 20}]},
        {"id": 2, "name": "Bob", "posts": [{"title": "Hello", "likes": 5}]}
    ]
}
'''

data = json.loads(json_str)

print("Parsed JSON structure:")
for user in data['users']:
    print(f"{user['name']}:")
    for post in user['posts']:
        print(f"  - {post['title']} ({post['likes']} likes)")

print("\n" + "=" * 60)
print("REAL-WORLD: Building complex filter expressions")
print("=" * 60)

# Database-like query on nested data
users = [
    {
        'id': 1,
        'name': 'Alice',
        'age': 30,
        'posts': [
            {'id': 1, 'content': 'Hello', 'likes': 100},
            {'id': 2, 'content': 'World', 'likes': 200},
        ]
    },
    {
        'id': 2,
        'name': 'Bob',
        'age': 25,
        'posts': [
            {'id': 3, 'content': 'Test', 'likes': 50},
        ]
    },
]

# Find posts with high engagement
popular_posts = []
for user in users:
    for post in user['posts']:
        if post['likes'] > 75:
            popular_posts.append({
                'author': user['name'],
                'content': post['content'],
                'likes': post['likes']
            })

print("Posts with >75 likes:")
for post in popular_posts:
    print(f"  {post['author']}: {post['content']} ({post['likes']} likes)")

print("\n" + "=" * 60)
print("REAL-WORLD: Graph and tree traversal")
print("=" * 60)

# Tree structure
tree = {
    'value': 1,
    'children': [
        {
            'value': 2,
            'children': [
                {'value': 4, 'children': []},
                {'value': 5, 'children': []},
            ]
        },
        {
            'value': 3,
            'children': [
                {'value': 6, 'children': []},
            ]
        },
    ]
}

# Depth-first traversal
def dfs_values(node):
    values = [node['value']]
    for child in node['children']:
        values.extend(dfs_values(child))
    return values

print("Tree structure (DFS values):", dfs_values(tree))

# Breadth-first traversal
def bfs_values(root):
    from collections import deque
    queue = deque([root])
    values = []
    while queue:
        node = queue.popleft()
        values.append(node['value'])
        queue.extend(node['children'])
    return values

print("Tree structure (BFS values):", bfs_values(tree))

print("\n" + "=" * 60)
print("REAL-WORLD: Configuration merging")
print("=" * 60)

# Deep merge nested dicts
def deep_merge(dict1, dict2):
    result = copy.deepcopy(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result

base_config = {
    'server': {'host': 'localhost', 'port': 8000, 'debug': False},
    'database': {'name': 'default', 'user': 'admin'},
}

env_config = {
    'server': {'port': 9000, 'debug': True},
    'database': {'name': 'production'},
    'logging': {'level': 'INFO'},
}

merged = deep_merge(base_config, env_config)
print("Base config:", base_config)
print("Environment config:", env_config)
print("Merged config:", merged)

print("\n" + "=" * 60)
print("WORKING WITH GENERATOR FOR MEMORY EFFICIENCY")
print("=" * 60)

# Generator for iterating nested structures
def iterate_nested(data):
    if isinstance(data, list):
        for item in data:
            yield from iterate_nested(item)
    elif isinstance(data, dict):
        for value in data.values():
            yield from iterate_nested(value)
    else:
        yield data

nested = [1, [2, 3, [4, 5]], {'a': 6, 'b': [7, 8]}]
print("Nested structure:", nested)
print("All values (using generator):", list(iterate_nested(nested)))

