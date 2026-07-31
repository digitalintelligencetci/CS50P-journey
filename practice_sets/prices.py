

groceries = input("Product: ").lower()

products = {                           # lowercase fruit keys and calories values
    "apple": 1.30,
    "avocado": 2.50,
    "banana": 1.00,
    "cantaloupe": 3.50,
    "grapefruit": 1.60,
    "grapes": 1.90,
    "honeydew melon": 1.50,
    "kiwifruit": 1.90,
}


if groceries in products:
    print(f"Price: {products[groceries]:.2f}")
