# Get a username

# Send it to a validation function

# Inside the validation function:
#   reject an invalid length
#   reject a non-letter beginning
#   reject punctuation or spaces

#   search for at least one number

#   if no number is found:
#       reject it

#   otherwise:
#       approve it


def is_valid(username):
    # 1. Reject an invalid length (must be between 4 and 10 characters)
    if len(username) < 4 or len(username) > 10:
        return False

    # 2. Reject a non-letter beginning
    if not username[0].isalpha():
        return False

    # 3. Reject punctuation or spaces (must be alphanumeric)
    if not username.isalnum():
        return False

    # 4. Search for at least one number
    # Start by assuming something has not been found
    found_number = False

    # Search through the input
    for char in username:
        if char.isdigit():
            # Change that state when it is found
            found_number = True
            break  # Exit loop early once found

    # Check the state after the loop
    if not found_number:  # noqa: SIM103
        return False

    # Otherwise: approve it
    return True


def main():
    # Get a username
    user_input = input("Enter a proposed username: ")

    # Send it to the validation function
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")


# Run the program
main()





