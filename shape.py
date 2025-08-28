class Shape:
    """Base class for all shapes."""
    length = 0 # attribute
    width = 0 # attribute
    def __init__(self, name): # constructor i.e initialize the object
        self.name = name
        print(f"{self.name} is created.")

    def area(self): # method i.e function inside a class, its know as property
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    

shape = Shape("Generic Shape")
print(shape.length) # accessing attribute
print(shape.width)  # accessing attribute
# print(f"Shape: {shape.name}")

# OOP - object oriented programming
# class - blueprint

class Rectangle(Shape): # inheritance
    pass


rect = Rectangle("My Rectangle")
print(rect.name) # accessing attribute from parent class