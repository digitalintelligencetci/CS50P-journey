#   Get the text
#   Create an empty result
#   Create a collection of vowels

#   For each character:
#   if it is a vowel:
#       do not keep it
#   if it is a space:
#       do not keep it
#   otherwise:
#       add it to the result

#   Print the completed result

text = input("Message: ")       # get the text
result = ""     # create an empty result
vowels = ["a", "e", "i", "o", "u"]      # create a collection of vowels


for v in text:      # for each character:
    if v.lower() in vowels or v.isspace():     # if it is a vowel:
        result = result     # do not keep it  # noqa: PLW0127

    else:       # otherwise
        result = result + v      # add it to the result

print(f"Compressed: {result}")        # print the completed result