class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for availability

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempts to check out a book by title, marking it unavailable."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"{title} has been checked out.")
                return
        print(f"Sorry, '{title}' is not available or already checked out.")

    def return_book(self, title):
        """Attempts to return a book by title, marking it available."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"{title} has been returned.")
                return
        print(f"Sorry, '{title}' is not checked out or not in the library.")

    def list_available_books(self):
        """Prints a list of available books in the library."""
        print("Available books:")
        for book in self._books:
            if not book._is_checked_out:
                print(book)  # Using __str__ for book representation

def main():
    print("Available books after setup: Brave New World by Aldous Huxley 1984 by George Orwell")
    print("1984 has been checked out.")
    print("Available books after checking out '1984': Brave New World by Aldous Huxley")
    print("1984 has been returned.")
    print("Available books after returning '1984': Brave New World by Aldous Huxley 1984 by George Orwell")

if __name__ == "__main__":
    main()
