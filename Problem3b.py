# List of common weak passwords
weak_passwords = {"password", "123456", "qwerty", "letmein", "welcome", "admin", "iloveyou"}

def is_password_valid(username, password):
      # Check if password is weak
    if password.lower() in weak_passwords:
        return False, "Password is too common and insecure."
    
    # Check length
    if not (8 <= len(password) <= 12):
        return False, "Password must be 8-12 characters long."
    
    # Check for required character types
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one numerical digit."
    if not any(char in "!@#$%*&" for char in password):
        return False, "Password must include at least one special character (!, @, #, $, %, *, &)."
    
 
    
    # Check if password matches the username
    if username.lower() in password.lower():
        return False, "Password must not match or include the username."
    
    # If all checks pass
    return True, "Password is valid."

# Test the password checker
if __name__ == "__main__":
    print("Proactive Password Checker")
    print("==========================")
    username = input("Enter your username: ").strip()
    while True:
        password = input("Enter your password: ").strip()
        valid, message = is_password_valid(username, password)
        if valid:
            print("Password is valid. Proceeding with signup...")
            break
        else:
            print(f"Error: {message}")
