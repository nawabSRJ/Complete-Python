# enumerate function is mostly used with loops, but it can be used in other contexts as well
# it returns an enumerate object which is an iterator that produces pairs of index and value
# basic usage with a list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# you can also specify a different starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

# enumerate can be used with any iterable, not just lists
text = "hello"
for index, char in enumerate(text):
    print(f"Index: {index}, Character: {char}") 

# enumerate can be used in list comprehensions and other expressions
squared_indices = [index**2 for index, value in enumerate(fruits)]
print(squared_indices)

# enumerate can be used with unpacking in more complex data structures
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
for index, (name, age) in enumerate(data):
    print(f"Index: {index}, Name: {name}, Age: {age}")

