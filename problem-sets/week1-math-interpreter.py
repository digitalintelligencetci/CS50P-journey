# Pseudo Code
# 1. Get input → split into x, y, z
# 2. Convert x and z to integers
# 3. if y is + → add
# 4. elif y is - → subtract
# 5. elif y is * → multiply
# 6. elif y is / → divide
# 7. Print result as float to 1 decimal place

#!/usr/bin/env python3


# Step 1 — get input and split immediately
expression = input("Expression: ").split()

# Step 2 — assign each part
x = int(expression[0])    # first number
y = expression[1]         # operator
z = int(expression[2])    # second number

# Step 3 — calculate based on operator
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Step 4 — print to 1 decimal place
print(f"{result:.1f}")
