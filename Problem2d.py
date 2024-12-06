import os
import unittest
from Problem2c import add_user, verify_user

class TestPasswordFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary password file for testing
        self.test_file = "temp.txt"
        with open(self.test_file, "w") as f:
            pass


    def test_add_new_user(self):
        # Add a new user and check if the record is written
        add_user("testuser", "TestPass123!", self.test_file)
        with open(self.test_file, "r") as f:
            content = f.read()
        self.assertIn("testuser", content)
        self.assertTrue(content.strip().count(":") == 2)  # Ensure format is correct

    def test_prevent_duplicate_usernames(self):
        # Add a user and attempt to add the same username again
        add_user("testuser", "TestPass123!", self.test_file)
        with self.assertRaises(ValueError) as context:
            add_user("testuser", "AnotherPass123!", self.test_file)
        self.assertEqual(str(context.exception), "Username already exists.")

    def test_verify_correct_password(self):
        # Add a user and verify with the correct password
        add_user("testuser", "TestPass123!", self.test_file)
        self.assertTrue(verify_user("testuser", "TestPass123!", self.test_file))

    def test_verify_incorrect_password(self):
        # Add a user and verify with an incorrect password
        add_user("testuser", "TestPass123!", self.test_file)
        self.assertFalse(verify_user("testuser", "WrongPass123!", self.test_file))

    def test_verify_nonexistent_user(self):
        # Attempt to verify a user that doesn't exist
        self.assertFalse(verify_user("nonexistentuser", "RandomPass123!", self.test_file))

    def test_unique_salt_for_users_with_same_password(self):
        # Add two users with the same password
        add_user("user1", "SamePassword123!", self.test_file)
        add_user("user2", "SamePassword123!", self.test_file)
        with open(self.test_file, "r") as f:
            lines = f.readlines()
        
        salt_user1 = lines[0].split(":")[1]
        salt_user2 = lines[1].split(":")[1]

        self.assertNotEqual(salt_user1, salt_user2, "Salt values should be unique for each user.")
    def tearDown(self):
        # Clean up the test password file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
