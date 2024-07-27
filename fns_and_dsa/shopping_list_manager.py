def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Start with an empty shopping list
    shopping_list = []

    while True:
        # Display the menu
        display_menu()
        
        # Get user input
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Item
            item = input("Enter the name of the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("You must enter a non-empty item name.")
        
        elif choice == '2':
            # Remove Item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")
        
        elif choice == '3':
            # View List
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':
            # Exit
            print("Goodbye!")
            break
        
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


