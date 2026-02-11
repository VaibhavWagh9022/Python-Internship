import unittest
from library_system.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Python 101", "John Doe", "123")

    def test_initial_state(self):
        self.assertTrue(self.book.available)

    def test_checkout(self):
        success, _ = self.book.check_out("MEM1")
        self.assertTrue(success)
        self.assertFalse(self.book.available)

    def test_return(self):
        self.book.check_out("MEM1")
        success, _ = self.book.return_book()
        self.assertTrue(success)
        self.assertTrue(self.book.available)


if __name__ == "__main__":
    unittest.main()
