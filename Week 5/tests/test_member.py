import unittest
from library_system.member import Member


class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Vaibhav", "MEM001")

    def test_borrow_book(self):
        success, _ = self.member.borrow_book("123")
        self.assertTrue(success)
        self.assertIn("123", self.member.borrowed_books)

    def test_return_book(self):
        self.member.borrow_book("123")
        success, _ = self.member.return_book("123")
        self.assertTrue(success)
        self.assertNotIn("123", self.member.borrowed_books)


if __name__ == "__main__":
    unittest.main()
