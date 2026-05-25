# Demonstrating the use of super() to extend parent class behavior

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def details(self):
        print(f'Vehicle: {self.make} {self.model}')

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def details(self):
        super().details()
        print(f'Doors: {self.doors}')

c = Car('Toyota', 'Corolla', 4)
c.details()
