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

# If you divide by 100, what does the remainder represent?

# Example:

# 987654 = ?

# Think about what remains after removing complete groups of 100.

# Rules
# ✅ Use only arithmetic operators.
# ✅ No strings.
# ✅ No loops.
# ✅ No if.


# Number = 987654 
# REMAINING = Number // 100
# print(f"After Dividing By 100: {REMAINING}\n")

# Number = Number % 100

# print(f"{Number}\n")

# Printing Last Number
number = 987654

last_two_digits = number % 100

print(last_two_digits)

# Remove the Last Two Digits
N =  987654

Left_No = N // 100

print(f"{Left_No}\n")

# Assignment Operators
# ----------------------------------------------------------------------------------------------
# python create int object 
# Step 1


# x = 10

# Python creates an Integer Object.

# Memory:

# x
# │
# ▼
# 10
# Step 2
# y = x

# Does Python create another integer object?

# No.

# It simply makes y refer to the same object.

# Memory:

# x ─┐
#    │
#    ▼
#   10
#    ▲
#    │
# y ─┘

# Both variables point to the same integer object.

# Step 3
# x += 5

# Python treats it as

# x = x + 5

# Now think carefully.

# Does Python change the integer object 10?

# ❌ No.

# Why?

# Because integers are immutable.

# Python creates a new integer object.

# 15

# Then x starts referring to this new object.

# Memory becomes:

# x ─────► 15

# y ─────► 10

# Notice something?

# y never moved.

# It still refers to the original integer object 10.

# That is why:

# print(x)

# prints

# 15

# and

# print(y)

# prints

# 10



x = 10
y = x

x += 5 

print(x)
print(y)




# This Is The Biggest Difference
# Immutable
x = 10

y = x

x += 5

# Memory

# Before

# x ─┐
#    │
#    ▼
#  10
#  ▲
#  │
#  y

# After

# x ─────► 15

# y ─────► 10

# A new object is created.

# Mutable

x = [10]

y = x

x.append(20)

# Memory

# Before

# x ─┐
#    │
#    ▼
# [10]
#  ▲
#  │
#  y

# After

# x ─┐
#    │
#    ▼
# [10,20]
#  ▲
#  │
#  y

# The same object changes.



x = [10]
y=x
x =[100]

y.append(20)
print(x)
print(y)



# Comparison Operator



# Example 1: Comparing Two Boolean Objects

x = True
y = True
print(x==y)

# Step 1

# Python creates a Boolean Object with value True.

# Since the value already exists, Python may reuse the same Boolean Object.

# Memory

#       x ─┐
#          │
#          ▼
#      Boolean Object
#      Value : True
#      Type  : bool
#          ▲
#          │
#       y ─┘

# Step 2

# Python executes

# x == y

# Python performs these steps:

# 1. Looks at variable 'x'.
# 2. Finds the Boolean Object referenced by 'x'.
# 3. Looks at variable 'y'.
# 4. Finds the Boolean Object referenced by 'y'.
# 5. Compares their values.
# 6. Since both values are True, Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Reason

# Both objects have the same Boolean value (True), so the comparison returns True.


# Example 2: Comparing Two Different Boolean Objects

x = False
y = True
print(x==y)

# Memory

# x ─────► Boolean Object (False)

# y ─────► Boolean Object (True)

# Python executes

# x == y

# Python performs these steps:

# 1. Finds the Boolean Object referenced by 'x'.
# 2. Finds the Boolean Object referenced by 'y'.
# 3. Compares their values.
# 4. False is not equal to True.
# 5. Python creates the Boolean Object False.
# 6. print() displays False.

# Output

# False

# Reason

# The Boolean values are different, so the comparison returns False.

# Example 3: Comparing a Floating-Point Number and an Integer

x = 5.0
y = 5
print(x==y)

# Memory

# x ─────► Float Object (5.0)

# y ─────► Integer Object (5)

# Python executes

# x == y

# Python performs these steps:

# 1. Finds the Float Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Checks whether both numeric values can be compared.
# 4. Python compares their numeric values (5.0 and 5).
# 5. Since both represent the same numeric value, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Although the object types are different (`float` and `int`), both represent the same numeric value (5). Therefore, `5.0 == 5` evaluates to `True`.

x = 10

y = 10.0

print(type(x))
print(type(y))
print(x == y)

# Example 9: Comparing an Integer and a Floating-Point Number

# x = 10
# y = 10.0


# Example 9: Comparing an Integer and a Floating-Point Number

# x = 10
# y = 10.0

# Step 1

# Python creates an Integer Object with value 10.

# Memory

# x ─────► Integer Object
#           Value : 10
#           Type  : int

# Step 2

# Python creates a Float Object with value 10.0.

# Memory

# x ─────► Integer Object (10)

# y ─────► Float Object (10.0)

# Step 3

# Python executes

# type(x)

# Python finds the object referenced by 'x',
# checks its type, and returns the type object <class 'int'>.

# Output

# <class 'int'>

# Step 4

# Python executes

# type(y)

# Python finds the object referenced by 'y',
# checks its type, and returns the type object <class 'float'>.

# Output

# <class 'float'>

# Step 5

# Python executes

# x == y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Checks whether both numeric values can be compared.
# 4. Python compares the numeric values (10 and 10.0).
# 5. Since both represent the same numeric value, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Although 'x' is an Integer Object and 'y' is a Float Object,
# both represent the same numeric value (10).

# The `==` operator compares values, not object types.
# Therefore,

# 10 == 10.0

# returns

# True.

# Quick Rule


# | Expression       | Result  | Reason                     |
# | ---------------- | ------- | -------------------------- |
# | `5 != 5.0`       | `False` | Same numeric value         |
# | `"AI" != "AI"`   | `False` | Same string value          |
# | `False != False` | `False` | Same Boolean value         |
# | `100 != "100"`   | `True`  | Different types and values |




Name = 'Gajanand'
User_Name = "gajanand"

print(Name != User_Name)


Age = 22
user_Age = 21
print(Age != user_Age)


Message = "Hi Hello"
Received_Message= "Hello"

print(Message != Received_Message)


Number =  21
str = 'Hi'
print(Number != str)


# Greater than ">"

Num1 = 100.1
Num2 = 100
print(Num1>Num2)


Num1 = 100.0
Num2 = 100
print(Num1<Num2)


Str = 'Hi'
Str1 = 'Hello'

print(Str>Str1)

# output  true 
Example 6: Comparing Two String Objects Using >

Str = "Hi"
Str1 = "Hello"

print(Str > Str1)

# Memory

# Str  ─────► String Object ("Hi")

# Str1 ─────► String Object ("Hello")

# Python executes

# Str > Str1

# Python performs these steps:

# 1. Finds the String Object referenced by 'Str'.
# 2. Finds the String Object referenced by 'Str1'.
# 3. Compares both strings lexicographically (dictionary order).
# 4. Python compares the first characters:
#       'H' and 'H' → Both are equal.
# 5. Python moves to the next characters:
#       'i' and 'e'
# 6. The character 'i' comes after 'e' in Unicode (ASCII) order.
# 7. Therefore, "Hi" is considered greater than "Hello".
# 8. Python creates the Boolean Object True.
# 9. print() displays True.

# Output

# True

# Reason

# Python compares strings character by character.

# Since 'i' comes after 'e',

# "Hi" > "Hello"

# returns

# True.





Str = "Good bye!"
Int1 = 100

print(Str > Int1)

# You will get Error instead output remember python raise Error when you  compare string with Int






#  Less than Operator "<"

a = 10
b = 22
print(a<b)


a = 2.2
b = 2.1

print(a<b)

Str = '1'
str2 = 1

print(Str < str2)


# Error Because we are comparing Int and Str Which is not work 




Num1 = 21
Num2 = Num1

Num1 = 20

print(Num2<Num1)

# OutPut = True we learnt Assignment Operators  Num1 refers to 20 but 21 not changed and Num2 still refers to 21







