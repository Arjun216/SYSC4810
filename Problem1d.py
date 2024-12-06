import unittest
from datetime import datetime, time
from Problem1c import AccessControl, authenticate, is_business_hour
#pip install argon2-cffi


class TestAccessControl(unittest.TestCase):

    def test_valid_user_authorization(self):
        user, message = authenticate("SashaKim", "ClientPass123!")
        self.assertIsNotNone(user)
        self.assertEqual(message, "Login successful.")
        self.assertIn("view_account_balance", user.permissions)
        self.assertEqual(user.perform_operation("view_account_balance"), "Operation 'view_account_balance' executed successfully.")

    def test_unauthorized_operation(self):
        user, _ = authenticate("SashaKim", "ClientPass123!")
        self.assertNotIn("modify_investment_portfolio", user.permissions)
        self.assertEqual(user.perform_operation("modify_investment_portfolio"), "Access Denied: You are not authorized to perform 'modify_investment_portfolio'.")

    def test_teller_business_hours(self):
        user, _ = authenticate("AlexHayes", "TellerPass456!")
        if is_business_hour():
            self.assertEqual(user.perform_operation("view_any_account_balance"), "Operation 'view_any_account_balance' executed successfully.")
        else:
            self.assertEqual(user.perform_operation("view_any_account_balance"), "Access Denied: Tellers can only operate during business hours (9:00 AM - 5:00 PM).")

    def test_premium_client_privileges(self):
        user, _ = authenticate("NoorAbbasi", "Premium$2023")
        self.assertIn("modify_investment_portfolio", user.permissions)
        self.assertIn("view_planner_contact", user.permissions)
        self.assertEqual(user.perform_operation("modify_investment_portfolio"), "Operation 'modify_investment_portfolio' executed successfully.")
        self.assertEqual(user.perform_operation("view_planner_contact"), "Operation 'view_planner_contact' executed successfully.")

    def test_invalid_credentials(self):
        user, message = authenticate("InvalidUser", "WrongPass123!")
        self.assertIsNone(user)
        self.assertEqual(message, "Invalid username.")

    def test_role_specific_operations(self):
        user, _ = authenticate("MikaelChen", "Advisor2023!")
        self.assertIn("view_private_consumer_instruments", user.permissions)
        self.assertNotIn("view_money_market_instruments", user.permissions)
        self.assertEqual(user.perform_operation("view_private_consumer_instruments"), "Operation 'view_private_consumer_instruments' executed successfully.")
        self.assertEqual(user.perform_operation("view_money_market_instruments"), "Access Denied: You are not authorized to perform 'view_money_market_instruments'.")

    def test_edge_case_teller_outside_business_hours(self):
        # Simulate outside business hours
        def mock_is_business_hour():
            return False

        original_is_business_hour = is_business_hour
        globals()["is_business_hour"] = mock_is_business_hour  # Replace the function temporarily
        user, _ = authenticate("AlexHayes", "TellerPass456!")
        self.assertEqual(user.perform_operation("view_any_account_balance"), "Access Denied: Tellers can only operate during business hours (9:00 AM - 5:00 PM).")
        globals()["is_business_hour"] = original_is_business_hour  # Restore the original function

        import unittest

if __name__ == "__main__":
    unittest.main()



