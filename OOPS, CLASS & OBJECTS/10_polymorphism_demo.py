# Demonstrating polymorphism with a common interface across different classes

class Shape:
    def area(self):
        raise NotImplementedError('Subclasses must implement area()')

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Circle(3)]
for shape in shapes:
    print(f'Area: {shape.area()}')
