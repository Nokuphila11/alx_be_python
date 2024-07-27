# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage
if __name__ == "__main__":
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    # Print areas
    print(f"Area of the rectangle: {rectangle.area()}")
    print(f"Area of the circle: {circle.area()}")

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

