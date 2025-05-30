# class Animal:
#     def speak(self):
#         return "I don't have a specific sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Bird(Animal):
#     def speak(self):
#         return "Chirp!"

# # Polymorphism in action
# animals = [Dog(), Cat(), Bird(), Animal()]

# for animal in animals:
#     print(f"{animal.__class__.__name__} says: {animal.speak()}")







class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must override this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



try:
    shape1=Shape()
    shape1.area()
except Exception as e:
    print (e)
# end try