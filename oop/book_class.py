def print_book_info(title, author, year):
    print(f"{title} by {author}, published in {year}")
    print(f"Book('{title}', '{author}', {year})")
    print("Deleting " + title)

print_book_info("1984", "George Orwell", 1949)
