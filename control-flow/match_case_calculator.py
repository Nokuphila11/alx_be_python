
def perform_calculation():
  """Prompts the user for two numbers and an operation, then performs the calculation."""

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Choose the operation (+, -, *, /): ")

  match operation:
    case "+":
      result = num1 + num2
    case "-":
      result = num1 - num2
    case "*":
      result = num1 * num2
    case "/":
      if num2 == 0:
        print("Error: Division by zero")
        return
      else:
        result = num1 / num2
    case _:
      print("Invalid operation")
      return

  print(f"The result is {result}")

if __name__ == "__main__":
  perform_calculation()

