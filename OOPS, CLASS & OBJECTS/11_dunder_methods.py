# Demonstrating some magic (dunder) methods to control object behavior

# Dunder methods are special methods with double underscores before and after the name.
# They allow custom classes to behave like built-in Python types.
# Practical use cases:
# - __repr__ for readable object representation during debugging
# - __add__ to support the + operator for custom objects
# - __eq__ to compare objects by value instead of by identity
#
# Use these methods when you want your custom objects to integrate naturally with
# Python syntax and standard operations.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Called when printing the object or inspecting it in a REPL
        return f'Point(x={self.x}, y={self.y})'

    def __add__(self, other):
        # Enables the + operator for Point objects
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        # Enables equality comparison using ==
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)
print('Sum:', p1 + p2)
print('Equal:', p1 == Point(1, 2))
