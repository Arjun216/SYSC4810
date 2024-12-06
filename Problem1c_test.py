import unittest
from datetime import datetime, time
from unittest.mock import patch

from Problem1c import AccessControl, authenticate, is_business_hour

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

    @patch('Problem1c.is_business_hour', return_value=True)
    def test_teller_business_hours(self, mock_is_business_hour):
        user, _ = authenticate("AlexHayes", "TellerPass456!")
        # When it's business hours, Tellers should be allowed
        self.assertEqual(user.perform_operation("view_any_account_balance"), "Operation 'view_any_account_balance' executed successfully.")

    @patch('Problem1c.is_business_hour', return_value=False)
    def test_edge_case_teller_outside_business_hours(self, mock_is_business_hour):
        user, _ = authenticate("AlexHayes", "TellerPass456!")
        # Outside of business hours, Tellers should be denied
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

if __name__ == "__main__":
    unittest.main()
