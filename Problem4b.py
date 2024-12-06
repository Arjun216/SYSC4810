from Problem2c import verify_user, retrieve_records
from Problem1c import AccessControl, authenticate

# Access control policy (as defined in the justInvest system)
roles_permissions = {
    "client": ["View account balance", "View investment portfolio", "View advisor contact"],
    "premium C]client": ["View account balance", "View investment portfolio", "Modify investment portfolio", "View planner contact"],
    "financial advisor": ["View any client account balance", "View any client investment portfolio", "Modify any client investment portfolio", "View private consumer instruments"],
    "financial planner": ["View any client account balance", "View any client investment portfolio", "Modify any client investment portfolio", "View money market instruments", "View private consumer instruments"],
    "teller": ["View any client account balance", "View any client investment portfolio (Business hours only)"]
}

def display_access_privileges(user, stored_role):
    """
    Displays access privileges for the authenticated user.
    """
    print("\n--- Access Privileges ---")
    print(f"Username: {user}")
    print(f"Role: {stored_role}")
    print("Access Rights:")
    print(roles_permissions[stored_role.lower()])
    print("--------------------------\n")

def login_and_display_privileges():
    """
    Login interface that displays access privileges after successful authentication.
    """
    print("Welcome to the justInvest System")
    print("================================")

    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if not username or not password:
            print("Error: Both username and password are required. Please try again.\n")
            continue

        user, stored_role, message = retrieve_records(username, password, "passwd.txt")
        if user:
            print(f"Username and password valid")
            display_access_privileges(user, stored_role)
            break
        else:
            print("Error: Invalid username or password. Please try again.\n")

if __name__ == "__main__":
    login_and_display_privileges()
