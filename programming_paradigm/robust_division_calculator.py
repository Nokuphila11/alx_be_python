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


def safe_divide(numerator, denominator):
  """Performs division with error handling for zero division and non-numeric input."""
  try:
    # Attempt to convert arguments to floats for division
    numerator = float(numerator)
    denominator = float(denominator)
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"  # Format to 2 decimal places
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."
