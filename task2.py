class Member:
    def init(self, member_id, name, has_subscription=False):
        self.member_id = member_id
        self.name = name
        self.has_subscription = has_subscription
        self.borrowed_books = []

    def has_valid_subscription(self):
        if self.has_subscription:
            return True
        else:
            print(f"{self.name}, you need a valid subscription to borrow books.")
            return False

    def borrow_book(self, book):
        if self.has_valid_subscription():
            if book.copies_available > 0:
                self.borrowed_books.append(book)
                book.copies_available -= 1
                print(f"{self.name} borrowed '{book.title}'.")
            else:
                print(f"Sorry, '{book.title}' is not available for borrowing.")
                
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.copies_available += 1
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"You did not borrow '{book.title}' from the library.")

class Library:
    def init(self, name, books):
        self.name = name
        self.books = books

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} - Copies Available: {book.copies_available}")


# Example Usage:
book1 = Book(1, "The Catcher in the Rye", "J.D. Salinger", 5)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 3)

member1 = Member(101, "John Doe")

library = Library("City Library", [book1, book2])

library.display_available_books()

member1.borrow_book(book1)
member1.borrow_book(book2)

library.display_available_books()

member1.return_book(book2)

library.display_available_books()