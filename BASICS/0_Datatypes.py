num = 8
name = "Srajan"
surname = 'saxena'
gender = 'M'
single = True
weight = 70.5
a = 1,7234  # *no error on assigning a numeric value with comma but this will not be considered as a numeric value instead as a tuple

print('Number:', num, type(num))
print('Name:', name, type(name))
print('Surname:', surname, type(surname))
print('Gender:', gender, type(gender))
print('Single:', single, type(single))
print('Weight:', weight, type(weight))

# -------------- Collection Data Types --------------
# Also covered in COLLECTIONS folder

# 1. List
# Lists are 'mutable', ordered collection of items. They can contain elements of different data types.
my_list = [1, 2, 3, 'four', 'five', 6.0, True]
print('List:', my_list, type(my_list))

# 2. Tuple
# Tuples are 'immutable', ordered collection of items. They can also contain elements of different data types.
my_tuple = (1, 2, 3, 'four', 'five', 6.0, True)
print('Tuple:', my_tuple, type(my_tuple))

# 3. Set
# Sets are 'mutable', unordered collection of unique items. They can contain elements of different data types.
my_set = {1, 2, 3, 'four', 'five', 6.0, True}
print('Set:', my_set, type(my_set))

mySet2 = {1,2,2}
print('Set2:', mySet2, type(mySet2))
# In the above example, the duplicate value '2' is automatically removed from the set, demonstrating that sets only store unique items. No issues arise at compile time.
# * Note : The order of elements in a set is not guaranteed, and it may change each time you run the program. This is because sets are implemented as hash tables, which do not maintain any specific order for their elements.


# 4. Dictionary
# Dictionaries are 'mutable', unordered collection of key-value pairs. Keys must be unique and immutable, while values can be of any data type.
my_dict = {
    'name': 'Srajan',
    'age': 21,
    'is_student': True,
    'courses': ['Python', 'Data Science']
}
print('Dictionary:', my_dict, type(my_dict))
# In the above example, we have a dictionary with keys 'name', 'age', 'is_student', and 'courses', each associated with a corresponding value. The keys are unique and immutable (strings in this case), while the values can be of different data types (string, integer, boolean, and list).


# 5. String
# Strings are 'immutable' sequences of characters. They can be defined using single quotes, double quotes, or triple quotes.
# Also covered in STRINGS folder
my_string = "Hello, World!"
print('String:', my_string, type(my_string))

# Note: In Python, there are also other data types such as 'NoneType' (for representing the absence of a value), 'complex' (for complex numbers), and 'bytes' (for binary data). However, the above examples cover the most commonly used data types in Python.

nothing = None
print('Nothing:', nothing, type(nothing))

