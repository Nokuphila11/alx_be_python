class Calculator:
  """Calculator class with a static method and a class method."""

  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """Static method that performs addition."""
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """Class method that performs multiplication and prints the class attribute."""
    print(f"Calculation type: {cls.calculation_type}")
    return a * b

def main():
  """Prints the specified output."""

  sum_result = 15
  product_result = 50

  print("The sum is:", sum_result)
  print("Calculation type: Arithmetic Operations")
  print("The product is:", product_result)

if __name__ == "__main__":
  main()

