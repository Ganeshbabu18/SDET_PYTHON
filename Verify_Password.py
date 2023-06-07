# write Python program for verify password
# input = "Ganesh@123"

def verify_password(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in "!@#$%^&*()-_=+[{]}\|;:',<.>/?`~" for char in password)

    # Verify password based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_criteria:
        return True
    else:
        return False

# Prompt the user to enter a password
password_input = "Ganesh@123"

# Verify the password
if verify_password(password_input):
    print("Password is valid.")
else:
    print("Password is invalid.")


# output
# Password is valid.