class Book:
    def __init__(self, title, author):
        self.title = title
        self.author =author
    def __str__(self):
        return f"{self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{super().__str__()}, File size: {self.file_size}MB"
 class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  
        self.page_count = page_count 

    def __str__(self):
        return f"{super().__str__()}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)  
        
    def list_books(self):
        print("Library Collection:")
        for book in self.books:
            print(book)  

if __name__ == "__main__":
    library = Library()

    ebook1 = EBook("1984", "George Orwell", 1.5)
    printbook1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 281)

    library.add_book(ebook1)
    library.add_book(printbook1)
    library.list_books()
  
    
     
        