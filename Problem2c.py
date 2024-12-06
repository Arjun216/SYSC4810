import os
import secrets
from argon2 import PasswordHasher #pip install argon2-cffi
from argon2.exceptions import VerifyMismatchError
from Problem1c import AccessControl
# Initialize Password Hasher
ph = PasswordHasher()

# File path for the password file

# Add a new user
def add_user(username, password, role, password_file):
    if os.path.exists(password_file):
        with open(password_file, "r") as file:
            if any(line.startswith(username + ":") for line in file):
                raise ValueError("Username already exists.")

    salt = secrets.token_hex(16)
    hashed_password = ph.hash(password + salt)

    with open(password_file, "a") as file:
        file.write(f"{username}:{salt}:{hashed_password}:{role}\n")
    print(f"User {username} added successfully.")

# Verify user credentials
def verify_user(username, password, password_file):
    if not os.path.exists(password_file):
        raise ValueError("Password file does not exist.")
    with open(password_file, "r") as file:
        for line in file:
            stored_username, salt, stored_hash, stored_role = line.strip().split(":")
            if stored_username == username:
                try:
                    ph.verify(stored_hash, password + salt)
                    return True
                except VerifyMismatchError:
                    return False
    return False

def retrieve_records(username, password, password_file):
    if(verify_user(username, password, password_file)):
        with open(password_file, "r") as file:
            for line in file:
                stored_username, salt, stored_hash, stored_role = line.strip().split(":")
                return stored_username, stored_role, "User Found!"
    else:
        return 0,0, "User not found!"

# Main program
def main():
    password_file = "passwd.txt"
    print("Password Management System")
    while True:
        print("\n1. Add User\n2. Verify User\n3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            add_user(username, password, password_file)

        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if verify_user(username, password, password_file):
                print("Authentication successful!")
            else:
                print("Authentication failed!")

        elif choice == "3":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

