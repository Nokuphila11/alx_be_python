def display_menu():
  """Prints the shopping list menu options."""
  print("\nShopping List Menu")
  print("1. Add item")
  print("2. Remove item")
  print("3. View list")
  print("4. Exit")

def add_item(shopping_list):
  """Prompts the user for an item name and adds it to the shopping list."""
  item = input("Enter the item to add: ")
  shopping_list.append(item)
  print(f"{item} added to shopping list.")

def remove_item(shopping_list):
  """Prompts the user for an item name and removes it from the shopping list if found."""
  item = input("Enter the item to remove: ")
  if item in shopping_list:
    shopping_list.remove(item)
    print(f"{item} removed from shopping list.")
  else:
    print(f"{item} not found in shopping list.")

def view_list(shopping_list):
  """Prints the contents of the shopping list."""
  if not shopping_list:
    print("Shopping list is empty.")
  else:
    print("Shopping List:")
    for item in shopping_list:
      print("- " + item)

def main():
  """Manages the shopping list application."""
  shopping_list = []  # Initialize an empty shopping list
  while True:
    display_menu()  # Show the menu options
    choice = input("Enter your choice: ")

    if choice == '1':
      add_item(shopping_list)  # Add item functionality
    elif choice == '2':
      remove_item(shopping_list)  # Remove item functionality
    elif choice == '3':
      view_list(shopping_list)  # View list functionality
    elif choice == '4':
      print("Goodbye!")  # Exit the program
      break
    else:
      print("Invalid choice. Please try again.")  # Handle invalid choices

if __name__ == "__main__":
  main()
