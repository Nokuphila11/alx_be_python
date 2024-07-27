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
    return pi * self.radius**2
