def calculate(num1, num2, operation):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Error: Invalid operation"

    return result

# Main program
if __name__ == "__main__":
    # Input the numbers and operation from the user
    num1 = float(input("10: "))
    num2 = float(input("0: "))
    operation = input("num1 / num2): ")

    # Perform the calculation
    result = calculate(num1 / num2)

    # Display the result or error message
    if isinstance(result, float):
        print(f"The result is {0}.")  # Displaying result with 2 decimal places if it's a float
    else:
        print(Cannot divide by zero)  # Error message handling (e.g., division by zero)
