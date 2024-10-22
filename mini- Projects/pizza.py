pizza_menu = [
    {'name': 'Pepperoni Pizza', 'ingredients': ['pepperoni', 'cheese', 'tomato sauce'], 'price': 8.99},
    {'name': 'Veggie Pizza', 'ingredients': ['bell peppers', 'onions', 'mushrooms', 'cheese'], 'price': 7.99},
    {'name': 'BBQ Chicken Pizza', 'ingredients': ['chicken', 'bbq sauce', 'cheese'], 'price': 9.99}
]


def show_menu():
    print("[Menu]\n")
    
    for pizza in pizza_menu:
        print("name: ", pizza["name"])
        print("for as low as: ", pizza["price"])
        print("________________")
    
        

    
  



def order_now():
    order = input("what do you like to order?: ").lower()
    
    
    for pizza in pizza_menu:
        if order == pizza["name"].lower():
            try:
                quantity = int(input("How many?: ")) # ask how many pizza 
                
                
                total = pizza["price"] * quantity  # total calculation
                # buy= input(f"You order {quantity}x ", pizza["name"], "that would be ${total} do you want to pay now or later? y/n:  ").lower()
                buy = input(f"You ordered {quantity}x {pizza['name']} for a total of ${total}. Do you want to pay now? (y/n): ").lower()
                
                
                if buy == "y":
                    try:
                        print(f"total: ${total}")
                        amount = float(input("Pls enter the exact amount:"))
                        
                        if amount == total:
                            print("purchase successfull Thanks for ordering ....")
                        elif amount < total:
                            print("Not enough money. Please come back later.")
                        else:
                            print(f"You gave too much! Here's your change: ${amount - total:.2f}")
                    except ValueError:
                        print("Please enter a valid amount.")
                else:
                    print("Order canceled. Returning to main menu.")
                    return  
            except ValueError:
                print("Invalid input for quantity. Please enter a number.")  
            return  
                 
    # if the user input is not in pizza
    print("Sorry, that pizza is not on the menu.")
            
                   
        
        
        
        
def main():
    while True:
        print("1. Menu")
        print("2. order")
        
        
        try:
            choice = int(input("Want to check the menu or order now? (1 or 2): "))
            
            if choice == 1:
                print("Here's the menu!")
                show_menu()
            elif choice == 2:
                print("Ordering now...")
                order_now()
            else:
                print("Please come back!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    main()  