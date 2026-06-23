students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"},
}

def show_dict():
    for key,value in students.items():
        print(key ,':', value)


# Adding new entries in dict
students["Srajan"] = {"age":21,"grade" : "A+"}
print(students)
print()
show_dict()


# Removing entries
removed = students.pop('Srajan')
print(removed)  # You won't see name here since it's a key, will only get value in here


# to remove the last inserted item
last = students.popitem()
print(last) # here you get both key and value as a tuple, since popitem() returns a tuple of (key, value) of the last inserted item

print()
# Merging dictionaris
dict1 = {'name':'Srajan', 'age':21}
dict2 = {'gender':'Male', 'course':'BCA'}

print('Preview : ',dict1 | dict2)
dict1 = dict1 | dict2
print('Now check : ', dict1)

print()
# Checking for keys 
user = {'name':'Alice', 'age':25, 'gender':'Female'}
print('Is name an attribute in user? : ', 'name' in user)

print()
# Nested structures in dictionaries
company = {
    'name' : 'Infosys',
    'employees': {
        'Alice': {'age':21,'gender':'Female','major':'Computer Science'},
        'Bob': {'age':22,'gender':'Male','major':'Finance'}
    },
    'locations':['Lucknow','Kanpur','Agra']
}

# print(company)
print('Employees in company : ', company['employees'])
print('Alice in company : ', company['employees']['Alice'])
print('Does Bob named person works here? : ', 'Bob' in company['employees'])

print()
company.clear()
print('Now company is : ', company)