# Working with JSON Files
# =======================
# JSON (JavaScript Object Notation) is a lightweight format for storing structured data.
# It is human-readable and widely used for APIs and configuration files.

import json

# 1. Understanding JSON format
# =============================
# JSON structure mirrors Python dictionaries and lists:
# - Objects: {\"key\": \"value\"} maps to Python dict
# - Arrays: [1, 2, 3] maps to Python list
# - Strings: \"text\" must use double quotes
# - Numbers, booleans, null map to Python types

# 2. Creating and saving JSON data
# ==================================
print("1. Saving data to JSON file:")
student_data = {
    'name': 'Srajan',
    'age': 21,
    'city': 'Delhi',
    'courses': ['Python', 'Data Science', 'Web Development'],
    'is_active': True,
    'gpa': 3.8
}

with open('student.json', 'w') as file:
    json.dump(student_data, file, indent=2)
    print("JSON file created: student.json")

# The indent parameter makes the JSON file human-readable

# 3. Reading JSON data
# ====================
print("\n2. Reading JSON file:")
with open('student.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"Loaded data: {loaded_data}")
    print(f"Name: {loaded_data['name']}")
    print(f"Courses: {loaded_data['courses']}")

# 4. Working with lists of objects
# ==================================
print("\n3. Working with list of JSON objects:")
students_list = [
    {'name': 'Srajan', 'age': 21, 'city': 'Delhi'},
    {'name': 'Aditi', 'age': 20, 'city': 'Mumbai'},
    {'name': 'Ravi', 'age': 22, 'city': 'Bangalore'},
]

with open('students.json', 'w') as file:
    json.dump(students_list, file, indent=2)
    print("List of students saved to JSON")

# Read and display
with open('students.json', 'r') as file:
    students = json.load(file)
    for student in students:
        print(f\"  {student['name']} from {student['city']}\")

# 5. Converting Python objects to JSON
# =====================================
# json.dumps() converts Python object to JSON string (without writing to file).
# json.dump() writes JSON directly to a file.

print("\n4. Converting to JSON string:")
data = {'key': 'value', 'numbers': [1, 2, 3], 'nested': {'a': 1}}
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# 6. Converting JSON string to Python object
# ============================================
# json.loads() parses JSON string into Python object.
# json.load() reads JSON from a file and parses it.

print("\n5. Parsing JSON string:")
json_text = '{\"name\": \"Alice\", \"age\": 25, \"city\": \"London\"}'
parsed_data = json.loads(json_text)
print(f"Parsed data: {parsed_data}")
print(f\"Name: {parsed_data['name']}\")

# 7. Handling nested JSON
# =======================
print("\n6. Working with nested JSON:")
company_data = {
    'name': 'TechCorp',
    'location': 'Bangalore',
    'employees': [
        {'id': 1, 'name': 'Srajan', 'role': 'Developer'},
        {'id': 2, 'name': 'Aditi', 'role': 'Designer'},
        {'id': 3, 'name': 'Ravi', 'role': 'Manager'},
    ],
    'founded': 2015,
    'active': True
}

with open('company.json', 'w') as file:
    json.dump(company_data, file, indent=2)

# Read and access nested data
with open('company.json', 'r') as file:
    company = json.load(file)
    print(f\"Company: {company['name']}\")
    print(\"Employees:\")
    for emp in company['employees']:
        print(f\"  - {emp['name']} ({emp['role']})\")

# 8. Adding to existing JSON file
# ================================
print("\n7. Appending to JSON file:")
with open('students.json', 'r') as file:
    students = json.load(file)

# Add new student
students.append({'name': 'Priya', 'age': 19, 'city': 'Pune'})

# Write back
with open('students.json', 'w') as file:
    json.dump(students, file, indent=2)
    print("New student added to JSON")

# 9. JSON vs Python data type mapping
# ====================================
# JSON Type        Python Type
# object           dict
# array            list
# string           str
# number (integer) int
# number (float)   float
# true             True
# false            False
# null             None

# 10. Handling special types
# ===========================
print("\n8. Handling non-serializable objects:")
from datetime import datetime

# datetime objects are not JSON serializable by default
data_with_date = {
    'event': 'Conference',
    'date': datetime(2026, 6, 15)  # this will cause an error
}

# Solution 1: Convert to string
data_with_date['date'] = str(datetime(2026, 6, 15))
with open('event.json', 'w') as file:
    json.dump(data_with_date, file, indent=2)
print("Event with date saved (converted to string)")

# Solution 2: Use default parameter
def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

event_data = {
    'event': 'Conference',
    'date': datetime(2026, 6, 15)
}

with open('event2.json', 'w') as file:
    json.dump(event_data, file, indent=2, default=default_handler)
print("Event with date saved (using default handler)")

# 11. Key takeaways
# =================
# - json.dump() writes Python object to JSON file.
# - json.load() reads JSON file and converts to Python object.
# - json.dumps() converts Python object to JSON string.
# - json.loads() parses JSON string to Python object.
# - Use indent parameter for readable formatting.
# - Not all Python types are JSON serializable (use default handler).
# - JSON is excellent for configuration files and data exchange.
