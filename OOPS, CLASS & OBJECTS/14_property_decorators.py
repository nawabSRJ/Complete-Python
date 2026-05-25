# Demonstrating property decorators to manage attributes with getter/setter behavior

# Property decorators allow a class to expose an attribute-like interface while keeping control over access and validation. This creates cleaner usage than explicit getter/setter methods.

# When to use property decorators:
# - You want to compute a value on demand but access it like an attribute.
# - You need to validate or transform values before setting them.
# - You want to keep backward-compatible attribute access while changing implementation details later.

# Practical use case:
# - validate width and height values before assignment.
# - compute area or other derived values without requiring a separate method call.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # So now width is no longer a normal method. It becomes a special descriptor/property object.
    @property
    def width(self):
        '''Read access for width.''' 
        return self._width

    # “Attach this function as the setter for the existing width property.”
    @width.setter
    def width(self, value):
        '''Validate width before updating the private variable.'''
        if value <= 0:
            raise ValueError('Width must be positive')
        self._width = value

    @property
    def area(self):
        '''Computed property that returns derived data from the object.'''
        return self._width * self._height

rect = Rectangle(5, 3)
print('Width:', rect.width)
print('Area:', rect.area)
rect.width = 7
print('New width:', rect.width)
print('New area:', rect.area)


# If you have to understand this in a traditional setup, this is the corresponding code for that :
# class Rectangle:

#     def get_width(self):
#         return self._width

#     def set_width(self, value):
#         if value <= 0:
#             raise ValueError
#         self._width = value

#     width = property(get_width, set_width)