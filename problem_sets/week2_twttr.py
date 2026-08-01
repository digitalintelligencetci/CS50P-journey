# Ask the user for some text

# Create somewhere to store the result

# Look at each character in the text:
#    If the character is not a vowel:
#        Add it to the result

#   Print the result


text = input("Input: ")     # ask the user for some text
output = ""     #  create somewhere to store the result

for v in text:      # look at each character in the text
    vowels = ["a", "e", "i", "o", "u"]  # list of vowels
    if v.lower() not in vowels:     # if the character is not a vowel
        output = output + v     # add it to the result

print(f"Output: {output}")      # print the result