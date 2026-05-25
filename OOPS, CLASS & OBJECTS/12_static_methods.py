# Demonstrating static methods that do not depend on instance state
#
# Static methods are functions defined inside a class that do not access the instance
# (self) or the class (cls). They are useful when you want to group related helper
# functions with a class, without requiring an object instance.
#
# When to use static methods:
# - The method is conceptually related to the class but does not need instance or class data.
# - You want a utility function alongside the class namespace.
# ! Most important part, we can still use add() with the help of an object of class and it will not throw any ERROR, because the decorator @staticmethod is used before it but if we remove that then due to Automatic Injection of arguments it will throw error.
# ? So basically the decorator of @staticmethod just tell the python to stop the automatic injection
# * Why do we need 'self' methods or instance methods? Because Static methods cannot access object-specific data automatically, for that instance methods are used with 'self' prop that can differentiate between objects, since objects can and mostly do hold separate data
# Difference from class methods:
# - staticmethod does not receive cls or self automatically.
# - classmethod receives cls and can modify or inspect class-level state.
#
# Example use case:
# - Math utilities, validators, formatters, or conversions that belong with the class but don't depend on object state.

class MathHelpers:

    @staticmethod
    def add(a, b):
        '''Add two numbers without using instance or class state.'''
        return a + b

    @staticmethod
    def multiply(a, b):
        '''Multiply two numbers without using instance or class state.'''
        return a * b

    def circumference(self,r):
        return 3.14 * MathHelpers.multiply(r,r)
    
print(MathHelpers.add(5, 7))
print(MathHelpers.multiply(3, 4))

obj = MathHelpers()
print('Here is the add : ',obj.add(1,2))
print('Here is the circumference : ',obj.circumference(2))
