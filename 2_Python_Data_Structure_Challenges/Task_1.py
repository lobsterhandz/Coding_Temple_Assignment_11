# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, title, author):
    """
    Function to add a new book to the library.
    :param library: list of existing books (list of tuples)
    :param title: title of the new book (str)
    :param author: author of the new book (str)
    """
    # Create a new book tuple
    new_book = (title, author)
    
    # Check for duplicates
    if new_book in library:
        print(f"The book '{title}' by {author} already exists in the library.")
    else:
        # Add the new book to the library
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added to the library.")

# Adding new books to the library
add_book(library, "1984", "George Orwell")  # Duplicate
add_book(library, "Fahrenheit 451", "Ray Bradbury")  # New book

# Print the updated library
print("Updated Library:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")
