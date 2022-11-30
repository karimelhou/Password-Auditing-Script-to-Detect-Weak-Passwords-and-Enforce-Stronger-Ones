import string
import random

# Check for weak passwords
def is_weak_password(password):
    # Check for length
    if len(password) < 8:
        return True
    # Check for special characters
    if any(char in string.punctuation for char in password):
        return False
    # Check for upper and lowercase letters
    if not any(char.isupper() for char in password):
        return True
    if not any(char.islower() for char in password):
        return True
    # Check for numbers
    if not any(char.isdigit() for char in password):
        return True
    return False

# Enforce stronger passwords
def enforce_strong_password(password):
    # Generate a random string of characters
    chars = string.ascii_letters + string.digits + string.punctuation
    random_str = ''.join(random.choice(chars) for i in range(8))
    # Append it to the password
    new_password = password + random_str
    # Return the new password
    return new_password

# Take the user's password
password = input("Please enter your password: ")

# Check if the password is weak
if is_weak_password(password):
    # Enforce a stronger password
    new_password = enforce_strong_password(password)
    print("Your new password is: " + new_password)
else:
    print("Your password is strong enough.")