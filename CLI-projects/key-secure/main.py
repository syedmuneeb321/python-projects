from random import choice
import string
import getpass
def check_password_strength(password: str) -> list: 
    """Check if the password meets strength requirements."""
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        issues.append("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        issues.append("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        issues.append("Password must contain at least one lowercase letter.")
    if not any(char in string.punctuation for char in password):
        issues.append("Password must contain at least one special character.")

    return issues

def generate_strong_password(length: int = 20) -> str:
    """Generate a strong password with a mix of characters."""
    character_length = int(length/3)
    symbol_digit_length = int(character_length/2)
    
    lower_character = "".join([choice(string.ascii_lowercase) for _ in range(character_length)])
    upper_character = "".join([choice(string.ascii_uppercase) for _ in range(character_length)])
    digits = "".join([choice(string.digits) for _ in range(symbol_digit_length)])
    symbols = "".join([choice(string.punctuation) for _ in range(symbol_digit_length)])

    return lower_character + upper_character + digits + symbols



def main():
    print("Welcome to the Password Strength Checker!\n")
    

    password = getpass.getpass("Enter your password: ")
    issues = check_password_strength(password)
    if issues:
        print("Password is not strong enough:")
        for issue in issues:
            print(f"- {issue}")
        print("\nGenerating a strong password for you...\n")
        strong_password = generate_strong_password()
        print(f"Your new strong password is: {strong_password}")
    else:
        print("Password is strong enough!")


if __name__ == "__main__":
    main()
