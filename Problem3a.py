from Problem2c import add_user

def signup_interface():
    print("Welcome to the Signup System")
    print("=============================")
    
    while True:
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        role = input("Enter role: ").strip()


        # Validate inputs
        if not username or not password or not role:
            print("Error: All fields are required! Please try again.\n")
            continue

        try:
            # Add the new user
            add_user(username, password, role, "passwd.txt")
            print(f"User '{username}' signed up successfully!\n")
            break
        except ValueError as e:
            print(f"Error: {str(e)}\n")
        except Exception as ex:
            print(f"An unexpected error occurred: {str(ex)}\n")
            break

if __name__ == "__main__":
    signup_interface()
