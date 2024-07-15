def main():
    # Ask user to input the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Print the square pattern
    for _ in range(size):
        print('*' * size)

if __name__ == "__main__":
    main()
