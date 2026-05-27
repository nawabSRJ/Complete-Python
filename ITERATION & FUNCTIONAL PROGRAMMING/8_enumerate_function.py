# enumerate() adds a counter to an iterable and returns pairs of index and value.
# It is especially useful when you need both the element and its position.

colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)

# Start the counter at a custom value:
for position, color in enumerate(colors, start=1):
    print(position, color)

# When to use enumerate():
# - when loop index and value are both required
# - when you want cleaner code than manual index management
# - when you want consistent loop behavior with built-in iterable support

# Example: create a numbered list of items
items = ['apple', 'banana', 'cherry']
numbered = [f'{i}. {item}' for i, item in enumerate(items, start=1)]
print('\nNumbered list:', numbered)
