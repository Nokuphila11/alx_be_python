def print_square_pattern(size):
    for _ in range(size):
        print('*' * size)

# Main program
if __name__ == "__main__":
    # Input the size of the pattern from the user
    size = int(input("Enter the size of the pattern: "))

    # Print the square pattern
    print_square_pattern(size)

