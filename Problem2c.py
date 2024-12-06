import os
import secrets
from argon2 import PasswordHasher  # pip install argon2-cffi
from argon2.exceptions import VerifyMismatchError

# Initialize Password Hasher
ph = PasswordHasher()

def add_user(username, password, password_file, role):
    # Check if user already exists
    if os.path.exists(password_file):
        with open(password_file, "r") as file:
            for line in file:
                stored_username, _, _, _ = line.strip().split(":")
                if stored_username == username:
                    raise ValueError("Username already exists.")
    
    # Generate salt and hash
    salt = secrets.token_hex(16)
    hashed_password = ph.hash(password + salt)

    # Write to the password file: username:salt:hashed_password:role
    with open(password_file, "a") as file:
        file.write(f"{username}:{salt}:{hashed_password}:{role}\n")
    print(f"User {username} added successfully.")

def verify_user(username, password, password_file, role):
    if not os.path.exists(password_file):
        raise ValueError("Password file does not exist.")
    with open(password_file, "r") as file:
        for line in file:
            # Each line format: username:salt:hashed_password:stored_role
            stored_username, salt, stored_hash, stored_role = line.strip().split(":")
            if stored_username == username:
                try:
                    ph.verify(stored_hash, password + salt)
                    # Optionally, you can verify the role here if needed
                    # For now, we just confirm the password. The caller can re-check the role if desired.
                    return True
                except VerifyMismatchError:
                    return False
    return False

def retrieve_records(username, password, password_file):
    if not os.path.exists(password_file):
        return 0, 0, "User not found!"

    with open(password_file, "r") as file:
        for line in file:
            stored_username, salt, stored_hash, stored_role = line.strip().split(":")
            if stored_username == username:
                # Attempt to verify this user's credentials
                try:
                    ph.verify(stored_hash, password + salt)
                    # If verification succeeds, return their username and role
                    return stored_username, stored_role, "User Found!"
                except VerifyMismatchError:
                    # Wrong password for this user
                    return 0, 0, "User not found!"
    # If we reach here, username was not found
    return 0, 0, "User not found!"

def main():
    password_file = "passwd.txt"
    print("Password Management System")
    while True:
        print("\n1. Add User\n2. Verify User\n3. Retrieve Records\n4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            role = input("Enter Role: ").strip()
            add_user(username, password, password_file, role)

        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            role = input("Enter Role: ").strip()

            if verify_user(username, password, password_file, role):
                print("Authentication successful!")
            else:
                print("Authentication failed!")

        elif choice == "3":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            user, user_role, message = retrieve_records(username, password, password_file)
            if user != 0:
                print(f"{message}\nUsername: {user}\nRole: {user_role}")
            else:
                print(message)

        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
