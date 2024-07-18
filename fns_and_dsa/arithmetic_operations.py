def perform_operation(num1, num2, operation):
  """
  Performs an arithmetic operation based on the provided parameters.

  Args:
      num1: The first number (float).
      num2: The second number (float).
      operation: The operation to perform (string, must be 'add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the arithmetic operation or a message indicating division by zero.
  """

  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
      # Handle division by zero
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    # Handle invalid operation (optional)
    return "Error: Invalid operation"

# Example usage (assuming this code is in your main.py script)
result = perform_operation(5, 6, "add")
print(f"Result: {result}")
