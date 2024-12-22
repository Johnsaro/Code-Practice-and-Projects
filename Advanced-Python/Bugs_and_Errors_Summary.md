# FILES {
    GUI_Bank.py, GUI_Random_Bank.py
}
# Random Bank System: User Account Management and Transactions

# Summary of Bugs and Errors Identified

## Bugs and Issues version 1

### 1. No Maximum Deposit Handling  
- **Severity**: Low  
- **Description**: Users can deposit very large amounts without any restrictions.
- **Fix**: Users can now see the max deposit amount, and the transaction will fail if the deposit amount exceeds the maximum limit.

### 2. Looping Menu in Invalid Withdrawals  
- **Severity**: Medium  
- **Description**: Error messages keep redirecting back to the menu, which might confuse users.
- **Enhancement**: Users will now be redirected to the view menu instead of the main menu and will be prompted to try again.

### 3. Missing Guidance After Recipient Error  
- **Severity**: Medium  
- **Description**: When the recipient account is invalid, there's no clear instruction to return to the menu.
- **Fix**: Provide instructions to try again later if the recipient is not found and return them to the view menu.

### 4. Long Transaction History Readability  
- **Severity**: Low  
- **Description**: Long transaction logs are hard to read; better formatting or breaking into pages is needed.

# Performance Observations

- **Execution Time**: All tests completed without noticeable lag for small datasets.
- **Scalability Risk**: With a larger dataset, search operations (e.g., locating accounts) may slow down due to linear searching.

# Recommendations

1. Implement binary search or indexing for account lookups to improve performance.
2. Add input validation for numerical limits on transactions.
3. Enhance user interface by adding guidance messages and formatting for readability.

# Account Number Attempt
- **Issue**: Users sometimes enter incorrect account numbers.
- **Recommendation**: Implement validation checks to ensure account numbers are in the correct format before processing.