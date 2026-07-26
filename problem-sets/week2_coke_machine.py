# Set the amount due to 50
# While money is still due:
#   Show the amount due
#   Ask for a coin

# If the coin is accepted:
#   Subtract it from the amount due

# Show the change owed


coke = 50

while coke > 0:
    print(f"Amount Due: {coke}")
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in [25, 10, 5]:
        coke = coke - insert_coin

print(f"Changed Owed: {-coke}")