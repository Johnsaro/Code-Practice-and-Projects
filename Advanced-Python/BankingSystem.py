import random
from datetime import datetime

AccountUser = [
    {
    "name": "John Francis Saro",
    "account_number": 638772479329,
    "balance": 99999,
    "account_type": "Savings",
    "username": "test",
    "password": "test1",
    "transactions": []
    },
    {
    "name": "Imelda Labrador",
    "account_number": 638774776075,
    "balance": 2435,
    "account_type": "Savings",
    "username": "test1",
    "password": "test1",
    "transactions": []
    },
    {
        "name": "Alice Mercado",
        "account_number": 638775992003,
        "balance": 0,
        "account_type": "Savings",
        "username": "alice123",
        "password": "password123",
        "transactions": []
    },
    {
        "name": "Carlos Santos",
        "account_number": 638778491007,
        "balance": 0,
        "account_type": "Savings",
        "username": "carlos_s",
        "password": "pass456",
        "transactions": []
    },
    {
        "name": "Betty Cruz",
        "account_number": 638773491234,
        "balance": 0,
        "account_type": "Savings",
        "username": "betty_cruz",
        "password": "cruz789",
        "transactions": []
    },
    {
        "name": "David Tan",
        "account_number": 638771239875,
        "balance": 0,
        "account_type": "Savings",
        "username": "david_tan",
        "password": "tan4321",
        "transactions": []
    },
    {
        "name": "Ella Villanueva",
        "account_number": 638774900345,
        "balance": 0,
        "account_type": "Savings",
        "username": "ella_v",
        "password": "villa567",
        "transactions": []
    },
    {
    "name": "John Francis Saro",
    "account_number": 638772479329,
    "balance": 5789,
    "account_type": "Savings",
    "username": "johnsaro",
    "password": "johnsaro2422",
    "transactions": []
    }
]

def view_account(username):
    for user in AccountUser:
        if username == user['username']:
            print("__________________________")
            print(f"-------{user['account_number']}-------\n")
            print(f"Name: {user['name']}")
            print(f"Balance: ${user['balance']}")
            print("[1] Transaction")
            print("[2] Deposit")
            print("[3] Withdraw")
            print("[4] Send Money")
            print("[5] Exit")
            print("__________________________")
            print("__________________________")
        
    # Account Options
    choice = input("> ")
    
    if choice < "1" or choice > "5":
        print("Invalid input...please try again")
    else:
        if choice == "1":
            print("Transaction History: ")
            view_history(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            send_money_from(username)
        else:
            print("Logging out...")
            return

def withdraw(username):
    for user in AccountUser:
        if username == user["username"]:
            print(f"Balance: ${user['balance']} - Name: {user['name']}")
            try:
                withdraw_amount = int(input("Amount: "))
            except ValueError:
                print("Try Again! Invalid input. Please enter a number.")
                view_account(username)
                return
            
            if withdraw_amount < 100:
                print("Invalid amount. Please input 100 or above.")
                view_account(username)
                return
            if user['balance'] < withdraw_amount:
                print("Balance is not enough to withdraw")
                print(f"{withdraw_amount} - {user['balance']}")
                view_account(username)
                return
            
            current_date = datetime.now().strftime("%d-%b-%Y")
            user["balance"] -= withdraw_amount
            log_transaction(user, "Withdraw", withdraw_amount)
            print("==========================")
            print("        Random Bank       ")
            print("==========================")     
            print(f"Name: {user['name']}")
            print("Transaction Type      : Withdraw ")
            print(f"Account Name          :{user['name']}")
            print(f"Account Number        :{user['account_number']}")
            print(f"Withdraw Amount       :{withdraw_amount}")
            print(f"Updated Balance       :{user['balance']}")
            print(f"Transaction Date: {current_date}")
            print("==========================")
            print("     Thank you for banking with us!")
            view_account(username)
            return

def deposit(username):
    max_deposit = 1000000
    print("Max deposit is 1,000,000")
    try:
        deposit_amount = int(input("Amount: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if deposit_amount < 100:
        print("Invalid amount. Please input 100 or above.")
        return
    if deposit_amount > max_deposit:
        print("Transaction failed. Deposit amount has reached the limit per account!")
        view_account(username)
        return

    current_date = datetime.now().strftime("%d-%b-%Y")
    for user in AccountUser:
        if username == user["username"]:
            user["balance"] += deposit_amount
            log_transaction(user, "Deposit", deposit_amount)
            print("==========================")
            print("        Random Bank       ")
            print("==========================")     
            print(f"Name: {user['name']}")
            print("Transaction Type      : Deposit ")
            print(f"Account Name          :{user['name']}")
            print(f"Account Number        :{user['account_number']}")
            print(f"Deposit Amount        :{deposit_amount}")
            print(f"Updated Balance       :{user['balance']}")
            print(f"Transaction Date: {current_date}")
            print("==========================")
            print("     Thank you for banking with us!")
            view_account(username)
            return

def send_money_from(username):
    sender = None
    recipient = None

    for user in AccountUser:
        if username == user['username']:
            sender = user
            break

    if not sender:
        print("Sender account not found.")
        return

    try:
        recipient_account_number = int(input("Recipient's Account number: "))
    except ValueError:
        print("Invalid input. Please enter a valid account number.")
        print("Try again later...")
        view_account(username)
        return

    for user in AccountUser:
        if recipient_account_number == user['account_number']:
            recipient = user
            break

    if not recipient:
        print("Recipient account not found! Try again later....")
        view_account(username)
        return

    print(f"\nRecipient Found: {recipient['name']}")
    print(f"Account Number: {recipient['account_number']}")
    print("-------------------------------------------------")
    confirm = input("Do you confirm sending money to this recipient? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Transaction cancelled. Returning to the menu...")
        view_account(username)
        return

    try:
        amount_to_send = int(input("Amount to Send: "))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return

    if sender['balance'] < amount_to_send:
        print("Insufficient balance to complete the transaction.")
        print(f"{amount_to_send} - {sender['balance']}")
        return

    sender['balance'] -= amount_to_send
    recipient['balance'] += amount_to_send

    log_transaction(sender, "Send Money", amount_to_send)
    log_transaction(recipient, "Receive Money", amount_to_send)

    transaction_id = f"TXN-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d-%b-%Y")

    print("\n-------------------------------------------------")
    print("              SEND MONEY RECEIPT")
    print("-------------------------------------------------")
    print(f"Transaction ID: {transaction_id}")
    print(f"Date: {current_date}   Time: {current_time}")
    print("-------------------------------------------------")
    print("SENDER:")
    print(f"  Name         : {sender['name']}")
    print(f"  Account No.  : {sender['account_number']}")
    print(f"  Starting Bal : ${sender['balance'] + amount_to_send}")
    print("-------------------------------------------------")
    print("RECIPIENT:")
    print(f"  Name         : {recipient['name']}")
    print(f"  Account No.  : {recipient['account_number']}")
    print("-------------------------------------------------")
    print("TRANSACTION DETAILS:")
    print(f"  Amount Sent  : ${amount_to_send}")
    print(f"  Sender Bal   : ${sender['balance']}")
    print(f"  Recipient Bal: ${recipient['balance']}")
    print("-------------------------------------------------")
    print("Status: SUCCESSFUL")
    print("We appreciate your trust in Random Bank!")
    print("-------------------------------------------------\n")
    view_account(username)
    return

def log_transaction(user, transaction_type, amount):
    transaction_date = datetime.now().strftime("%d-%b-%Y")
    transaction = {
        "date": transaction_date,
        "type": transaction_type,
        "amount": amount,
        "balance_after": user["balance"]
    }
    user["transactions"].append(transaction)

def view_history(username):
    for user in AccountUser:
        if username == user['username']:
            print("--------------------------------------------------------")
            print("                        TRANSACTIONS                    ")
            print("--------------------------------------------------------")
            print("| Date         | Type          | Amount  | Balance     |")
            print("--------------------------------------------------------")
            if user['transactions']:
                for transaction in user['transactions']:
                    print(f"| {transaction['date']}  | {transaction['type']:<13} | ${transaction['amount']:<6} | ${transaction['balance_after']:<13} |")
            else:
                print("| No transactions found.                              |")
            print("-----------------------------------------------------")
            view_account(username)
            return

def login():
    print("\n=_=_=_= Random Bank =_=_=_=")
    print("=_=_=_==_LOGIN_==_=_=_=")
    username = input("Username: ")
    password = input("Password: ")
    
    for user in AccountUser:
        if username == user['username'] and password == user['password']:
            print("\n__________________________")
            print(f"welcome, {user['name']}!")
            view_account(username)
            return

    print("Wrong password or username!")
    return

def generate_account_number():
    prefix = "63877"
    while True:
        random_suffix = random.randint(100000, 999999)
        random_number = int(prefix + str(random_suffix))
        if not any(user['account_number'] == random_number for user in AccountUser):
            return random_number

def register_account():
    print("-------------------------------------------------")
    print("         Welcome to Random Bank Registration      ")
    print("-------------------------------------------------")
    print("Hi there! 🎉 Let’s create your account. It’s quick and easy!\n")
    print("\nOnce you’re done fillup, hit enter, and your account will be ready in seconds! 🚀")
    print("-------------------------------------------------")  
                    
    type_of = input("👉 Pick Account Type: [Savings] [Checking]: ").lower().strip().title()
    full_name = input("👉 What should we call you? (Full Name)       : ").strip()
    username = input("👉 Pick a cool username (Username) (3-6)          : ").strip()
    password = input("👉 Set a strong lock (Password) (6-12)            : ").strip()
    confirm_password = input("👉 Repeat it for safety (Confirm Password)   : ").strip()
    
    if len(username) < 3:
        print(f"{username} is invalid")
        print("The username must have more than 3 characters. Please try again.")
        return
    elif len(password) < 6:
        print(f"{password} - is not strong !")
        print("The password must have more than 6 characters. Please try again.")
        return
    
    if password != confirm_password:
        print("\nPasswords do not match! Please try again.")
        return
    
    for user in AccountUser:
        if username == user['username']:
            print(f"Username: {username} - is already Exist")
            print("Try Again!\n")
            return 
    
    try:
        initial_deposit = float(input("👉 How much cash to start with? (Min: $100)  : ").strip())
        if initial_deposit < 100:
            print("\nInitial deposit must be at least $100. Please try again.")
            return
        elif initial_deposit > 100000:
            print("\nInitial deposit exceeded the limit value. Please try again.")
            return
    except ValueError:
        print("\nInvalid amount entered. Please enter a numeric value.")
        return
    
    new_user_Account = {
        "name": full_name,
        "account_number": generate_account_number(),
        "balance": initial_deposit,
        "username": username,
        "password": password,
        "account_type": type_of,
        "transactions": []
    }
    
    AccountUser.append(new_user_Account)
    
    print("\nCongratulations! 🎉 Your account has been created successfully.")
    print(f"Your account number is: {new_user_Account['account_number']}")
    print("Thank you for choosing Random Bank!")
    print("-------------------------------------------------\n")

def main_menu():
    print("=_=_=[Random Bank]=_=_=")
    print("========================")
    while True:
        print("---------------")
        print("| [1] Login   |")
        print('| [2] Register|')
        print("| [3] Exit    |")
        print("---------------")
        
        try:
            choice = int(input("> "))
            if choice == 1:
                login()
            elif choice == 2:
                register_account()
            elif choice == 3:
                print("Thanks for using our Bank!...") 
                break
            else:
                print("Invalid choice try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    main_menu()