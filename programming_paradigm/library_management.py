class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False

  def __str__(self):
    return f"{self.title} by {self.author}"

class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title and not book._is_checked_out:
        book._is_checked_out = True
        print(f"{title} has been checked out.")
        return
    print(f"Sorry, '{title}' is not available or already checked out.")

  def return_book(self, title):
    for book in self._books:
      if book.title == title and book._is_checked_out:
        book._is_checked_out = False
        print(f"{title} has been returned.")
        return
    print(f"Sorry, '{title}' is not checked out or not in the library.")

  def list_available_books(self):
    print("Available books:")
    for book in self._books:
      if not book._is_checked_out:
        print(book)


# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out: {book}")
                    return True
        print(f"Book not available: {title}")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned: {book}")
                    return True
        print(f"Book not checked out or not found: {title}")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

