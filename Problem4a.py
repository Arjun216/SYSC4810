from Problem2c import verify_user

def login_interface():
    print("Welcome to the Login System")
    print("===========================")

    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if not username or not password:
            print("Error: Both username and password are required. Please try again.\n")
            continue

        if verify_user(username, password, "passwd.txt"):
            print(f"Login successful! Welcome, {username}.\n")
            break
        else:
            print("Error: Invalid username or password. Please try again.\n")

if __name__ == "__main__":
    login_interface()
