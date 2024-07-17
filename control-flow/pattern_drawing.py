def draw_square_pattern(size):
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end="")
            col += 1
        print()  # Move to the next line after completing the row
        row += 1

# Main program
if __name__ == "__main__":
    # Input the size of the pattern from the user
    size = int(input("Enter the size of the pattern: "))

    # Validate the input size (positive integer)
    while size <= 0:
        print("Please enter a positive integer greater than 0.")
        size = int(input("Enter the size of the pattern: "))

    # Draw the square pattern
    draw_square_pattern(size)


