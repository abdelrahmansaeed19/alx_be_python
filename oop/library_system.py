class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"
    # def __del__(self):
    #     print(f"Deleting book: {self.title} by {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

    def __repr__(self):
        return f"EBook(title={self.title!r}, author={self.author!r}, file_size={self.file_size!r})"

    # def __del__(self):
    #     print(f"Deleting ebook: {self.title} by {self.author}, File Size: {self.file_size}")

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook(title={self.title!r}, author={self.author!r}, page_count={self.page_count!r})"

    # def __del__(self):
    #     print(f"Deleting print book: {self.title} by {self.author}, Page Count: {self.page_count}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            #print(f"Added: {book}")
        else:
            print("Only instances of Book or its subclasses can be added.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed: {book}")
        else:
            print("Book not found in the library.")

    def list_books(self):
        for book in self.books:
            print(book)
    
    # def __del__(self):
    #     print("Deleting library and its books:")
    #     for book in self.books:
    #         del book
    #     self.books.clear()
    #     print("Library deleted.")