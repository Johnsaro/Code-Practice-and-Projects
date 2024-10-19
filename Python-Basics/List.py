
inventory = []
modified = False



def view_inventory():
    if inventory:
        print("[Inventory]")
        for item in inventory: 
            print(f"- {item.capitalize()}")
    else:
        print("Inventory is Empty\n\n")

def add_item():
    global modified
    item = input("Enter the item name to add: ").strip().lower()
    if item:
        if item not in inventory:
            inventory.append(item)
            modified = True
            print(f"{item.capitalize()} is added!\n")
        else:
            print(f"{item.capitalize()} is already in your inventory.\n")
    else:
        print("Cannot add an empty item.\n")

def remove_item():
    item_info = input("Enter item to remove: ").strip().lower()

    if inventory:
        if item_info in inventory:
            inventory.remove(item_info)
            print(f"{item_info.capitalize()} - is removed")
        else: 
            print(f"{item_info.capitalize()} - not found in inventory")
    else:
        print("Inventory is Empty\n\n")    

def find_item():
    find_item = input("Enter item to search: ").strip().lower()

    if find_item in inventory:
        print(f"{find_item.capitalize()} is in your inventory.")
    else:
        print(f"{find_item.capitalize()} not found")

def save_inventory():
    with open("Inventory.txt", "w") as f:
        for item in inventory:
            f.write(item +"\n")

def load_inventory():
    try:
        with open("Inventory.txt", "r") as f:
            inventory.clear()
            for line in f:
                inventory.append(line.strip())
        
        if inventory:
            print("Inventory is loaded successfully!\n")
        else:
            print("No saved inventory found. You may need to add items and save them first.\n")
    except FileNotFoundError:
        print("No saved inventory found.")

def end_program():
    confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
    if confirm == "y":
        if modified:
            save_inventory()
            print("Inventory is saved...")
        print("Logging out...\nLog Out Successfully...\n")
        return True
    return False
    
def main():
    while True:
        print("\nWelcome to the RPG Inventory Manager!\n")
        print("What would you like to do?")
        print("[1] View Inventory")
        print("[2] Add Item")
        print("[3] Remove Item")
        print("[4] Search for Item")
        print("[5] Exit")
        print("[6] Load Existing Inventory")


 
        try:
            ask_user = int(input("Choose an option (1-6):"))
            if ask_user == 1:
                view_inventory()
            elif ask_user == 2:
                add_item()
            elif ask_user == 3:
                remove_item()
            elif ask_user == 4:
                find_item()
            elif ask_user == 5:
                if end_program():
                    break
            elif ask_user == 6:
                load_inventory()
            else:
                print("Ooppsss !!!\n")
                print("Pls enter A number only from (1-5)")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
# v.1
