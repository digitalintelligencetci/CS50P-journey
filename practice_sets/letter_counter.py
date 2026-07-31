# Get some text
# Start the count at zero
# Examine every character
# If the character is a letter:
#   increase the count
# Print the final count


text = input("Text: ")          # get some text
counter = 0

for char in text:               # examine every character
    if char.isalpha():          # if the character is a letter
        counter +=1             # increase the count


print(f"Letters: {counter}")