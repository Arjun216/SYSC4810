import unittest
from Problem1c import authenticate, AccessControl, roles_permissions, is_business_hour
from Problem2c import retrieve_records, add_user, verify_user

class TestLoginAndAccessControl(unittest.TestCase):

    def test_valid_login_and_permissions(self):
        # Test valid login for a Client
        user, message = authenticate("SashaKim", "ClientPass123!")
        self.assertIsNotNone(user)
        self.assertEqual(message, "Login successful.")
        self.assertEqual(user.role, "Client")
        self.assertEqual(user.permissions, roles_permissions["Client"])

        # Verify permissions for Client
        self.assertIn("view_account_balance", user.permissions)
        self.assertNotIn("Modify investment portfolio", user.permissions)

    def test_invalid_login(self):
        # Test invalid username
        user, message = authenticate("InvalidUser", "RandomPass123!")
        self.assertIsNone(user)
        self.assertEqual(message, "Invalid username.")

        # Test invalid password
        user, message = authenticate("SashaKim", "WrongPass123!")
        self.assertIsNone(user)
        self.assertEqual(message, "Invalid password.")

    def test_access_rights_client(self):
        # Test access rights for a Client
        user, _ = authenticate("SashaKim", "ClientPass123!")
        self.assertIn("view_account_balance", user.permissions)
        self.assertNotIn("Modify investment portfolio", user.permissions)

    def test_access_rights_premium_client(self):
        # Test access rights for a Premium Client
        user, _ = authenticate("NoorAbbasi", "Premium$2023")
        self.assertIn("modify_investment_portfolio", user.permissions)
        self.assertNotIn("view_private_consumer_instruments", user.permissions)

    def test_access_rights_financial_advisor(self):
        # Test access rights for a Financial Advisor
        user, _ = authenticate("MikaelChen", "Advisor2023!")
        self.assertIn("view_private_consumer_instruments", user.permissions)
        self.assertNotIn("View money market instruments", user.permissions)

    def test_access_rights_financial_planner(self):
        # Test access rights for a Financial Planner
        user, _ = authenticate("EllisNakamura", "Planner#2023")
        self.assertIn("view_money_market_instruments", user.permissions)
        self.assertIn("modify_any_investment_portfolio", user.permissions)

    def test_access_rights_teller_business_hours(self):
        # Test Teller access during business hours
        user, _ = authenticate("AlexHayes", "TellerPass456!")
        self.assertIn("view_any_account_balance", user.permissions)

    def test_teller_outside_business_hours(self):
        # Simulate outside business hours for Teller
        def mock_is_business_hour():
            return False

        original_is_business_hour = is_business_hour()
        AccessControl.is_business_hour = staticmethod(mock_is_business_hour)

        user, _ = authenticate("AlexHayes", "TellerPass456!")
        self.assertNotIn("View any client account balance", user.permissions)

        # Restore the original function
        AccessControl.is_business_hour = original_is_business_hour

if __name__ == "__main__":
    unittest.main()
