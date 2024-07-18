<<<<<<< HEAD

def main():
    # Ask user for the first number
    first_number = float(input("Enter the first number: "))

    # Ask user for the second number
    second_number = float(input("Enter the second number: "))

    # Ask user to choose the operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation based on the chosen operation
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero")
            return
    else:
        print("Invalid operation")
        return

    # Print the result
    print(f"The result is {result}.")
=======

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


