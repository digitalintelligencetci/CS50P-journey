# Pseudo Code:
# 1. Get input to .lower() = .strip()
# 2. if starts with "hello" = $0
# 3. elif starts with "h"   = $20
# 4. else                   = $100

#!/usr/bin/env python3

user_greeting = input("Greeting: ").lower().strip()

if user_greeting.startswith('hello'):
    print('$0')
elif user_greeting.startswith('h'):
    print('$20')
else:
    print("$100")
