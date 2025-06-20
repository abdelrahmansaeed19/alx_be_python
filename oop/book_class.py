class Book:
    def __init__(self, title, author, year):
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("Title and author must be strings")
        if not isinstance(year, int):
            raise TypeError("Published year and pages must be integers")
        if year < 0:
            raise ValueError("Published year must be non-negative and pages must be positive")
        self.year = year
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __len__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author)
        return False
    
    def __del__(self):
        print(f"Deleting {self.title}")