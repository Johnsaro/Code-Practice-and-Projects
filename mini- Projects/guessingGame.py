import random
# Create a dictionary that maps prices to items
price_items = {
    1000: "Iphone",
    40: "wallet",
    70: "bag",
    200: "Gamepad",
    800: "PC",
    230: "mouse",
    600: "keyboard",
    120: "Tumblr",
    50: "Sunglass"
}

points = 100

def get_price():
    # Example: Check if you can afford an item for 40 points
    if points in price_items:
        print(f"You can afford: {price_items[points]}")
    else:
        print("No items available at this price.")
        
        
def main():
    correct_number = random.randint(1, 100)
    attempts = 0
    max_attempt = 5
    global points 
    
    
    print("Welcome to Guessing Game!")
    print("Try to Guess the random number and win prices\n")
    
    
    while True:
        try:
            print(f"Guess a number from 1 to 100 (Attempt {attempts + 1}/{max_attempt}):")
            guess = int(input("Your Guess: "))
            attempts += 1
            
            
            #  # Cheat code logic
            # if guess == 999:  # Reveal correct number
            #     print(f"Cheat activated! The correct number is: {correct_number}")
            #     continue
            # elif guess == 111:  # Add 2 extra attempts, respecting max_attempt limit
            #     if max_attempt - attempts > 2:
            #         max_attempt += 2  # Increase max_attempt by 2
            #         print(f"Cheat activated! You have {max_attempt - attempts} attempts left.")
            #     else:
            #         print(f"Cheat activated, but you have no extra attempts available.")
            #     continue
            
            
            if guess == correct_number:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                print(f"You guess the number after {attempts} attempts\n ")
                win = input(f"You win ${points}  claim it now!(y/n): \n")
                if win == "y":
                    get_price()
                elif win == "n":
                    print("Thanks for playing!")
                    break
                else:
                    continue   
            elif guess < correct_number:
                print("Your guess is to Low!")
            else:
                print("Your Guess is Too High!")
        except ValueError:
            print("Enter a number Only!")   
            
        # Check if max attempts are reached
        if attempts >= max_attempt:
            print("You've reached the maximum number of attempts.")
            print(f"The correct number was {correct_number}. Better luck next time!")
            break
        
        
   
        
if __name__ == "__main__":
    main()