# Demonstrating method overriding in a subclass

class Animal:
    def sound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def sound(self):
        print('Bark!')

class Cat(Animal):
    def sound(self):
        print('Meow!')

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.sound()
