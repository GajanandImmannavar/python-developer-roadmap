#  How to convert Minutes to Hours  (Using "//" and "%")
Time  = 135
min = 60
Hour = Time // min
Min_1 = Time % min
print(f"{Hour} Hours {Min_1} Minutes\n")

# You have: seconds = 367  Convert into: minutes and remaining seconds 

Sec = 367
m = 367 // 60 
SEC = 367 % 60
print(f"{m} minutes {SEC} sec")

#  Convert Seconds to Hours, Minutes, Seconds You are given: seconds = 7384

Total_Minutes = 7384

hours = Total_Minutes // 3600
Remaining_Minutes = Total_Minutes % 3600

Minutes = Remaining_Minutes // 60
Remaining_Sec  = Remaining_Minutes % 60

print(f"{hours} Hours {Minutes} Minutes {Remaining_Sec} Seconds")


# 🟢 Problem 2 — Total Marks

# A student scored:

# math = 85
# science = 90
# english = 78

# Print:

# Total Marks = 253
# Average = 84.33333333333333

Math = 85
science = 90
english = 78
Total = Math+science+english
sum = Math + science + english  
average = sum / 3
print(Total)
print(f"{average}\n")


# # Problem 3 — Area and Perimeter of Rectangle
# # Given: length = 12, width = 8
# # Print
# # Area = 96
# # Perimeter = 40
# # Formula:
# # Area = length × width
# # Perimeter = 2 × (length + width)

Length = 12
Width = 8
Area = Length * Width
Perimeter = 2 * (Length + Width)
print("Area of Rectangle")
print(f"{Area}")
print("Perimeter of Rectangle")
print(f"{Perimeter}\n")


# Convert Money
# Given: amount = 786
# Convert into
# 7 notes of ₹100
# 1 note of ₹50
# 1 note of ₹20
# 1 note of ₹10
# 1 note of ₹5
# 1 coin of ₹1
# Use only: // and %
# Think like an ATM.

Amount = 786

Hundreds = Amount // 100
Amount = Amount % 100

Fifties = Amount // 50
Amount = Amount % 50

Twenties = Amount // 20
Amount = Amount % 20

Tens = Amount // 10
Amount = Amount % 10

fives = Amount // 5
Amount = Amount % 5

one = Amount // 1
Amount = Amount % 1

print(f"$100 Notes {Hundreds}\n")
print(f"$50 Notes {Fifties}\n")
print(f"$20 Notes {Twenties}\n")
print(f"$10 Notes {Tens}\n")
print(f"$5 Notes {Tens}\n")
print(f"$1 Coins {one}\n")

# Break a Number into Digits ⭐ (DSA Foundation)

# Given

# number = 583

# Print Hundreds = 5 Tens = 8  Ones = 3 Hint: Use only // and %

Number = 583
Hundred = Number // 100
Number = Number % 100

Tens = Number // 10
Number = Number % 10

Ones = Number // 1
Number =Number % 1

print (f"$5 Hundred Notes {Hundred}\n")
print(f"$8 Ten Notes {Tens}\n")
print(f"$3 Coins {Ones}\n")



# Remove the Last Digit of a Number

Number = 9876

last_digit = Number % 10

remaining_digit = Number // 10

last_two_digit = Number % 100

final = Number // 100

print(f"Original Number {Number}\n")

print(f"Last Number {last_digit}\n")

print(f"Remove Last digit {remaining_digit}\n")

print(f"Last Two Digit {last_two_digit}\n")

print(f"Remove Last Two Digit {final}\n")







