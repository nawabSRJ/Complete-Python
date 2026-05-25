# Demonstrating static methods that do not depend on instance state

class MathHelpers:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathHelpers.add(5, 7))
print(MathHelpers.multiply(3, 4))
