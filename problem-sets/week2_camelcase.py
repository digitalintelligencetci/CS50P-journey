
# name: whatever the user types / preferredFirstName
# snake_case: starts empty and gradually become preferred_first_name
# snake_case stores the new result. 
# character holds one letter at a time. 
# Uppercase letters are changed into an underscore plus lowercase. 
# Lowercase letters are copied as they are.

name = input("camelCase: ")
snake_case = ""


for character in name:
    if character.isupper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character


print(snake_case)