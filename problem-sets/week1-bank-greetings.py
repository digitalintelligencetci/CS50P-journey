
#!/usr/bin/env python3

user_greeting = input("Welcome, what is your name? ").lower().strip()

if user_greeting.startswith('hello'):
    print('$0')
elif user_greeting.startswith('h'):
    print('$20')
else:
    print("$100")
