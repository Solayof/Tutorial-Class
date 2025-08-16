class Shape:
    """Base class for all shapes."""
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    

shape = Shape("Generic Shape")
print(f"Shape: {shape.name}")