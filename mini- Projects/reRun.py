# Step 1: Define the Item class
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity})"

# Step 2: Define the Inventory class
class Inventory:
    def __init__(self):
        self.items = []

    # Add item to inventory
    def add_item(self, name, quantity):
        try:
            quantity = int(quantity)
            self.items.append(Item(name, quantity))
            print(f"Added {quantity} of {name} to the inventory.")
        except ValueError:
            print("Error: Quantity must be a number.")

    # Remove item from inventory
    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed {name} from the inventory.")
                return
        print(f"Error: {name} not found in inventory.")  # Error handling

    # View all items in the inventory
    def view_inventory(self):
        if self.items:
            print("Current Inventory:")
            for item in self.items:
                print(item)
        else:
            print("Inventory is empty.")

    # Save the inventory to a file
    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for item in self.items:
                    file.write(f"{item.name},{item.quantity}\n")
            print(f"Inventory saved to {filename}.")
        except Exception as e:
            print(f"Error saving to file: {e}")  # Error handling

    # Load the inventory from a file
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.items = []
                for line in file:
                    name, quantity = line.strip().split(",")
                    self.add_item(name, quantity)
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading from file: {e}")  # Error handling

# Step 3: Main Program
def main():
    inventory = Inventory()

    # Load inventory from file at the start
    inventory.load_from_file("inventory.txt")

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View inventory")
        print("4. Save inventory")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the item name: ")
            quantity = input("Enter the quantity: ")
            inventory.add_item(name, quantity)

        elif choice == "2":
            name = input("Enter the name of the item to remove: ")
            inventory.remove_item(name)

        elif choice == "3":
            inventory.view_inventory()

        elif choice == "4":
            inventory.save_to_file("inventory.txt")

        elif choice == "5":
            inventory.save_to_file("inventory.txt")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
