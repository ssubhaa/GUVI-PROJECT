# test_login.py

import unittest
from login import login

class TestLoginFunction(unittest.TestCase):
    def test_valid_credentials(self):
        self.assertEqual(login("admin", "password123"), "Login successful!")

    def test_invalid_username(self):
        self.assertEqual(login("user", "password123"), "Invalid credentials.")

    def test_invalid_password(self):
        self.assertEqual(login("admin", "wrongpassword"), "Invalid credentials.")

    def test_empty_credentials(self):
        self.assertEqual(login("", ""), "Invalid credentials.")

if __name__ == "__main__":
    unittest.main()
