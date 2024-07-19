def safe_divide(numerator, denominator):
  """Performs division handling division by zero and non-numeric input."""
  try:
    # Attempt conversion to floats
    numerator = float(numerator)
    denominator = float(denominator)
  except ValueError:
    return "Invalid input: Please provide numeric values."

  try:
    # Perform division with ZeroDivisionError handling
    result = numerator / denominator
    return result
  except ZeroDivisionError:
    return "Division by zero is not allowed."

# Example usage (uncomment for testing)
# num = input("Enter numerator: ")
# den = input("Enter denominator: ")
# result = safe_divide(num, den)
# print(result)
