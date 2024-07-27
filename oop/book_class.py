class Book:
  """Represents a book with title, author, and year."""

  def __init__(self, title, author, year):
    """Initializes a Book instance."""
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    """Returns a user-friendly string representation of the book."""
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """Returns a string that can recreate the Book instance."""
    return f"Book('{self.title}', '{self.author}', {self.year})"

  def __del__(self):
    """Prints a message when the Book instance is deleted (optional)."""
    print(f"Deleting {self.title}")  # Simulate deletion

# Provided for testing (leave this at the bottom)
if __name__ == "__main__":
  main()  # Run the main function if this script is executed directly
