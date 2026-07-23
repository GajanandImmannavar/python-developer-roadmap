# My First Real Project Task

# Created this program using only what I have learned.

# 📚 Student Hall Ticket Generator



Name = "Gajanand L Immannavar"
Attendance = 82
Internal_Marks = 42
Fees_Paid = True 
Suspend = False

HallTicket = Attendance >= 35 and Internal_Marks >= 42 and Fees_Paid == True and not Suspend and Name
print(f"Congratulation Gajanand You are Eligible For Exam : {HallTicket}")




# Correct Version :

Name = "Gajanand L Immannavar"
Attendance = 82
Internal_Marks = 42
Fees_Paid = True 
Suspend = False

HallTicket = (
    Attendance >= 75
    and Internal_Marks >= 35
    and Fees_Paid == True
    and not Suspend
)

print(f"Congratulations {Name}, You are Eligible For Exam: {HallTicket}")






# 🎓 Project Task: Scholarship Eligibility Checker

# Create a program that checks whether a student is eligible for a scholarship.

# Store these values:
# Student name
# Percentage
# Family income
# Entrance exam score
# Whether the student has submitted all documents
# Whether the student is currently suspended
# Scholarship rules:

# A student is eligible when:

# Percentage is greater than or equal to 80
# Family income is less than or equal to ₹5,00,000
# Entrance exam score is greater than or equal to 70
# All documents are submitted
# The student is not suspended

# All conditions must be satisfied.

# Your program should:

# Calculate a variable called:

# Scholarship_Eligible

# Then print the student's name and the eligibility result.

# Restrictions

# Use only what we have learned:

# Variables
# int, float, str, bool
# Arithmetic operators
# Comparison operators
# and
# or
# not
# print()

     #Not Eligible

Student_Name = "Gajanand L Immannavar"

Percentage =  75

Family_Income = 1000000

Entrance_Exam_Score =  75

Documents = True

Suspended = False


Scholarship=(
    Percentage >= 85 and Family_Income <= 1000000 and Entrance_Exam_Score >= 70
    and Documents == True and not Suspended and Student_Name
)
print(f"Sorry {Student_Name} You aren't Eligible for  Scholarship: {Scholarship}")



# 🛒 Project Task: Online Shopping Order Validation

# Build a small order validation system using only the operators you have learned.

# Store these values:
# Customer name
# Product price
# Customer wallet balance
# Product stock quantity
# Whether the customer is a verified user
# Whether the product is restricted
# Order rules:

# The order should be considered valid when:

# The product price is less than or equal to the customer's wallet balance.
# Product stock quantity is greater than 0.
# The customer is a verified user.
# The product is not restricted.

# All conditions must be satisfied.

# Your program should calculate:
# Order_Valid

# Then print:

# Customer name
# Product price
# Wallet balance
# Order valid: True or False
# Use only:
# Variables
# int, float, str, bool
# Arithmetic operators
# Comparison operators
# and
# or
# not
# print()


Customer_Name = "Gajanand L Immannavar"

Product_Price = 2000

Product_Stock_Quantity = 10

Wallet_Balance = 100

User = True

Product_Restricted = False

Order_Valid =(
    Product_Price <= Wallet_Balance and Product_Stock_Quantity > 0 and not User and not Product_Restricted
) 

print(f"Sorry {Customer_Name} the Product Prise is {Product_Price} and Wallet Balance is {Wallet_Balance} So Order is  {Order_Valid}")


# clean Code 

customer_name = "Gajanand L Immannavar"

product_price = 2000
wallet_balance = 100
product_stock_quantity = 10

is_verified_user = True
is_product_restricted = False

order_valid = (
    product_price <= wallet_balance
    and product_stock_quantity > 0
    and is_verified_user
    and not is_product_restricted
)

print(f"Customer: {customer_name}")
print(f"Product Price: Rs.{product_price}")
print(f"Wallet Balance: Rs.{wallet_balance}")
print(f"Order Valid: {order_valid}")




# 🏧 Project Task: ATM Withdrawal Validation

# Build an ATM withdrawal validation program using only the concepts learned so far.

# Store these values:
# Customer name
# Account balance
# Withdrawal amount
# ATM cash available
# Whether the card is active
# Whether the account is blocked
# Withdrawal rules:

# The withdrawal should be valid only when:

# Withdrawal amount is greater than 0
# Withdrawal amount is less than or equal to the account balance
# Withdrawal amount is less than or equal to the cash available in the ATM
# The card is active
# The account is not blocked

# All conditions must be satisfied.

# Calculate:
# Withdrawal_Valid
# Print:
# Customer name
# Account balance
# Withdrawal amount
# Withdrawal valid: True or False
# Use only:
# Variables
# int, float, str, bool
# Arithmetic operators
# Comparison operators
# and
# or
# not
# print()



Name = "Gajanand L Immannavar"

Balance = 200000

Withdrawal_amount = 20000

ATM_cash_available = 55000

card = True

Account_Blocked = False

Withdrawal_Valid =(
    Withdrawal_amount > 0 
    and Withdrawal_amount <= Balance 
    and Withdrawal_amount <= ATM_cash_available
    and card and not Account_Blocked
)

print(f"{Name}")
print(f"{Balance}")
print(f"{Withdrawal_amount}")
print(f"{Withdrawal_Valid}")



# customer_name = "Gajanand L Immannavar"

# account_balance = 200000
# withdrawal_amount = 20000
# atm_cash_available = 55000

# is_card_active = True
# is_account_blocked = False
# 1. Creating the Customer Name
# customer_name = "Gajanand L Immannavar"

# Python creates a string object:

# "Gajanand L Immannavar"

# Then:

# customer_name ───────► "Gajanand L Immannavar"

# The variable customer_name references that string object.

# 2. Creating the Account Balance
# account_balance = 200000

# Python creates an integer object:

# 200000

# Then:

# account_balance ─────► 200000
# 3. Creating the Withdrawal Amount
# withdrawal_amount = 20000

# Python creates:

# 20000

# Then:

# withdrawal_amount ──► 20000
# 4. Creating ATM Cash
# atm_cash_available = 55000

# Python creates:

# 55000

# Then:

# atm_cash_available ──► 55000
# 5. Card Status
# is_card_active = True

# Python uses the built-in Boolean object:

# True

# So:

# is_card_active ─────► True

# This means:

# The card is active.

# 6. Account Status
# is_account_blocked = False

# The variable references:

# False

# Meaning:

# The account is not blocked.

# Now the Important Part
# withdrawal_valid = (
#     withdrawal_amount > 0
#     and withdrawal_amount <= account_balance
#     and withdrawal_amount <= atm_cash_available
#     and is_card_active
#     and not is_account_blocked
# )

# Python evaluates the expression from left to right.

# Condition 1
# withdrawal_amount > 0

# Python retrieves the values:

# withdrawal_amount → 20000
# 0                 → 0

# Then compares:

# 20000 > 0

# Result:

# True

# Now the expression becomes:

# True and ...
# Condition 2
# withdrawal_amount <= account_balance

# Python retrieves:

# withdrawal_amount → 20000
# account_balance    → 200000

# Comparison:

# 20000 <= 200000

# Result:

# True

# Now:

# True and True and ...
# Condition 3
# withdrawal_amount <= atm_cash_available

# Values:

# 20000 <= 55000

# Result:

# True

# Now:

# True and True and True and ...
# Condition 4
# is_card_active

# The variable contains:

# is_card_active → True

# So:

# True

# Now:

# True and True and True and True and ...
# Condition 5
# not is_account_blocked

# First Python retrieves:

# is_account_blocked → False

# Then applies not:

# not False

# Result:

# True

# Now the complete expression is:

# True and True and True and True and True

# Final result:

# True

# Therefore:

# withdrawal_valid ───► True
# 🧠 Complete Flow
# withdrawal_amount > 0
# 20000 > 0
# ↓
# True
# withdrawal_amount <= account_balance
# 20000 <= 200000
# ↓
# True
# withdrawal_amount <= atm_cash_available
# 20000 <= 55000
# ↓
# True
# is_card_active
# ↓
# True
# not is_account_blocked
# not False
# ↓
# True

# Finally:

# True and True and True and True and True
# ↓
# True

# 🧠 Memory Diagram
# customer_name
#       │
#       ▼
# "Gajanand L Immannavar"


# account_balance
#       │
#       ▼
#    200000


# withdrawal_amount
#       │
#       ▼
#     20000


# atm_cash_available
#       │
#       ▼
#     55000


# is_card_active
#       │
#       ▼
#      True


# is_account_blocked
#       │
#       ▼
#      False

# Then:

#         ┌──────────────────────────────┐
#         │  withdrawal_valid expression │
#         └──────────────┬───────────────┘
#                        │
#                        ▼
#               True and True and
#               True and True and
#               True
#                        │
#                        ▼
#                     True