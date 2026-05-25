# Demonstrating some magic (dunder) methods to control object behavior

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)
print('Sum:', p1 + p2)
print('Equal:', p1 == Point(1, 2))
