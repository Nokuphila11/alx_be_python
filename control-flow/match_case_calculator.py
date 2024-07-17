def calculate(num1, num2, operation):
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Cannot divide by zero."
        case _:
            return "Error: Invalid operation"

    return result

# Main program
if __name__ == "__main__":
    # Input the first number from the user
    num1 = float(input("Enter the first number: "))
    
    # Input the second number from the user
    num2 = float(input("Enter the second number: "))
    
    # Input the operation from the user
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform the calculation using the calculate function
    result = calculate(num1, num2, operation)
    
    # Display the result or error message
    if isinstance(result, float):
        print(f"The result is {result:.2f}.")  # Displaying result with 2 decimal places if it's a float
    else:
        print(result)  # Error message handling (e.g., division by zero)
