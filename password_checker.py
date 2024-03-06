import re

def check_password_strength(password):
    # Minimum length requirement
    min_length = 8
    
    # Check length
    if len(password) < min_length:
        return "Password should be at least {} characters long.".format(min_length), "Weak"
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter.", "Weak"
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter.", "Weak"
    
    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one number.", "Weak"
    
    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password should contain at least one special character.", "Weak"
    
    # If all criteria are met
    return "Password meets complexity requirements.", "Strong"

def main():
    password = input("Enter your password: ")
    message, strength = check_password_strength(password)
    print("\nResult:")
    print(message)
    print("Strength: {}".format(strength))

if __name__ == "__main__":
    main()
