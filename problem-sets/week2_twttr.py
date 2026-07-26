# Ask the user for some text

# Create somewhere to store the result

# Look at each character in the text:
#    If the character is not a vowel:
#        Add it to the result

#   Print the result


text = input("Input: ")
output = ""

for v in text:
    vowels = ["a", "e", "i", "o", "u"]
    if v.lower() not in vowels:
        output = output + v

print(f"Output: {output}")

