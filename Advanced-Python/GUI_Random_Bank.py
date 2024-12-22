import customtkinter as ctk
from tkinter import messagebox
import random
from datetime import datetime

# Initialize customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

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

class BankingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Random Bank")
        self.geometry("500x400")
        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Random Bank", font=("Arial", 24)).pack(pady=20)
        ctk.CTkButton(self, text="Login", command=self.login).pack(pady=10)
        ctk.CTkButton(self, text="Register", command=self.register_account).pack(pady=10)
        ctk.CTkButton(self, text="Exit", command=self.quit).pack(pady=10)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        self.clear_frame()
        ctk.CTkLabel(self, text="Login", font=("Arial", 24)).pack(pady=20)
        username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        username_entry.pack(pady=10)
        password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        password_entry.pack(pady=10)
        ctk.CTkButton(self, text="Login", command=lambda: self.authenticate(username_entry.get(), password_entry.get())).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=self.main_menu).pack(pady=10)

    def authenticate(self, username, password):
        for user in AccountUser:
            if username == user['username'] and password == user['password']:
                messagebox.showinfo("Login Successful", f"Welcome, {user['name']}!")
                self.view_account(username)
                return
        messagebox.showerror("Login Failed", "Wrong username or password!")

    def view_account(self, username):
        self.clear_frame()
        for user in AccountUser:
            if username == user['username']:
                ctk.CTkLabel(self, text=f"Account Number: {user['account_number']}", font=("Arial", 18)).pack(pady=10)
                ctk.CTkLabel(self, text=f"Name: {user['name']}", font=("Arial", 18)).pack(pady=10)
                ctk.CTkLabel(self, text=f"Balance: ${user['balance']}", font=("Arial", 18)).pack(pady=10)
                ctk.CTkButton(self, text="Transaction History", command=lambda: self.view_history(username)).pack(pady=5)
                ctk.CTkButton(self, text="Deposit", command=lambda: self.deposit(username)).pack(pady=5)
                ctk.CTkButton(self, text="Withdraw", command=lambda: self.withdraw(username)).pack(pady=5)
                ctk.CTkButton(self, text="Send Money", command=lambda: self.send_money_from(username)).pack(pady=5)
                ctk.CTkButton(self, text="Logout", command=self.main_menu).pack(pady=5)
                return

    def register_account(self):
        self.clear_frame()
        
        canvas = ctk.CTkCanvas(self)
        scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ctk.CTkLabel(scrollable_frame, text="Register", font=("Arial", 24)).pack(pady=20)
        
        ctk.CTkLabel(scrollable_frame, text="Account Type").pack(pady=5)
        account_type_var = ctk.StringVar(value="Savings")
        account_type_menu = ctk.CTkOptionMenu(scrollable_frame, variable=account_type_var, values=["Savings", "Checking"])
        account_type_menu.pack(pady=10)
        
        ctk.CTkLabel(scrollable_frame, text="Full Name").pack(pady=5)
        full_name_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Full Name")
        full_name_entry.pack(pady=10)
        
        ctk.CTkLabel(scrollable_frame, text="Username").pack(pady=5)
        username_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Username")
        username_entry.pack(pady=10)
        
        ctk.CTkLabel(scrollable_frame, text="Password").pack(pady=5)
        password_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Password", show="*")
        password_entry.pack(pady=10)
        
        ctk.CTkLabel(scrollable_frame, text="Confirm Password").pack(pady=5)
        confirm_password_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Confirm Password", show="*")
        confirm_password_entry.pack(pady=10)
        
        ctk.CTkLabel(scrollable_frame, text="Initial Deposit (Minimum $100)").pack(pady=5)
        initial_deposit_entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Initial Deposit")
        initial_deposit_entry.pack(pady=10)
        
        ctk.CTkButton(scrollable_frame, text="Register", command=lambda: self.create_account(
            account_type_var.get(), full_name_entry.get(), username_entry.get(), password_entry.get(), confirm_password_entry.get(), initial_deposit_entry.get()
        )).pack(pady=10)
        
        ctk.CTkButton(scrollable_frame, text="Back", command=self.main_menu).pack(pady=10)

    def create_account(self, type_of, full_name, username, password, confirm_password, initial_deposit):
        if len(username) < 3:
            messagebox.showerror("Error", "Username must have more than 3 characters.")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must have more than 6 characters.")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        if any(user['username'] == username for user in AccountUser):
            messagebox.showerror("Error", "Username already exists.")
            return
        try:
            initial_deposit = float(initial_deposit)
            if initial_deposit < 100:
                messagebox.showerror("Error", "Initial deposit must be at least $100.")
                return
            if initial_deposit > 100000:
                messagebox.showerror("Error", "Initial deposit exceeded the limit value.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
            return

        new_user_account = {
            "name": full_name,
            "account_number": self.generate_account_number(),
            "balance": initial_deposit,
            "username": username,
            "password": password,
            "account_type": type_of,
            "transactions": []
        }
        AccountUser.append(new_user_account)
        messagebox.showinfo("Success", "Account created successfully!")
        self.main_menu()

    def generate_account_number(self):
        prefix = "63877"
        while True:
            random_suffix = random.randint(100000, 999999)
            random_number = int(prefix + str(random_suffix))
            if not any(user['account_number'] == random_number for user in AccountUser):
                return random_number

    def view_history(self, username, page=1):
        self.clear_frame()
        transactions_per_page = 5
        for user in AccountUser:
            if username == user['username']:
                ctk.CTkLabel(self, text="Transaction History", font=("Arial", 24)).pack(pady=20)
                if user['transactions']:
                    start = (page - 1) * transactions_per_page
                    end = start + transactions_per_page
                    for transaction in user['transactions'][start:end]:
                        ctk.CTkLabel(self, text=f"{transaction['date']} - {transaction['type']} - ${transaction['amount']} - Balance: ${transaction['balance_after']}").pack(pady=5)
                    
                    total_pages = (len(user['transactions']) + transactions_per_page - 1) // transactions_per_page
                    if page > 1:
                        ctk.CTkButton(self, text="Previous", command=lambda: self.view_history(username, page - 1)).pack(side="left", padx=10)
                    if page < total_pages:
                        ctk.CTkButton(self, text="Next", command=lambda: self.view_history(username, page + 1)).pack(side="right", padx=10)
                else:
                    ctk.CTkLabel(self, text="No transactions found.").pack(pady=5)
                ctk.CTkButton(self, text="Back", command=lambda: self.view_account(username)).pack(pady=10)
                return

    def deposit(self, username):
        self.clear_frame()
        ctk.CTkLabel(self, text="Deposit", font=("Arial", 24)).pack(pady=20)
        ctk.CTkButton(self, text="Deposit $100", command=lambda: self.process_deposit(username, 100)).pack(pady=5)
        ctk.CTkButton(self, text="Deposit $500", command=lambda: self.process_deposit(username, 500)).pack(pady=5)
        ctk.CTkButton(self, text="Deposit $1000", command=lambda: self.process_deposit(username, 1000)).pack(pady=5)
        custom_amount_entry = ctk.CTkEntry(self, placeholder_text="Custom Amount")
        custom_amount_entry.pack(pady=10)
        ctk.CTkButton(self, text="Deposit Custom Amount", command=lambda: self.process_deposit(username, custom_amount_entry.get())).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: self.view_account(username)).pack(pady=10)

    def process_deposit(self, username, amount):
        try:
            amount = int(amount)
            if amount < 100:
                messagebox.showerror("Error", "Deposit amount must be at least $100.")
                return
            if amount > 1000000:
                messagebox.showerror("Error", "Deposit amount exceeds the limit.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
            return

        for user in AccountUser:
            if username == user['username']:
                user['balance'] += amount
                self.log_transaction(user, "Deposit", amount)
                messagebox.showinfo("Success", f"Deposited ${amount} successfully!")
                self.view_account(username)
                return

    def withdraw(self, username):
        self.clear_frame()
        ctk.CTkLabel(self, text="Withdraw", font=("Arial", 24)).pack(pady=20)
        ctk.CTkButton(self, text="Withdraw $100", command=lambda: self.confirm_withdraw(username, 100)).pack(pady=5)
        ctk.CTkButton(self, text="Withdraw $500", command=lambda: self.confirm_withdraw(username, 500)).pack(pady=5)
        ctk.CTkButton(self, text="Withdraw $1000", command=lambda: self.confirm_withdraw(username, 1000)).pack(pady=5)
        custom_amount_entry = ctk.CTkEntry(self, placeholder_text="Custom Amount")
        custom_amount_entry.pack(pady=10)
        ctk.CTkButton(self, text="Withdraw Custom Amount", command=lambda: self.confirm_withdraw(username, custom_amount_entry.get())).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: self.view_account(username)).pack(pady=10)

    def confirm_withdraw(self, username, amount):
        self.clear_frame()
        ctk.CTkLabel(self, text="Confirm Withdraw", font=("Arial", 24)).pack(pady=20)
        ctk.CTkLabel(self, text=f"Amount: ${amount}", font=("Arial", 18)).pack(pady=10)
        password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        password_entry.pack(pady=10)
        ctk.CTkButton(self, text="Confirm", command=lambda: self.process_withdraw(username, amount, password_entry.get())).pack(pady=10)
        ctk.CTkButton(self, text="Undo", command=lambda: self.withdraw(username)).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: self.view_account(username)).pack(pady=10)

    def process_withdraw(self, username, amount, password):
        for user in AccountUser:
            if username == user['username']:
                if user['password'] != password:
                    messagebox.showerror("Error", "Incorrect password.")
                    self.confirm_withdraw(username, amount)
                    return
                try:
                    amount = int(amount)
                    if amount < 100:
                        messagebox.showerror("Error", "Withdraw amount must be at least $100.")
                        self.confirm_withdraw(username, amount)
                        return
                except ValueError:
                    messagebox.showerror("Error", "Invalid amount entered.")
                    self.confirm_withdraw(username, amount)
                    return

                if user['balance'] < amount:
                    messagebox.showerror("Error", "Insufficient balance.")
                    self.confirm_withdraw(username, amount)
                    return

                user['balance'] -= amount
                self.log_transaction(user, "Withdraw", amount)
                messagebox.showinfo("Success", f"Withdrew ${amount} successfully!")
                self.view_account(username)
                return

    def send_money_from(self, username):
        self.clear_frame()
        ctk.CTkLabel(self, text="Send Money", font=("Arial", 24)).pack(pady=20)
        recipient_entry = ctk.CTkEntry(self, placeholder_text="Recipient Account Number")
        recipient_entry.pack(pady=10)
        amount_entry = ctk.CTkEntry(self, placeholder_text="Amount")
        amount_entry.pack(pady=10)
        ctk.CTkButton(self, text="Send", command=lambda: self.process_send_money(username, recipient_entry.get(), amount_entry.get())).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: self.view_account(username)).pack(pady=10)

    def process_send_money(self, username, recipient_account_number, amount):
        try:
            recipient_account_number = int(recipient_account_number)
            amount = int(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
            return

        sender = None
        recipient = None

        for user in AccountUser:
            if username == user['username']:
                sender = user
                break

        if not sender:
            messagebox.showerror("Error", "Sender account not found.")
            return

        for user in AccountUser:
            if recipient_account_number == user['account_number']:
                recipient = user
                break

        if not recipient:
            messagebox.showerror("Error", "Recipient account not found.")
            return

        if sender['balance'] < amount:
            messagebox.showerror("Error", "Insufficient balance.")
            return

        sender['balance'] -= amount
        recipient['balance'] += amount

        self.log_transaction(sender, "Send Money", amount)
        self.log_transaction(recipient, "Receive Money", amount)

        messagebox.showinfo("Success", f"Sent ${amount} to {recipient['name']} successfully!")
        self.view_account(username)

    def log_transaction(self, user, transaction_type, amount):
        transaction_date = datetime.now().strftime("%d-%b-%Y")
        transaction = {
            "date": transaction_date,
            "type": transaction_type,
            "amount": amount,
            "balance_after": user["balance"]
        }
        user["transactions"].append(transaction)

if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()
