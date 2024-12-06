import unittest
import os
from Problem3b import is_password_valid
from Problem3a import add_user
class TestEnrollment(unittest.TestCase):

    def setUp(self):
        # Create a temporary password file for testing
        self.test_file = "test_passwd.txt"
        with open(self.test_file, "w") as f:
            pass

    def tearDown(self):
        # Clean up the test password file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_valid_password_enrollment(self):
        """Test Valid Password Enrollment"""
        # Valid username and password
        username = "testuser"
        password = "Valid123!"
        valid, message = is_password_valid(username, password)
        self.assertTrue(valid, "Password should be valid.")
        add_user(username, password, self.test_file, "Client")
        with open(self.test_file, "r") as f:
            content = f.read()
        self.assertIn(username, content, "Username should be present in the password file.")

    def test_password_too_short(self):
        """Test Password Too Short"""
        username = "testuser"
        password = "Short1!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to length.")
        self.assertEqual(message, "Password must be 8-12 characters long.")

    def test_password_too_long(self):
        """Test Password Too Long"""
        username = "testuser"
        password = "VeryLongPassword123!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to length.")
        self.assertEqual(message, "Password must be 8-12 characters long.")

    def test_password_missing_uppercase(self):
        """Test Password Missing Uppercase"""
        username = "testuser"
        password = "valid123!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to missing uppercase.")
        self.assertEqual(message, "Password must include at least one uppercase letter.")

    def test_password_missing_lowercase(self):
        """Test Password Mising LowerCase"""
        username = "testuser"
        password = "VALID123!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to missing lowercase.")
        self.assertEqual(message, "Password must include at least one lowercase letter.")

    def test_password_missing_digit(self):
        """Test Password Missing Digits"""
        username = "testuser"
        password = "ValidPass!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to missing digit.")
        self.assertEqual(message, "Password must include at least one numerical digit.")

    def test_password_missing_special_character(self):
        """Test Password Missing Special Character"""
        username = "testuser"
        password = "ValidPass123"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid due to missing special character.")
        self.assertEqual(message, "Password must include at least one special character (!, @, #, $, %, *, &).")

    def test_password_common_weak(self):
        """Test Password Common Weak"""
        username = "testuser"
        password = "password"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid because it is common and weak.")
        self.assertEqual(message, "Password is too common and insecure.")

    
    def test_password_matches_username(self):
        """"Test Password Matches Username"""
        username = "testuser"
        password = "Testuser123!"
        valid, message = is_password_valid(username, password)
        self.assertFalse(valid, "Password should be invalid because it matches the username.")
        self.assertEqual(message, "Password must not match or include the username.")

if __name__ == "__main__":
    unittest.main(verbosity=2)