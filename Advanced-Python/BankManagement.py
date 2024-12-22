# Bank360 Management System

from BankingSystem import AccountUser

# Admin and employee data
admin_accounts = [{
    "employee_id": "ADMIN",
    "name": "Elon Musk",
    "role": "Administrator",
    "email": "stark.link@bank360.com",
    "contact_number": "234-567-8901",
}]

employees = [
    {
        "employee_id": "EMP001",
        "name": "Alice Johnson",
        "role": "Teller",
        "email": "alice.johnson@bank360.com",
        "contact_number": "123-456-7890",
    },
    {
        "employee_id": "EMP002",
        "name": "Bob Smith",
        "role": "Manager",
        "email": "bob.smith@bank360.com",
        "contact_number": "234-567-8901",
    },
    {
        "employee_id": "EMP003",
        "name": "Charlie Davis",
        "role": "Customer Support",
        "email": "charlie.davis@bank360.com",
        "contact_number": "345-678-9012",
    },
    {
        "employee_id": "EMP004",
        "name": "Diana Perez",
        "role": "Fraud Analyst",
        "email": "diana.perez@bank360.com",
        "contact_number": "456-789-0123",
    },
    {
        "employee_id": "EMP005",
        "name": "Ethan Brown",
        "role": "Currency Specialist",
        "email": "ethan.brown@bank360.com",
        "contact_number": "567-890-1234",
    },
    {
        "employee_id": "EMP006",
        "name": "John Francis Saro",
        "role": "Administrator",
        "email": "John.Testing@bank360.com",
        "contact_number": "567-777-9899",
    },
]

# Function to display all customer accounts
def display_all_accounts(employee):
    print("==========================================")
    print("        All Customer Accounts 📋          ")
    print("==========================================")
    print("Account Number      Name                Balance    Account Type")
    print("------------------------------------------------------------")
    
    for user in AccountUser:
        print(f"{user['account_number']}    {user['name']}    💲{user['balance']:.2f}    {user['account_type']} 💳")
    
    input("\n🔙 Press any key to return to the previous menu.")

# Function to search for an account by account number
def search_account_number(employee):
    attempt = 0
    max_attempt = 3
    print("==========================================")
    print("        Search by Account Number 🔍          ")
    print("==========================================\n\n")
    
    while True:
        try:
            account_num = int(input("Account number: "))
            attempt += 1
        except ValueError:
            print("Enter a number only")
            continue
        
        if attempt >= max_attempt:
            print("Try again next time !")
            break
        
        # Check if the account number is 12 digits
        if len(str(account_num)) != 12:
            print("Account number must be 12 digits. Please try again...\n")
            continue
        
        user_found = False
        for user in AccountUser:
            if account_num == user['account_number']:
                print("🔎 Searching... ")
                print("------------------------------------------")
                print("Account Found!")
                print(f"Account Number: {user['account_number']}")
                print(f"Name: {user['name']}")
                print(f"Balance: 💲{user['balance']}")
                print(f"Account Type: {user['account_type']}")
                user_found = True
                break
        
        if user_found:
            break
        else:
            print("⚠️ Account Number not found. Please try again.\n\n")
    
    input("\n🔙 Press any key to return to the previous menu.")

# Function to search for an account by customer name
def search_customer_name(employee):
    print("==========================================")
    print("        Search by Customer Name 🔍          ")
    print("==========================================\n\n")
    
    while True:
        customer_name = input("Enter Customer Name: ").strip().lower()
        
        # Ensure the name is at least 6 characters
        if len(customer_name) < 6:
            print("Subscriber Name must be 6 characters or above. Please try again...\n")
            continue
        
        # Filter the accounts where the name matches (case-insensitive)
        matches = [user for user in AccountUser if user["name"].lower() == customer_name]
        
        if matches:
            print("🔎 Searching... ")
            print("------------------------------------------")
            print("Matching Accounts: ")    
            for i, match in enumerate(matches, start=1):
                print(f"{i}. Account Number: {match['account_number']} | Name: {match['name']} | Balance: ${match['balance']:.2f} | Account Type: {match['account_type']}")
        else:
            print("🔎 Searching... ")
            print("------------------------------------------")
            print("⚠️ No accounts found for the name provided. Please try again.")
        
        input("\n🔙 Press any key to return to the previous menu.")
        break

# Function to display the accounts menu
def Accounts_menu(employee):
    print("==========================================")
    print("     View Customer Accounts 📋     ")
    print("==========================================")
    
    while True:
        print("🔍 Search Options: ")
        print("1️⃣  View All Customer Accounts")
        print("2️⃣  Search by Account Number")
        print("3️⃣  Search by Customer Name ")
        print("4️⃣  Back to Dashboard")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                display_all_accounts(employee)
            elif choice == 2:
                search_account_number(employee)
            elif choice == 3:
                search_customer_name(employee)
            elif choice == 4:
                print("🔙 Returning to the Dashboard...  \n")
                dashboard(employee)
                return
            else:
                print("❌ Invalid choice, please try again.")
        except ValueError:
            print("Invalid pls enter a number")

# Function to display the admin view
def admin_view(admin):
    if employees:
        for employee in employees:
            print("Name    |     Employee ID")
            print(f"{employee['name']}    |    {employee['employee_id']}")
        return
    print("Employee Database is Empty")

# Function to display the employee dashboard
def dashboard(employee):
    while True:
        print("==========================================")
        print("     Bank360 Employee Dashboard    ")
        print("==========================================\n")
        
        print(f"👋 Welcome, {employee['name']}! ")
        print(f"Role: {employee['role']}")
        print(f"Employee ID: [{employee['employee_id']}] ")
        print("------------------------------------------\n\n")
        
        print("🌟 **Dashboard Menu** ")
        print("1️⃣  View Customer Accounts 📋")
        print("2️⃣  Manage Transactions 💳 ")
        print("3️⃣  Monitor Fraud Alerts 🚨 ")
        print("4️⃣  Customer Support Tickets 📨")
        print("5️⃣  Currency Exchange Reports 💱")
        print("6️⃣  Savings Goal Tracker Updates 🏦 ")
        print("7️⃣  Logout 🚪 \n\n")
        
        print("------------------------------------------")
        print("📌 Notifications: ")
        print("- [0] pending support tickets.")
        print("- [0] flagged fraud transactions.")
        print("\n⚙️ System Status: ✅ Operational ")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Accounts_menu(employee)
            elif choice == 2:
                print("Manage Transactions 💳 coming soon...")
            elif choice == 3:
                print("Monitor Fraud Alerts 🚨 coming soon...")
            elif choice == 4:
                print("Customer Support Tickets 📨 coming soon...")
            elif choice == 5:
                print("Currency Exchange Reports 💱")
            elif choice == 6:
                print("Savings Goal Tracker Updates 🏦")
            elif choice == 7:
                confirm = input("Are you sure you want to Log-out? Yes/No: ").lower()
                if confirm == "yes":
                    print("🔒 Logging out... Goodbye!")
                    login()
                elif confirm == "no":
                    return
                else:
                    print("❌ Invalid choice, Type only YES or NO!")
            else:
                print("❌ Invalid choice, please try again.")
        except ValueError:
            print("Invalid pls enter a number")

# Function to display the admin dashboard
def admin_login(admin):
    while True:
        print("==========================================")
        print("     Bank360 Admin Dashboard    ")
        print("==========================================\n")
        
        print(f"👋 Welcome, ADMIN {admin['name']}! ")
        print(f"Role: {admin['role']}")
        print(f"Employee ID: [{admin['employee_id']}] ")
        print("------------------------------------------\n\n")
        
        print("🌟 **Dashboard Menu**  ")
        print("1️⃣ **Manage Accounts** → View / Add / Edit Customer Accounts ")
        print("2️⃣ **Employee Management** → Add / View / Remove Employees")
        print("3️⃣ **Reports & Analytics** → View Transaction Reports, System Logs")
        print("4️⃣ **Fraud Alerts** → Investigate Suspicious Transactions")
        print("5️⃣ **Exit** 🚪")
        
        print("\n------------------------------------------")
        print('📌 Notifications: ')
        print("- [ 23 ] pending account modifications.")
        print("- [ 10 ] new fraud alerts.")
        
        print("\n⚙️ System Status: ✅ All systems operational. ")
        
        try:
            choice = int(input("Enter your choice (number): "))
            if choice == 1:
                admin_view(admin)
            elif choice == 2:
                print("coming soon...")
            elif choice == 3:
                print("coming soon...")
            elif choice == 4:
                print("coming soon...")
            elif choice == 5:
                confirm = input("Are you sure you want to Log-out? Yes/No: ").lower()
                if confirm == "yes":
                    print("🔒 Logging out... Goodbye!")
                    return
                else:
                    print("❌ Invalid choice, Type only YES or NO!")
            else:
                print("❌ Invalid choice, please try again.")
        except ValueError:
            print("Choice must be a number!")

# Function to handle login
def login():
    personel = input("Enter your Employee ID: ")
    
    for admin in admin_accounts:
        if personel == admin['employee_id']:
            admin_login(admin)
            return
    
    for employee in employees:
        if personel == employee['employee_id']:
            dashboard(employee)
            return
    
    print("No Employee with that ID!")
    return

# Main function to start the program
def main():
    print("Welcome to Bank360 Management System")

    while True:
        print("🌟 **Menu:**  ")
        print("1️⃣  Login 🔑")
        print("2️⃣  Exit 🚪")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                login()
            elif choice == 2:
                print("Thanks for using our Bank!... Goodbye!")
                break
            else:
                print("❌ Invalid choice, please try again.")
        except ValueError:
            print("Invalid pls enter a number")

if __name__ == "__main__":
    main()
