# Working with CSV Files
# ======================
# CSV (Comma-Separated Values) is a common format for tabular data.
# This file demonstrates how to read and write CSV files using Python's csv module.

import csv

# 1. Understanding CSV format
# ============================
# CSV files have rows and columns separated by delimiters (usually commas).
# Example:
#   name,age,city
#   Srajan,21,Delhi
#   Aditi,20,Mumbai
#   Ravi,22,Bangalore

# 2. Creating a sample CSV file
# ==============================
print("1. Creating a sample CSV file:")
data = [
    ['Name', 'Age', 'City', 'Occupation'],
    ['Srajan', '21', 'Delhi', 'Student'],
    ['Aditi', '20', 'Mumbai', 'Intern'],
    ['Ravi', '22', 'Bangalore', 'Developer'],
]

with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("CSV file created: employees.csv")

# Note: use newline='' to prevent extra blank lines in the CSV file

# 3. Reading CSV files using csv.reader()
# ========================================
# csv.reader() reads the file row by row as lists.
# Use when: you want simple list-based access to rows.

print("\n2. Reading CSV with csv.reader():")
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 4. Reading CSV files using csv.DictReader()
# ============================================
# csv.DictReader() reads each row as a dictionary with column names as keys.
# Use when: you want to access columns by name instead of index.
# This is more readable and less error-prone.

print("\n3. Reading CSV with csv.DictReader():")
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(f"  Name: {row['Name']}, City: {row['City']}")

# 5. Writing CSV files using csv.writer()
# ========================================
# csv.writer() writes rows as lists to the CSV file.

print("\n4. Writing CSV with csv.writer():")
new_employees = [
    ['Priya', '19', 'Pune', 'Trainee'],
    ['Ankush', '23', 'Hyderabad', 'Consultant'],
]

with open('employees.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_employees)
    print("New rows appended to CSV")

# 6. Writing CSV files using csv.DictWriter()
# ============================================
# csv.DictWriter() writes rows as dictionaries.
# Use when: your data is already in dictionary format.

print("\n5. Writing CSV with csv.DictWriter():")
fieldnames = ['Name', 'Age', 'City', 'Occupation']
data_dicts = [
    {'Name': 'Kavya', 'Age': '21', 'City': 'Chennai', 'Occupation': 'Designer'},
    {'Name': 'Arjun', 'Age': '22', 'City': 'Kolkata', 'Occupation': 'Analyst'},
]

with open('employees2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # writes column names
    writer.writerows(data_dicts)
    print("CSV file created with DictWriter: employees2.csv")

# 7. Filtering and processing CSV data
# =====================================
print("\n6. Filtering CSV data:")
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    delhi_employees = [row for row in reader if row['City'] == 'Delhi']
    print(f"Employees in Delhi: {delhi_employees}")

# 8. CSV with different delimiters
# ==================================
# CSV files can use different delimiters like semicolons, tabs, etc.

print("\n7. Writing CSV with different delimiter:")
with open('data_semicolon.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')  # use semicolon instead of comma
    writer.writerows([
        ['Name', 'Age', 'Score'],
        ['Alice', '20', '85'],
        ['Bob', '21', '90'],
    ])
    print("CSV file with semicolon delimiter created")

# Read it back
print("Reading semicolon-delimited CSV:")
with open('data_semicolon.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

# 9. Quoting and special characters
# ==================================
# CSV quoting handles special characters and newlines in data.

print("\n8. Handling special characters:")
special_data = [
    ['Name', 'Description'],
    ['Item1', 'Simple text'],
    ['Item2', 'Text with \"quotes\"'],
    ['Item3', 'Text with, comma'],
]

with open('special_csv.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(special_data)

print("Reading CSV with special characters:")
with open('special_csv.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 10. Key takeaways
# =================
# - Use csv.reader() for simple list-based access.
# - Use csv.DictReader() for key-based (column name) access.
# - Use csv.DictWriter() when writing dictionary data.
# - Always use newline='' when opening CSV files.
# - csv.QUOTE_MINIMAL handles special characters automatically.
# - Specify delimiter if using something other than comma.
