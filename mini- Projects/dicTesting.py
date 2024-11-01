# player_info is a list of dictionarys
player_info = [
{ # GM ACCOUNT
    "name": "GameMater",
    "level": 12,
    "skills": 4,
    "inventory": ["sword", "potion", "0G"],
    "Authority": True,
    "username": "Admin",
    "password": "1--1",
    "isActive": False
},
{
        "name": "ShadowFury",
        "level": 5,
        "skills": 2,
        "inventory": ["dagger", "shield", "25G"],
        "Authority": False,
        "username": "ShadowFury_91",
        "password": "xf12&vsl",
        "isActive": True
    },
    {
        "name": "MageMist",
        "level": 8,
        "skills": 3,
        "inventory": ["staff", "mana potion", "50G"],
        "Authority": False,
        "username": "MistMage101",
        "password": "ManaBlast8",
        "isActive": False
    },
    {
        "name": "IronClad",
        "level": 10,
        "skills": 4,
        "inventory": ["great sword", "armor", "100G"],
        "Authority": False,
        "username": "IronCladKing",
        "password": "SteelW12#",
        "isActive": True
    },
    {
        "name": "WindDancer",
        "level": 6,
        "skills": 2,
        "inventory": ["bow", "arrows", "35G"],
        "Authority": False,
        "username": "Wind_Dancer",
        "password": "ArrowPath78",
        "isActive": True
    },
    {
        "name": "LunarMage",
        "level": 9,
        "skills": 3,
        "inventory": ["magic staff", "elixir", "75G"],
        "Authority": False,
        "username": "LunarMageX",
        "password": "Moonlight@3",
        "isActive": True
    }
]


def login_user():
    while True:
        print("Enter username & password!")

        username = input("username: ")
        password = input("password: ")
        
        # for user in player_info: # I add this to get rid of the error code 
            
                
        for player in player_info:  # Iterate through each player dictionary in the list
            
            if username == player.get("username") and password == player.get("password"):
                print("Login Successful")

                view = input("check status: ").lower()
                if view == "yes":
                    updated_info = {
                        "name": player["name"],      # Using values from the existing player
                        "level": player["level"],
                        "skills": player["skills"],
                        "inventory": player["inventory"],
                        "friends": 12,               # New value for this login session
                        "isActive": True             # Another new value
                    }
                    print("Player Status:")
                    print(updated_info)
                    break  # Exit the loop after a successful login
        else:
            print("Account not found. Please try again or sign up for an account.")
        
def signup():
    global player_info  # To allow modifying the global player_info variable
    
    print("Sign up for a new account!")
    
    # Check if username exists
    while True:
        new_username = input("Enter a username: ")
        
        for player in player_info:
            if new_username == player.get("username"):
                print("Username already exists. Try a different one.")
                break
        else:
            print("Username is available.")

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
        return
   
 
def secret_login():
    print("GameMaster is login\n")  
     
    while True:
        print("[1] check All user status")
        print("[2] Ban User")
        print("[3] Back to main menu")  
         
        try:
            admin = int(input("> ")) 
            
            if admin == 1:
                print("Checking all user statuses... \n")
                # Assuming player_info is a list of dictionaries containing player data
                for player in player_info:
                    print("- Name:", player["name"])
                    print("- Level:", player["level"])
                    print("- Is Active:", "Online\n" if player["isActive"] else "Offline\n")
                    
                
            elif admin == 2:
                confirmation = input("Are you sure you want to ban a user? (yes/no): ").lower()
                if confirmation == "yes":
                    print("Ban functionality coming soon..")
                    for index in range(len(player_info)): #  print the indices of the players in player_info , using the range() function along with len()
                        print(f"ID: {index}, Player Name: {player_info[index]['name']}")
                        
                    unique_ID = int(input("Enter player ID: "))  # Convert to int to match the index type
        
                    # Check if ID is found in player_info
                    if 0 <= unique_ID < len(player_info):  # Check if the input ID is within range
                        player_name = player_info[unique_ID]["name"]
                        player_info.pop(unique_ID)  # Remove the player from the list
                        print(f"{player_name} has been banned for 3 months...")
                    else:
                        print("Invalid ID. Please try again.")
                        
                        
            elif admin == 3:
                main()
                break
            else:
                print("1-3 only")
        except ValueError:
            print("try again admin")
                  
        
def main():    
    while True:
        
        print("[1] Login")
        print("[2] Signup")
        print("[3] Exit")
        
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
            elif choice == 4:    
                secret_login()
            else:
                print("okay try again")
        except ValueError:
            print("Invalid input")
            

if __name__ == "__main__":
    main()