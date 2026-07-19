
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






