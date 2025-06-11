import random
import string

# Function to generate a strong password
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character sets
    lowercase = string.ascii_lowercase      # a-z
    uppercase = string.ascii_uppercase      # A-Z
    digits = string.digits                  # 0-9
    symbols = string.punctuation            # !@#$%^&*()...

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining characters randomly
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list so it's random
    random.shuffle(password)

    # Join and return the password as a string
    return ''.join(password)

# Main function
def main():
    print("Welcome to the Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Your secure password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
