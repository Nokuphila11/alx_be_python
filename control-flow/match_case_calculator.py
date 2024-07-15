def main():
    # Ask user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Ask user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Ask user to choose the operation
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform the calculation based on the chosen operation
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation")
        return
    
    # Print the result
    print(f"The result is {result}.")
