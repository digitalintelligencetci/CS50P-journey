# contain between 6 and 10 characters
# start with exactly two letters
# contain only letters and numbers
# after the first two letters, at least one number must appear
# once a number appears, no letters may appear afterward
# the first number cannot be 0
# the final two characters must be numbers
# valid reference pattern: at least two letters → possibly more letters → then numbers only
# once the number section begins, letters cannot return.


# 1. Check the length
# 2. Check the first two characters
# 3. Check all characters are alphanumeric
# 4. Find the first number
# 5. Reject 0 as the first number
# 6. Check everything after the first number is numeric
#   6a. Remember where the first number appears.
#   6b. Start checking at the character after that position.
#   6c. If any later character is not numeric, return False.
#   6d. Do not return True until all remaining rules pass.
# 7. Check the final two characters are numeric
# 8. Return True only if everything passes


def main():
    parcel = input("Parcel: ")
    if is_valid(parcel):
        print("Valid")
    else:
        print("Invalid")


# this function can be thought of as security checkpoints
def is_valid(reference):
    if (
        len(reference) < 6 or len(reference) > 10
    ):  # length check between 6 and 10 characters
        return False

    if not reference[:2].isalpha():  # check the first two characters
        return False

    if not reference.isalnum():  # check all characters are alphanumeric
        return False

    # 4. Find the first number and confirm one exists
    number_found = False

    for character in reference[2:]:
        if character.isnumeric():
            number_found = True

        # 5. Reject 0 as the first number
        if character == "0":
            return False

        break

    if not number_found:
        return False

    # 6. check everything after the first number is numeric
    first_number_index = index  # a variable name representing the current position

    # 6a. remember where the first number appears
    # in this example the first number appears at index 2
    # search each index from the third character to the end
    # range gives the loop a sequence of numbers to move through
    # range() is like giving the loop a route map
    # let index take every position from 2 up to, but not including, the length of the reference
    # this loop checks starting from index 2 because prior loops already checks the first 2 indexes [0 and 1]
    for index in range(2, len(reference)):




main()
