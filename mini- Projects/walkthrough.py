class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        
        
    def __str__(self):
        return f"{self.name} - {self.quantity}"
    

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, name, quantity):
        try:
            # Check if item name is already Exist
            for item in self.items:
                if item.name == name.lower():
                    print(f"item {name} is already exists")
                    return
            # If item doesn't exist, add it
            quantity = int(quantity)
            self.items.append(Item(name, quantity))
            print(f"Added {quantity} of {name} to the inventory.")
        except ValueError:
            print("Error: Quantity must be a number.")
            
    def remove_item(self, name):
        for item in self.items:
            if item.name == name.lower():
                self.items.remove(item)
                print(f"Removed {name} from the inventory.")
                return
        print(f"Error: {name} not found in inventory.")  # Error handling
  
  
    def view_inventory(self):
        if self.items:
            print("[Inventory]")
            for item in self.items:
                print(f"{item}")
        else:
            print("[Inventory]\n  Empty")
   
   
    def save_inventory_file(self, filename):
        try:
            with open(filename, "w") as file:
                for item in self.items:
                    file.write(f"{item.name} - {item.quantity}")
            print(f"Inventory saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")
            
            
    def load_inventory_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.items = []
                for line in file:
                    name, quantity = line.strip().split(",")
                    self.add_item(name, quantity)
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with empty inventory.")
        except Exception as e:
            print(f"Error loading from file: {e}")    
            
                  
def main():
    inventory = Inventory()
    
    inventory.load_inventory_file("Storage.txt")          
            

    while True:
        print("Menu:\n")
        print("[1] Add Item")
        print("[2] Remove Item")
        print("[3] View Inventory")
        print("[4] Saved Inventory")
        print("[5] Exit")


        try:
            choice = int(input("Enter (1-5): "))
            
            if choice == 1:
                name = input("Enter the item name: ")
                quantity = input("Enter the quantity: ")
                inventory.add_item(name, quantity)
                
            elif choice == 2:
                name = input("Enter the name of the item to remove: ")
                inventory.remove_item(name)

            elif choice == 3:
                inventory.view_inventory()

            elif choice == 4:
                inventory.save_inventory_file("Storage.txt")

            elif choice == 5:
                inventory.save_inventory_file("Storage.txt")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
                print("Enter A number only ")




if __name__ == "__main__":
    main()
         
# # for test cases
# def test_inventory():
#     inventory = Inventory()
    
    
#     # inventory.add_item("sword", "2")
#     # inventory.add_item("sword", "22")
#     # inventory.add_item("dagger", "2")
#     # inventory.remove_item("DAGGER")
#     inventory.view_inventory()
    
# test_inventory()