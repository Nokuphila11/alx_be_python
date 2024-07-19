def divide_numbers(dividend, divisor):
  """Divides two numbers and returns the result."""
  if divisor == 0:
    return "Division by zero is not allowed."
  else:
    result = dividend / divisor
    return result

# Example usage:
dividend = 4
divisor = 2
result = divide_numbers(dividend, divisor)
print(f"The result of the division is {result}")
