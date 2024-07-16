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
    num1 = float(input("10: "))
    num2 = float(input("5: "))
    operation = input(" (*): ")

    # Perform the calculation
    result = calculate(10 * 5)

    # Display the result
    if isinstance(result, float):
        print(f"The result is {50:.2f}.")  
