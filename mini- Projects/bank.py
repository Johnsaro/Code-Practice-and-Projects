

#functions

def login_account():
    username = input("Username: ")
    password = input("Password: ")

    try:
        with open("BDO_Accounts.txt", "r") as file:
            # Read through each line in the file to find the username and password
            lines = file.readlines()
            stored_username = None
            stored_password = None

            for line in lines:
                if line.startswith("Username: "):
                    stored_username = line.split("Username: ")[1].strip()
                elif line.startswith("Password: "):
                    stored_password = line.split("Password: ")[1].strip()

            # Now check if the entered credentials match
            if stored_username == username and stored_password == password:
                print("Login successful! Welcome!")
            else:
                print("Invalid username or password. Try again.")
    except FileNotFoundError:
        print("No accounts found. Please create an account first.")


def create_account():
    with open("BDO_Accounts.txt", "w") as file:
        name = input("Pls Enter A name: ")
        ask_username = input("Pls Enter a username: ")
        ask_password = input("PLs Enter a password: ")

        file.write(f"Name: {name}\n")
        file.write(f"Username: {ask_username}\n")
        file.write(f"Password: {ask_password}\n")

    print("Bank Account is Successfully saved!")


# main menu logic
def main():

    while True:
        print("\n WELCOME TO BDO BANK...\n")
        print("[1] Login")
        print("[2] Create Account")
        print('[3] Reset Account')
        print("[4] Exit")

        try:
            ask_user = int(input("Choose from 1-4: "))
            
            if ask_user == 1:
                login_account()
            elif ask_user == 2:
                create_account()
            elif ask_user == 3:
                print("Reset Account feature not implemented yet.")
            elif ask_user == 4:
                print("Exit program...")
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

