import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password): # Function to check the strength of the password
    length = len(password)
    strength = 0
    
    # Add points for password length
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if length >= 16:
        strength += 1
    
    # Add points for different types of characters
    categories = {
        'lower': any(char.islower() for char in password),
        'upper': any(char.isupper() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special': any(char in string.punctuation for char in password)
    }
    
    strength += sum(categories.values())
    
    # Penalize common patterns or dictionary words 
    common_patterns = [
        '123', 'abc', 'password', 'qwerty', 'letmein', 'trustno1'
    ]
    if any(pattern in password.lower() for pattern in common_patterns):
        strength -= 1
    # Penalize repeating characters
    if any(password.count(char) > 1 for char in password):
        strength -= 1
        
    
    return strength

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
        print("Password Strength:", password_strength(password))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    if(input("Do you want to generate another password? (y/n): ").lower() == 'y'):
        main()
if __name__ == "__main__":
    main()
