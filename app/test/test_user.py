import unittest
from app.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='albertbyrone')
    def test_password_setter(self):
        self.assertTrue(self.new_user.secure_password is not None)

    def test_no_access_password(self):
        with self.assertRaises(ArithmeticError):
            self.new_user.password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('albertbyrone'))
