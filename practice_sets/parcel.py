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
    # 5. Reject 0 as the first number
    # 6a. Remember where the first number appears

    first_number_index = None  # None means no number position has been recorded yet

    # The first number may appear at different indexes
    # search each index from the third character to the end
    # range gives the loop a sequence of numbers to move through
    # range() is like giving the loop a route map
    # let index take every position from 2 up to, but not including, the length of the reference
    # Start at index 2 because the first two indexes, 0 and 1, were already checked
    for index in range(2, len(reference)):
        character = reference[index]  # get the character stored at the current index

        if character.isnumeric():  # when the first numeric character is found
            first_number_index = index  # save its position

            # reject the reference if the first number is 0
            if character == "0":
                return False

            break

    # safeguard: reject if no number was found
    if first_number_index is None:
        return False

    # 6b. start checking after the first number
    # 6c. reject any later character that is not numeric
    # start at the character after the first number, then continue to the end
    # check every character after the first number
    # if even one of them is not numeric, reject the reference

    for index in range(first_number_index + 1, len(reference)):
        character = reference[index]  # get the character at the current index

        # once numbers begin, every later character must also be numeric
        if not character.isnumeric():
            return False

    # 7. check the final two characters are numeric
    # take the last two characters
    # if they are not both numeric, reject the reference
    # a colon with nothing after it means continue to the end
    if not reference[-2:].isnumeric():
        return False

    return True


main()
