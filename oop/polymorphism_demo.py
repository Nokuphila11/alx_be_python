from math import pi  # Import pi for circle area calculation

class Shape:
  """Base class representing a shape."""

  def area(self):
    """Raises an error indicating subclasses should implement this method."""
    raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
  """Derived class representing a rectangle."""

  def __init__(self, length, width):
    """Initializes the rectangle with length and width."""
    self.length = length
    self.width = width

  def area(self):
    """Calculates and returns the area of the rectangle."""
    return self.length * self.width

class Circle(Shape):
  """Derived class representing a circle."""

  def __init__(self, radius):
    """Initializes the circle with radius."""
    self.radius = radius

  def area(self):
    """Calculates and returns the area of the circle using pi."""
    return pi * self.radius**2”

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    """Demonstrates polymorphism by calculating areas of different shapes."""
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
import math

def calculate_circle_area(radius):
  """Calculates the area of a circle given its radius."""
  area = math.pi * radius**2
  return area

radius = 7  # Replace with desired radius

circle_area = calculate_circle_area(radius)
print("The area of the Circle is:", circle_area)


