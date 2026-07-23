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


# 🚗 Project Task: Car Rental Eligibility Checker

# Build a car rental eligibility checker using only what you have learned so far.

# Store these values:
# Customer name
# Customer age
# Driving license validity in years
# Available wallet balance
# Rental price
# Whether the customer has unpaid fines
# Whether the car is available
# Rental rules

# The customer can rent the car only when:

# Age is greater than or equal to 21
# Driving license validity is greater than or equal to 1 year
# Wallet balance is greater than or equal to rental price
# The customer has no unpaid fines
# The car is available

# All conditions must be satisfied.

# Calculate:
# Rental_Valid
# Print:
# Customer Name
# Customer Age
# Rental Price
# Wallet Balance
# Rental Valid: True or False
# Use only:
# Variables
# int
# float
# str
# bool
# Arithmetic operators
# Comparison operators
# and
# or
# not

Name = "Gajanand L Immannavar"

Age = 22

License_Validity = 2

Wallet_Balance = 2000

Rental_Price = 1000

Unpaid_Fines = False

Car_available= False 


Rental_Valid =(
    Age >= 21 and License_Validity >= 1 and Wallet_Balance >= Rental_Price 
    and not Unpaid_Fines  and not Car_available 
)

print(f"{Name}")
print(f"{Age}")
print(f"{Rental_Price}")
print(f"{Wallet_Balance}")
print(f'{Rental_Valid}')



# 🔑 The Main Rule

# Use not when your variable already represents the negative condition.

# For example:

# has_unpaid_fines = False

# This variable means:

# Does the customer have unpaid fines?

# The rental rule says:

# The customer must NOT have unpaid fines.

# So:

# not has_unpaid_fines

# means:

# not False
# ↓
# True

# Therefore, the customer passes the condition.

# Example 1: Unpaid Fines
# has_unpaid_fines = False

# Read the variable:

# Has unpaid fines = False

# The requirement:

# Must NOT have unpaid fines.

# Code:

# not has_unpaid_fines

# Evaluation:

# not False
# ↓
# True

# Correct.


# 🏥 Project Task: Hospital Appointment Eligibility

# Build a hospital appointment eligibility checker using only what you have learned.

# Store these values:
# Patient name
# Patient age
# Appointment fee
# Patient wallet balance
# Whether the patient has valid ID
# Whether the doctor is available
# Whether the patient is banned from booking
# Appointment rules

# The appointment is valid only when:

# Patient age is greater than or equal to 18
# Appointment fee is less than or equal to wallet balance
# Patient has a valid ID
# Doctor is available
# Patient is not banned from booking

# All conditions must be satisfied.

# Calculate:
# Appointment_Valid
# Print:
# Patient Name
# Patient Age
# Appointment Fee
# Wallet Balance
# Appointment Valid: True or False
# Use only:
# Variables
# int, float, str, bool
# Arithmetic operators
# Comparison operators
# and
# or
# not
# print()




Patient_name = "Ji"

Patient_age = 90

Appointment_fee =20

Patient_wallet_balance = 2000

valid_ID = True

doctor_available =  True

patient_is_banned = False

Appointment_Valid =(
    Patient_age >= 18 and Appointment_fee <= Patient_wallet_balance 
    and  valid_ID and doctor_available and not  patient_is_banned
)

print(f"Patient: {Patient_name}")
print(f"Age: {Patient_age}")
print(f"Appointment Fee: {Appointment_fee}")
print(f"Wallet Balance: {Patient_wallet_balance}")
print(f"Appointment Valid: {Appointment_Valid}")


# 🏦 Project Task: Bank Loan Eligibility Checker

# Now let's combine all the operators you have learned so far in a more realistic project.

# Store these values:
# Applicant name
# Applicant age
# Monthly salary
# Loan amount
# Credit score
# Whether the applicant has existing unpaid loans
# Whether the applicant's documents are verified
# Loan eligibility rules

# The applicant is eligible for the loan only when:

# Age is greater than or equal to 21
# Monthly salary is greater than or equal to ₹30,000
# Credit score is greater than or equal to 700
# Loan amount is less than or equal to 10 times the monthly salary
# Applicant has no existing unpaid loans
# Documents are verified

# All conditions must be satisfied.

# Calculate:
# Loan_Eligible
# Print:
# Applicant Name
# Age
# Monthly Salary
# Loan Amounint, float, str, bool
# Arithmetic operators
# Comparison operators
# and
# or
# not
# print()t
# Credit Score
# Loan Eligible: True or False
# Use only:
# Variables


Applicant_Name  = "Gajanand L Immannavar"

Applicant_Age = 21

Monthly_Salary = 50000

Loan_Amount = 40000

Credit_Score = 1000

Unpaid_Loans = False

Documents_Verified = True 

Loan_Eligible = (
    Applicant_Age >= 21 and  Monthly_Salary > 30000
    and Credit_Score > 700 and Loan_Amount <= Monthly_Salary * 10
    and not Unpaid_Loans and Documents_Verified 
                )



print(f"{Applicant_Name}")
print(f"{Applicant_Age}")
print(f"{Monthly_Salary}")
print(f"{Loan_Amount}")
print(f"{Credit_Score}")
print(f"{Loan_Eligible}")



