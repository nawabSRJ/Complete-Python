# Demonstrating property decorators to manage attributes with getter/setter behavior

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Width must be positive')
        self._width = value

    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 3)
print('Width:', rect.width)
print('Area:', rect.area)
rect.width = 7
print('New width:', rect.width)
print('New area:', rect.area)
