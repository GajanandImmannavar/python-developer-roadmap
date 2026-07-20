
# Problem 1 — Total Seconds

# Store:

# Seconds = 5432

# Print:

# 1 Hours
# 30 Minutes
# 32 Seconds



Seconds = 5432

Hours = Seconds // 3600
Remaining =  Seconds % 3600

Minutes = Remaining // 60
REMAINING = Remaining % 60


print(f"{Hours} Hours ")
print(f"{Minutes} Minutes")
print(f"{REMAINING} Seconds")




# Minutes = 8432

Minutes = 8432
Hours = Minutes // 3600
Remaining = Minutes % 3600
Minutes = Remaining // 60
Sec = Remaining % 60
print(f"{Hours}:Hours {Minutes}:Minutes {Sec}:Seconds")


# Time

# Convert

# 98765 seconds

# into

# Days
# Hours
# Minutes
# Seconds

Seconds = 98765

Day = Seconds // 86400
Remaining = Seconds % 86400

Hours = Remaining // 3600
Left = Remaining % 3600

Minutes = Left // 60
Second = Left % 60


print(f"{Day}: Day {Hours}: Hour {Minutes}:Minutes {Second}: Seconds")





# Problem 4 — Currency Breakdown

# Amount = 4867

Amount =  4867

Thousands = Amount // 1000

Remaining = Amount % 1000


Five_Hundreds  = Remaining // 500
Reman = Remaining % 500


Hundreds = Reman // 100
money = Reman % 100


fifty = money // 50
left = money % 50

twenties = left // 20
reman = left % 20


tens = reman // 10
save = reman % 10

fives = save // 5
having = save % 5

twos = having // 2
inhand = having % 2


ones = inhand // 1
mine = inhand % 1


print(f"{Thousands} 1000 notes")
print(f"{Five_Hundreds} 500 notes")
print(f"{Hundreds} 100 notes")
print(f"{fifty} 50 notes")
print(f"{twenties} 20 notes")
print(f"{tens} 10 notes")
print(f"{fives} 5 coins")
print(f"{twos} 2 coins")
print(f"{ones} 1 coins")





# Extract Digits
# Number = 72891

# Find

# Last digit

# Last two digits

# Last three digits

# Remaining after removing last digit

# Remaining after removing last two digits

# Remaining after removing last three digits





Number = 72891

Last_Digit = Number % 10
Last_Two_Digits = Number % 100
Last_Three_Digits = Number % 1000

Remaining_After_Last_Digit = Number // 10
Remaining_After_Last_Two_Digits = Number // 100
Remaining_After_Last_Three_Digits = Number // 1000
print(f"Original Number = {Number}")
print(f"Last digit: {Last_Digit}")
print(f"Last two digits: {Last_Two_Digits}")
print(f"Last three digits: {Last_Three_Digits}")

print(f"Remaining after removing last digit: {Remaining_After_Last_Digit}")
print(f"Remaining after removing last two digits: {Remaining_After_Last_Two_Digits}")
print(f"Remaining after removing last three digits: {Remaining_After_Last_Three_Digits}")





# Problem 2 — Average Marks

# Store marks of five subjects.

# Print:

# Total
# Average


KANNADA = 125
HINDI = 100
ENGLISH = 100
S_S = 100
SCIENCE = 80
MATH = 100
TOTAL = KANNADA + HINDI + ENGLISH + S_S + SCIENCE + MATH 
AVERAGE = TOTAL / 6
PERSANTAGE = (TOTAL/625)*100

print(f"Total Marks = {TOTAL}")
print(f"Average Marks = {AVERAGE}")
print(f"Persantage(%) = {PERSANTAGE}")



# Problem 3 — Area and Perimeter

# Store:

# Length = 25
# Width = 18

# Print:

# Area
# Perimeter

Length = 25
Width = 18
Area = Length * Width
Parameter =  2 * (Length + Width)
print(f"Area of this Place: {Area}")
print(f"Parameter of this Place {Parameter}")




# A movie is 3675 seconds long.

# Find:

# Hours

# Remaining Minutes

# Remaining Seconds

# Notice:
# This looks similar to time conversion, but you have to think about what "remaining" means.


Seconds = 3675
Hours = Seconds //  3600
Remaining_Minutes = Seconds % 3600
Minutes = Remaining_Minutes //  60
Sec = Remaining_Minutes % 60


print(f"{Hours}: Hours {Minutes}: Minutes  {Sec}: Seconds")


# Price of one notebook = ₹45
# Price of one pen = ₹12
# You bought:
# 8 notebooks
# 15 pens
# Find:
# Notebook cost
# Pen cost
# Total bill

Price_Of_NoteBook = 45
Price_Of_Pen = 12
Eight_NoteBooks = 8 * 45
Fifteen_Pens = 15 * 12


NoteBook_Cost = Eight_NoteBooks
Pen_Cost = Fifteen_Pens
Total_Bill = NoteBook_Cost + Pen_Cost

print(f"NoteBook Cost: {NoteBook_Cost}\n  Pen Cost: {Pen_Cost}\n  Total Bill: {Total_Bill}")








# Mobile Price = ₹25000

# Discount = ₹3500

# GST = ₹3870

# Find:

# Price after discount

# Final price after GST



Mobile_Price = 25000
Discount = 3500
Gst = 3870

Price_After_Discount = Mobile_Price - Discount
Final_Price = Price_After_Discount + Gst

print(f"Price after discount: {Price_After_Discount}\n Final price with gst: {Final_Price}")







# Basic Salary = ₹45000

# Bonus = ₹7500

# Tax = ₹3200

# Find:

# Gross Salary

# Net Salary


Basic_Salary = 45000
Bonus = 7500
Tax = 3200

Gross_Salary = Basic_Salary + Bonus
Net_Salary = Gross_Salary - Tax

print(f"Gross Salary: {Gross_Salary}\n Net Salary: {Net_Salary}")
# Previous Reading = 28450

# Current Reading = 29120

# Cost per Unit = ₹8

# Find:

# Units Consumed

# Total Bill


# Petrol Price = ₹104

# Litres = 23

# Find:

# Total Cost

Petrol_Price =  104
Litres = 23
Total_Cost = 104*23
print(f"Total Cost: {Total_Cost}")

# Electricity Bill

# Previous Reading = 28450

# Current Reading = 29120

# Cost per Unit = ₹8

# Find:

# Units Consumed

# Total Bill



