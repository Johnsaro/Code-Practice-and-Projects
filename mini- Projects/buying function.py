marketplace_items = [
    # Common Items
    {
        "item_name": "Iron Sword",
        "item_type": "weapon",
        "rarity": "common",
        "price": 50,
        "attack": 10,
        "upgrade_level": 0
    },
    {
        "item_name": "Wooden Shield",
        "item_type": "armor",
        "rarity": "common",
        "price": 40,
        "defense": 8,
        "upgrade_level": 0
    },
    {
        "item_name": "Health Potion",
        "item_type": "potion",
        "rarity": "common",
        "price": 15,
        "effect": "heal 50 HP"
    },
    {
        "item_name": "Mana Potion",
        "item_type": "potion",
        "rarity": "common",
        "price": 20,
        "effect": "restore 30 MP"
    },
    # Rare Items
    {
        "item_name": "Steel Axe",
        "item_type": "weapon",
        "rarity": "rare",
        "price": 150,
        "attack": 20,
        "upgrade_level": 0
    },
    {
        "item_name": "Chainmail Armor",
        "item_type": "armor",
        "rarity": "rare",
        "price": 120,
        "defense": 15,
        "upgrade_level": 0
    },
    {
        "item_name": "Elixir of Strength",
        "item_type": "potion",
        "rarity": "rare",
        "price": 100,
        "effect": "+10 attack for 30 mins"
    },
    # Epic Items
    {
        "item_name": "Flame Sword",
        "item_type": "weapon",
        "rarity": "epic",
        "price": 300,
        "attack": 40,
        "upgrade_level": 0,
        "element": "fire"
    },
    {
        "item_name": "Dragon Scale Shield",
        "item_type": "armor",
        "rarity": "epic",
        "price": 350,
        "defense": 35,
        "upgrade_level": 0,
        "special_ability": "resist fire"
    },
    {
        "item_name": "Potion of Invincibility",
        "item_type": "potion",
        "rarity": "epic",
        "price": 250,
        "effect": "invincible for 10 seconds"
    },
    # Legendary Items
    {
        "item_name": "Excalibur",
        "item_type": "weapon",
        "rarity": "legendary",
        "price": 1000,
        "attack": 100,
        "upgrade_level": 0,
        "special_ability": "holy damage"
    },
    {
        "item_name": "Armor of the Gods",
        "item_type": "armor",
        "rarity": "legendary",
        "price": 900,
        "defense": 80,
        "upgrade_level": 0,
        "special_ability": "resist all elements"
    },
    {
        "item_name": "Elixir of Eternal Life",
        "item_type": "potion",
        "rarity": "legendary",
        "price": 500,
        "effect": "restore full HP and MP"
    },
    # Crafting Materials
    {
        "item_name": "Iron Ore",
        "item_type": "material",
        "rarity": "common",
        "price": 10,
        "use": "crafting basic weapons"
    },
    {
        "item_name": "Dragon Scale",
        "item_type": "material",
        "rarity": "epic",
        "price": 200,
        "use": "crafting epic armor"
    },
    {
        "item_name": "Magic Crystal",
        "item_type": "material",
        "rarity": "rare",
        "price": 150,
        "use": "enchanting weapons"
    }
]


# function to check json marketplace if exist or not
# fucntion to add item in json marketplace
# function to buy item in marketplace
# function to give user a reciept
# main menu for user intraction such as buy, check item,exit
def open_market():
    # Display available items in the marketplace
    print("[Shop]\n")
    for item in marketplace_items:
        print("Name: ", item["item_name"])
        print("Rarity:", item["rarity"])
        print("Price: ", item["price"])

    # Ask the user if they want to buy an item
    choice = input("\nWant to buy? (y/n): ").lower()

    if choice == "y":
        print("Buying...")
        try:
            # Get the item name the user wants to buy
            buy_item = input("Enter item name: ").lower()
            
            # Search for the item in the marketplace
            for item in marketplace_items:
                if buy_item == item["item_name"].lower():  # Compare item names in lowercase
                    amount = int(input("Enter amount of gold: "))
                    
                    # Check if the user has enough gold
                    if amount == item["price"]:
                        print(f"Name: {item['item_name']} is sold!")
                    elif amount < item["price"]:
                        print("Not enough Gold!")
                    else:
                        print("You entered more than the price, please enter the correct amount.")
                    break
            else:
                # If the loop completes without finding the item
                print("Item not found.")
        except ValueError:
            print("Please enter the correct amount in numbers.")
    elif choice == "n":
        print("Okay, come back anytime!")
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        




def main():
    while True:
        print("[1] Open market")
        print("[2] trade") 
        print("[3] Exit")
        
        try:
            choice = int(input("1-3: "))
            
            if choice == 1:
                open_market()
            elif choice == 2:
                print("coming soon...")
            elif choice == 3:
                print("exit")
                break
            else:
                print("1-3 only")
        except ValueError:
            print("Enter a number from 1 to 3!")
if __name__ == "__main__":
    main()       