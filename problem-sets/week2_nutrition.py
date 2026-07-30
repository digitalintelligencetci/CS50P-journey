# Create a dictionary containing fruits and their calories

# Ask the user for a fruit
# Convert the input to lowercase

# If the fruit exists in the dictionary:
#    print its calorie value

# Otherwise:
#    print nothing


fruit = input("Item: ").lower()

d = {                           # lowercase fruit keys and calories values
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

if fruit in d:
    print(f"Calories: {d[fruit]}")