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







