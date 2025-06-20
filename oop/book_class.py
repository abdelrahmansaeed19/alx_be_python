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

""""
- [Got]
Deleting 1984

(14 chars long)
[stderr]: Traceback (most recent call last):
  File "main.py", line 17, in <module>
    main()
  File "main.py", line 8, in main
    print(my_book)  # Expected to use __str__
  File "/tmp/correction/6030073846597538746600292581665252316563_5/100940/1264650/oop/book_class.py", line 14, in __str__
    return f"{self.title} by {self.author}, published in {self.published_year}"
AttributeError: 'Book' object has no attribute 'published_year'

(431 chars long)
[Expected]
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984

(91 chars long)
[stderr]: [Anything]
(0 chars long)

"""