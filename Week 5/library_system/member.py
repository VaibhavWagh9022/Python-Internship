class Member:
    """Represents a library member"""

    def __init__(self, name, member_id, max_books=5):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = max_books

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.max_books:
            return False, "Borrow limit reached."

        self.borrowed_books.append(isbn)
        return True, "Book added to member account."

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            return False, "This member did not borrow this book."

        self.borrowed_books.remove(isbn)
        return True, "Book removed from member account."

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"], data.get("max_books", 5))
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)}"
