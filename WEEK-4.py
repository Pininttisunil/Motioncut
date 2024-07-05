import random
import string

def generate_password(length):
    if length < 4:  # Ensuring the password length is sufficient for a strong password
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a mix of all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password list to ensure randomness and convert it to a string
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    # User input for password length and number of passwords
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return

    # Generate and display the passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        try:
            print(generate_password(length))
        except ValueError as e:
            print(e)
            break

if __name__ == "__main__":
    main()
