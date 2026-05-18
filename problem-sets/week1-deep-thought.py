# Pseudo Code:
# 1. Get user input and convert to lowercase
# 2. If input is "42" or "forty-two" or "forty two", print Yes
# 3. Otherwise, print No


#!/usr/bin/env python3

user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower()

if user_input == "forty-two" or user_input == "forty two":
    print("yes")
elif user_input == "42":
    print("yes")
else:
    print("no")
