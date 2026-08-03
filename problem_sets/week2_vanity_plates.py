# Ask the user for a plate

# Check whether:
#   its length is between 2 and 6
#   its first two characters are letters - not method
#   it contains only letters and numbers
#   any numbers appear only at the end
#   the first number is not 0

# If every check passes:
#   return True
# Otherwise:
#   return False


def main():
    plate = input("Plate: ")  # gets the user input
    if is_valid(plate):  # plate is now passed into is_valid
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):  # special set of instructions of what to do with the input.
    if len(s) < 2 or len(s) > 6:  # checks if the length is between 2 and 6.
        return False  # returns false if it does not meet the required condition.

    if not s[:2].isalpha():  # checks the first two characters are letters.
        return False  # not is used as a reverse method or if something must be true the code should read "if it is not what is true".

    if not s.isalnum():  # checks it contains only letters and numbers.
        return False

    for i in range(len(s)):
        if s[i].isnumeric():  # = assigns a value and == compares two values
            if s[i] == "0":
                return False

            if not s[i:].isnumeric():
                return False
            break  # break / stops the loop
    return True  # return false stops the entire function and sends back false.


main()
