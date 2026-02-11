import unittest
from library_system.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.books = {}
        self.library.members = {}

    def test_add_book(self):
        success, _ = self.library.add_book("Python", "Author", "111")
        self.assertTrue(success)
        self.assertIn("111", self.library.books)

    def test_register_member(self):
        success, _ = self.library.register_member("Vaibhav", "MEM1")
        self.assertTrue(success)
        self.assertIn("MEM1", self.library.members)

    def test_borrow_book(self):
        self.library.add_book("Python", "Author", "111")
        self.library.register_member("Vaibhav", "MEM1")
        success, _ = self.library.borrow_book("MEM1", "111")
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
