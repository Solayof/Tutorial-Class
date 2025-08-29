class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} the animal is created.")
    
    def speak(self):
        return "Sound"
    def info(self):
        return f"This is {self.name}"
    def birth(self):
        return f"{self.name} is born"
    def __str__(self):
        return f"Animal: {self.name}"


class Cat(Animal): # inheritance
    def __init__(self, name): # constructor overriding
        name = "Cat " + name
        super().__init__(name)
    
    def speak(self): # method overriding
        return super().speak() + " Meow Meow"
    
    def __str__(self):
        return super().__str__()
    
animal = Animal("Generic Animal")
print(animal.info())
print(animal.speak())
print("-----------------------")
cat = Cat("Whiskers")
print(cat.info())
print(cat.speak()) # accessing overridden method


print(cat)




class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # def __add__(self, other):
    #     return Point(self.x + other.x, self.y + other.y)

    # def __eq__(self, other):
    #     if isinstance(other, Point):
    #         return self.x == other.x and self.y == other.y
    #     return False
    

point = Point(2, 3)
point2 = Point(4, 5)

x = 2 + 4
y = 3 + 5
new_point = Point(x, y)
print(new_point)

new_p = point + point2 # this will give error
print(new_p)

print(new_p == new_point) # this will give false because they are different objects

dic = {}
