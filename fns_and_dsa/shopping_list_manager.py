def displaymenu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shoppinglist = []
    while True:
        displaymenu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shoppinglist.append(input (""Enter the item to add:"" ))

        elif choice == '2':
            item = input("Enter item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not on list")

        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name == "__main":
    main()
def displaymenu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shoppinglist = []
    while True:
        displaymenu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input ("Enter the item to add: " )
            shoppinglist.append(item)

        elif choice == '2':
            item = input("Enter item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not on list")

        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name == "__main":
    main()
