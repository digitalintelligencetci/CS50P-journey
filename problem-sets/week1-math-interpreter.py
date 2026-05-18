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
