import json
import os
from .book import Book
from .member import Member


class Library:
    """Main library system"""

    def __init__(self, books_file="data/books.json", members_file="data/members.json"):
        self.books = {}
        self.members = {}
        self.books_file = books_file
        self.members_file = members_file
        self.load_data()

    # ------------------------
    # Book Methods
    # ------------------------

    def add_book(self, title, author, isbn, year=None):
        if isbn in self.books:
            return False, "Book already exists."

        self.books[isbn] = Book(title, author, isbn, year)
        return True, "Book added successfully."

    def find_book(self, isbn):
        return self.books.get(isbn)

    def search_books(self, keyword):
        results = []
        for book in self.books.values():
            if (keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or
                keyword == book.isbn):
                results.append(book)
        return results

    # ------------------------
    # Member Methods
    # ------------------------

    def register_member(self, name, member_id):
        if member_id in self.members:
            return False, "Member already exists."

        self.members[member_id] = Member(name, member_id)
        return True, "Member registered successfully."

    def find_member(self, member_id):
        return self.members.get(member_id)

    # ------------------------
    # Borrow / Return
    # ------------------------

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            return False, "Member not found."
        if not book:
            return False, "Book not found."

        success, msg = member.borrow_book(isbn)
        if not success:
            return False, msg

        success, msg = book.check_out(member_id)
        if not success:
            member.return_book(isbn)
            return False, msg

        return True, msg

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False, "Invalid member or book."

        member.return_book(isbn)
        return book.return_book()

    # ------------------------
    # File Operations
    # ------------------------

    def save_data(self):
        os.makedirs("data", exist_ok=True)

        with open(self.books_file, "w") as f:
            json.dump({isbn: book.to_dict() for isbn, book in self.books.items()}, f, indent=4)

        with open(self.members_file, "w") as f:
            json.dump({mid: member.to_dict() for mid, member in self.members.items()}, f, indent=4)

    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, "r") as f:
                books_data = json.load(f)
                for isbn, data in books_data.items():
                    self.books[isbn] = Book.from_dict(data)

        if os.path.exists(self.members_file):
            with open(self.members_file, "r") as f:
                members_data = json.load(f)
                for mid, data in members_data.items():
                    self.members[mid] = Member.from_dict(data)
