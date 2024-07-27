# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create instances of EBook and PrintBook
    ebook1 = EBook("Data Science Handbook", "Alice Smith", 12)
    printbook1 = PrintBook("Introduction to Algorithms", "Robert Martin", 500)

    # Create a Library instance
    library = Library()

    # Add books to the library
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()




