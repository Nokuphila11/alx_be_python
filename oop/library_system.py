class Book:
  """Base class representing a book."""

  def __init__(self, title, author):
    """Initializes the book with title and author."""
    self.title = title
    self.author = author

class EBook(Book):
  """Derived class representing an ebook."""

  def __init__(self, title, author, file_size):
    """
    Initializes the ebook with additional file_size attribute.
    Calls the base class __init__ for title and author.
    """
    super().__init__(title, author)
    self.file_size = file_size

class PrintBook(Book):
  """Derived class representing a printed book."""

  def __init__(self, title, author, page_count):
    """
    Initializes the printed book with additional page_count attribute.
    Calls the base class __init__ for title and author.
    """
    super().__init__(title, author)
    self.page_count = page_count

class Library:
  """Class representing a library that manages a collection of books."""

  def __init__(self):
    """Initializes the library with an empty list of books."""
    self.books = []

  def add_book(self, book):
    """Adds a Book, EBook, or PrintBook instance to the library."""
    if isinstance(book, Book):
      self.books.append(book)
    else:
      print(f"Invalid book type: {type(book)}")

  def list_books(self):
    """Prints details of each book in the library."""
    if not self.books:
      print("No books in the library.")
      return

    for book in self.books:
      print(f"{book.title} by {book.author}")  # Print common attributes



