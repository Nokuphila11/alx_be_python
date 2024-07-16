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

