import customtkinter as ctk
from tkinter import messagebox
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

class Bank360App:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank360 Management System")
        self.root.geometry("600x400")
        ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Bank360 Management System", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkLabel(self.root, text="Employee ID:", font=("Helvetica", 12)).pack(pady=10)
        self.employee_id_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.employee_id_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Login", command=self.login).pack(pady=10)
        ctk.CTkButton(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def login(self):
        employee_id = self.employee_id_entry.get()
        for admin in admin_accounts:
            if employee_id == admin['employee_id']:
                self.create_admin_dashboard(admin)
                return
        for employee in employees:
            if employee_id == employee['employee_id']:
                self.create_employee_dashboard(employee)
                return
        error_message = f"Error: No Employee with ID {employee_id} found. Possible causes: wrong ID type or ID does not exist."
        print(error_message)
        messagebox.showerror("Error", error_message)

    def create_admin_dashboard(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text=f"Welcome, ADMIN {admin['name']}!", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="Manage Accounts", command=lambda: self.admin_view(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Employee Management", command=lambda: self.manage_employees(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Reports & Analytics", command=lambda: self.reports_analytics(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Fraud Alerts", command=lambda: self.fraud_alerts(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Logout", command=self.create_login_screen).pack(pady=10)

    def create_employee_dashboard(self, employee):
        self.clear_screen()
        ctk.CTkLabel(self.root, text=f"Welcome, {employee['name']}!", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="View Customer Accounts", command=lambda: self.create_accounts_menu(employee)).pack(pady=5)
        ctk.CTkButton(self.root, text="Manage Transactions", command=lambda: messagebox.showinfo("Coming Soon", "Feature coming soon...")).pack(pady=5)
        ctk.CTkButton(self.root, text="Monitor Fraud Alerts", command=lambda: messagebox.showinfo("Coming Soon", "Feature coming soon...")).pack(pady=5)
        ctk.CTkButton(self.root, text="Customer Support Tickets", command=lambda: messagebox.showinfo("Coming Soon", "Feature coming soon...")).pack(pady=5)
        ctk.CTkButton(self.root, text="Currency Exchange Reports", command=lambda: messagebox.showinfo("Coming Soon", "Feature coming soon...")).pack(pady=5)
        ctk.CTkButton(self.root, text="Savings Goal Tracker Updates", command=lambda: messagebox.showinfo("Coming Soon", "Feature coming soon...")).pack(pady=5)
        ctk.CTkButton(self.root, text="Logout", command=self.create_login_screen).pack(pady=10)

    def create_accounts_menu(self, employee):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="View Customer Accounts", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="View All Customer Accounts", command=lambda: self.display_all_accounts(employee)).pack(pady=5)
        ctk.CTkButton(self.root, text="Search by Account Number", command=lambda: self.search_account_number(employee)).pack(pady=5)
        ctk.CTkButton(self.root, text="Search by Customer Name", command=lambda: self.search_customer_name(employee)).pack(pady=5)
        ctk.CTkButton(self.root, text="Back to Dashboard", command=lambda: self.create_employee_dashboard(employee)).pack(pady=10)

    def display_all_accounts(self, employee):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="All Customer Accounts", font=("Helvetica", 16, "bold")).pack(pady=20)
        for user in AccountUser:
            ctk.CTkLabel(self.root, text=f"{user['account_number']} | {user['name']} | ${user['balance']:.2f} | {user['account_type']}", font=("Helvetica", 12)).pack()
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_accounts_menu(employee)).pack(pady=10)

    def search_account_number(self, employee):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Search by Account Number", font=("Helvetica", 16, "bold")).pack(pady=20)
        self.account_number_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.account_number_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Search", command=lambda: self.perform_account_search(employee)).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_accounts_menu(employee)).pack(pady=10)

    def perform_account_search(self, employee):
        account_num = self.account_number_entry.get()
        if len(account_num) != 12 or not account_num.isdigit():
            error_message = f"Error: Account number {account_num} must be 12 digits. Possible causes: incorrect length or non-digit characters."
            print(error_message)
            messagebox.showerror("Error", error_message)
            return
        for user in AccountUser:
            if account_num == user['account_number']:
                messagebox.showinfo("Account Found", f"Account Number: {user['account_number']}\nName: {user['name']}\nBalance: ${user['balance']}\nAccount Type: {user['account_type']}")
                return
        error_message = f"Error: Account Number {account_num} not found. Possible causes: incorrect account number or account does not exist."
        print(error_message)
        messagebox.showerror("Error", error_message)

    def search_customer_name(self, employee):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Search by Customer Name", font=("Helvetica", 16, "bold")).pack(pady=20)
        self.customer_name_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.customer_name_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Search", command=lambda: self.perform_name_search(employee)).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_accounts_menu(employee)).pack(pady=10)

    def perform_name_search(self, employee):
        customer_name = self.customer_name_entry.get().strip().lower()
        if len(customer_name) < 6:
            error_message = f"Error: Customer Name {customer_name} must be 6 characters or above. Possible causes: name too short."
            print(error_message)
            messagebox.showerror("Error", error_message)
            return
        matches = [user for user in AccountUser if user["name"].lower() == customer_name]
        if matches:
            result = "\n".join([f"{match['account_number']} | {match['name']} | ${match['balance']:.2f} | {match['account_type']}" for match in matches])
            messagebox.showinfo("Matching Accounts", result)
        else:
            error_message = f"Error: No accounts found for the name {customer_name}. Possible causes: incorrect name or no matching accounts."
            print(error_message)
            messagebox.showerror("Error", error_message)

    def admin_view(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Employee List", font=("Helvetica", 16, "bold")).pack(pady=20)
        for employee in employees:
            ctk.CTkLabel(self.root, text=f"{employee['name']} | {employee['employee_id']}", font=("Helvetica", 12)).pack()
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_admin_dashboard(admin)).pack(pady=10)

    def manage_employees(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Employee Management", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="Add Employee", command=lambda: self.add_employee(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Edit Employee", command=lambda: self.edit_employee(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Delete Employee", command=lambda: self.delete_employee(admin)).pack(pady=5)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_admin_dashboard(admin)).pack(pady=10)

    def add_employee(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Add Employee", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkLabel(self.root, text="Employee ID:", font=("Helvetica", 12)).pack(pady=5)
        self.new_employee_id_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.new_employee_id_entry.pack(pady=5)
        ctk.CTkLabel(self.root, text="Name:", font=("Helvetica", 12)).pack(pady=5)
        self.new_employee_name_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.new_employee_name_entry.pack(pady=5)
        ctk.CTkLabel(self.root, text="Role:", font=("Helvetica", 12)).pack(pady=5)
        self.new_employee_role_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.new_employee_role_entry.pack(pady=5)
        ctk.CTkLabel(self.root, text="Email:", font=("Helvetica", 12)).pack(pady=5)
        self.new_employee_email_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.new_employee_email_entry.pack(pady=5)
        ctk.CTkLabel(self.root, text="Contact Number:", font=("Helvetica", 12)).pack(pady=5)
        self.new_employee_contact_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.new_employee_contact_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Add", command=self.save_new_employee).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.manage_employees(admin)).pack(pady=10)

    def save_new_employee(self):
        new_employee = {
            "employee_id": self.new_employee_id_entry.get(),
            "name": self.new_employee_name_entry.get(),
            "role": self.new_employee_role_entry.get(),
            "email": self.new_employee_email_entry.get(),
            "contact_number": self.new_employee_contact_entry.get(),
        }
        employees.append(new_employee)
        messagebox.showinfo("Success", "Employee added successfully!")
        self.manage_employees(None)

    def edit_employee(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Edit Employee", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkLabel(self.root, text="Employee ID:", font=("Helvetica", 12)).pack(pady=5)
        self.edit_employee_id_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.edit_employee_id_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Search", command=self.load_employee_details).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.manage_employees(admin)).pack(pady=10)

    def load_employee_details(self):
        employee_id = self.edit_employee_id_entry.get()
        for employee in employees:
            if employee["employee_id"] == employee_id:
                self.clear_screen()
                ctk.CTkLabel(self.root, text="Edit Employee", font=("Helvetica", 16, "bold")).pack(pady=20)
                ctk.CTkLabel(self.root, text="Name:", font=("Helvetica", 12)).pack(pady=5)
                self.edit_employee_name_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
                self.edit_employee_name_entry.insert(0, employee["name"])
                self.edit_employee_name_entry.pack(pady=5)
                ctk.CTkLabel(self.root, text="Role:", font=("Helvetica", 12)).pack(pady=5)
                self.edit_employee_role_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
                self.edit_employee_role_entry.insert(0, employee["role"])
                self.edit_employee_role_entry.pack(pady=5)
                ctk.CTkLabel(self.root, text="Email:", font=("Helvetica", 12)).pack(pady=5)
                self.edit_employee_email_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
                self.edit_employee_email_entry.insert(0, employee["email"])
                self.edit_employee_email_entry.pack(pady=5)
                ctk.CTkLabel(self.root, text="Contact Number:", font=("Helvetica", 12)).pack(pady=5)
                self.edit_employee_contact_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
                self.edit_employee_contact_entry.insert(0, employee["contact_number"])
                self.edit_employee_contact_entry.pack(pady=5)
                ctk.CTkButton(self.root, text="Save", command=lambda: self.save_employee_details(employee)).pack(pady=10)
                ctk.CTkButton(self.root, text="Back", command=lambda: self.manage_employees(None)).pack(pady=10)
                return
        messagebox.showerror("Error", "Employee not found!")

    def save_employee_details(self, employee):
        employee["name"] = self.edit_employee_name_entry.get()
        employee["role"] = self.edit_employee_role_entry.get()
        employee["email"] = self.edit_employee_email_entry.get()
        employee["contact_number"] = self.edit_employee_contact_entry.get()
        messagebox.showinfo("Success", "Employee details updated successfully!")
        self.manage_employees(None)

    def delete_employee(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Delete Employee", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkLabel(self.root, text="Employee ID:", font=("Helvetica", 12)).pack(pady=5)
        self.delete_employee_id_entry = ctk.CTkEntry(self.root, font=("Helvetica", 12))
        self.delete_employee_id_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Delete", command=self.confirm_delete_employee).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.manage_employees(admin)).pack(pady=10)

    def confirm_delete_employee(self):
        employee_id = self.delete_employee_id_entry.get()
        for employee in employees:
            if employee["employee_id"] == employee_id:
                employees.remove(employee)
                messagebox.showinfo("Success", "Employee deleted successfully!")
                self.manage_employees(None)
                return
        messagebox.showerror("Error", "Employee not found!")

    def reports_analytics(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Reports & Analytics", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="Generate Report", command=self.generate_report).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_admin_dashboard(admin)).pack(pady=10)

    def generate_report(self):
        # Placeholder for report generation logic
        messagebox.showinfo("Report", "Report generated successfully!")

    def fraud_alerts(self, admin):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Fraud Alerts", font=("Helvetica", 16, "bold")).pack(pady=20)
        ctk.CTkButton(self.root, text="Monitor Alerts", command=self.monitor_fraud_alerts).pack(pady=10)
        ctk.CTkButton(self.root, text="Back", command=lambda: self.create_admin_dashboard(admin)).pack(pady=10)

    def monitor_fraud_alerts(self):
        # Placeholder for fraud alert monitoring logic
        messagebox.showinfo("Fraud Alerts", "Monitoring fraud alerts!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = Bank360App(root)
    root.mainloop()
