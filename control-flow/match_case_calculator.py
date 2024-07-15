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
