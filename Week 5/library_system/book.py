from datetime import datetime, timedelta


class Book:
    """Represents a book in the library"""

    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def check_out(self, member_id, loan_days=14):
        if not self.available:
            return False, "Book is already borrowed."

        self.available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=loan_days)).strftime("%Y-%m-%d")
        return True, f"Book borrowed successfully. Due date: {self.due_date}"

    def return_book(self):
        if self.available:
            return False, "Book is already available."

        overdue_days = self.days_overdue()

        self.available = True
        self.borrowed_by = None
        self.due_date = None

        if overdue_days > 0:
            return True, f"Book returned. Overdue by {overdue_days} days."
        return True, "Book returned successfully."

    def is_overdue(self):
        if self.due_date and not self.available:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return datetime.now() > due
        return False

    def days_overdue(self):
        if self.is_overdue():
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return (datetime.now() - due).days
        return 0

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"], data["isbn"], data.get("year"))
        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.due_date = data["due_date"]
        return book

    def __str__(self):
        status = "Available" if self.available else f"Borrowed (Due: {self.due_date})"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"
