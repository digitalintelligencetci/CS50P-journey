# contain between 6 and 10 characters
# start with exactly two letters
# contain only letters and numbers
# after the first two letters, at least one number must appear
# once a number appears, no letters may appear afterward
# the first number cannot be 0
# the final two characters must be numbers


# 1. Check the length
# 2. Check the first two characters
# 3. Check all characters are alphanumeric
# 4. Find the first number
# 5. Reject 0 as the first number
# 6. Check everything after it is numeric
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


main()
