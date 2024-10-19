player_info = {
    "name": "GameMater",
    "level": 12,
    "skills": 4,
    "inventory": ["sword", "potion", "0G"],
    "Authority": True,
    "username": "Admin",
    "password": "1--1"
}

def login_user():
    while True:
        print("Enter username & password!")

        username = input("username: ")
        password = input("password: ")
        
        
        if username == player_info.get("username") and password == player_info.get("password"):
            print("Login Successful")
            view = input("check status: ").lower()
            if view == "yes":
                
                updated_info = {
                    "name": player_info["name"],      # Using values from the existing player_info
                    "level": player_info["level"],
                    "skills": player_info["skills"],
                    "inventory": player_info["inventory"],
                    "friends": 12,                    # New value for this login session
                    "isActive": True                  # Another new value
                }
                print("Player Status:")
                print(updated_info)
            else:
                return
        else:
            print("Account not found pls try again or signup account") 
            break
        
def signup():
    global player_info  # To allow modifying the global player_info variable
    
    print("Sign up for a new account!")
    
    # Check if username exists
    while True:
        new_username = input("Enter a username: ")
        if new_username == player_info.get("username"):
            print("Username already exists. Try a different one.")
        else:
            break

    new_password = input("Enter a password: ")
    
    # Collect new user information
    name = input("Enter your name: ")
    level = 1  # Default starting level
    skills = 1  # Default skills
    inventory = ["starter sword"]  # Default inventory
    
    # Create new player info
    player_info = {
        "name": name,
        "level": level,
        "skills": skills,
        "inventory": inventory,
        "Authority": False,
        "username": new_username,
        "password": new_password
    }
    
    print(f"Signup complete! Welcome, {name}.")
   
    
    
    
                  
        
        
while True:
    
    print("[1] Login")
    print("[2] signup")
    print("Exit")
    
    try:
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("Loading ....")
            login_user()
        elif choice == 2:
            signup()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("okay try again")
            break
    except ValueError:
        print("Invalid input")