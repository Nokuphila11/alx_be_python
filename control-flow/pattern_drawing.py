def main():
    # Ask user to input the size of the pattern
    size = int(input("Enter the size of the pattern (positive integer): "))
    
    # Validate input
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Draw the square pattern
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end=" ")
            col += 1
        print()  # move to the next line after each row is complete
        row += 1

if __name__ == "__main__":
    main()
