# Function to perform arithmetic operations
def calculate(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number != 0:  # Check for division by zero
            return first_number / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Main program
if __name__ == "__main__":
    # Input the numbers and operation from the user
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Calculate the result
    result = calculate(first_number, second_number, operation)

    # Print the result
    print(f"The result is {result}.")
