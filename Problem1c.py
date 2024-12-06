import datetime

# Define roles and permissions
roles_permissions = {
    "Client": ["view_account_balance", "view_investment_portfolio", "view_advisor_contact"],
    "Premium Client": ["view_account_balance", "view_investment_portfolio","view_advisor_contact", "modify_investment_portfolio", "view_planner_contact"],
    "Financial Advisor": ["view_any_account_balance", "view_any_investment_portfolio", "modify_any_investment_portfolio", "view_private_consumer_instruments"],
    "Financial Planner": ["view_any_account_balance", "view_any_investment_portfolio", "modify_any_investment_portfolio", "view_money_market_instruments", "view_private_consumer_instruments"],
    "Teller": ["view_any_account_balance", "view_any_investment_portfolio"]
}

# Sample users
users = {
    "SashaKim": {"role": "Client", "password": "ClientPass123!"},
    "EmeryBlake": {"role": "Client", "password": "ClientPass123!"},
    "NoorAbbasi": {"role": "Premium Client", "password": "Premium$2023"},
    "ZuriAdebayo": {"role": "Client", "password": "ClientPass123!"},
    "MikaelChen": {"role": "Financial Advisor", "password": "Advisor2023!"},
    "JordanRiley": {"role": "Financial Advisor", "password": "ClientPass123!"},
    "EllisNakamura": {"role": "Financial Planner", "password": "Planner#2023"},
    "HarperDiaz": {"role": "Financial Planner", "password": "Planner#2023"},
    "AlexHayes": {"role": "Teller", "password": "TellerPass456!"},
    "AdairPatel": {"role": "Teller", "password": "TellerPass456!"}
}

# Check if access is during business hours for Tellers
def is_business_hour():
    current_time = datetime.datetime.now().time()
    start = datetime.time(9, 0)
    end = datetime.time(17, 0)
    return start <= current_time <= end

# Access control class
class AccessControl:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.permissions = roles_permissions.get(role, [])
    
    def perform_operation(self, operation):
        if self.role == "Teller" and not is_business_hour():
            return "Access Denied: Tellers can only operate during business hours (9:00 AM - 5:00 PM)."
        if operation in self.permissions:
            return f"Operation '{operation}' executed successfully."
        return f"Access Denied: You are not authorized to perform '{operation}'."

# Authenticate user 
def authenticate(username, password):
    user = users.get(username)
    if not user:
        return None, "Invalid username."
    if user["password"] != password:
        return None, "Invalid password."
    return AccessControl(username, user["role"]), "Login successful."

# Main program
def main():
    print("Welcome to the justInvest System!")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user, message = authenticate(username, password)
    if not user:
        print(message)
        return

    print(message)
    while True:
        print("\nAvailable operations:")
        for id, operation in enumerate(user.permissions, start=1):
            print(f"{id}. {operation}")
        choice = input("Choose an operation number or type 'exit' to quit: ").strip()

        if choice.lower() == 'exit':
            print("Logged Out Successfully")
            break
        if choice.isdigit() and 1 <= int(choice) <= len(user.permissions):
            operation = user.permissions[int(choice) - 1]
            print(user.perform_operation(operation))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
