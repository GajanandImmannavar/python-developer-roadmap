# Example 1: Addition of Two Integers

# Python creates Integer Objects for 10 and 20.
# Variables 'a' and 'b' store references to those objects.
# When 'a + b' is executed, Python adds both Integer Objects,
# creates a new Integer Object (30), and stores its reference in 'c'.
print("Addition Section")
print("------------------------")
a = 10
b = 20
c = a + b
print("Example 1: Addition of two Number")
print(f"{a} + {b} = ")
print(f"{c}\n")

# Output
# 30


# Example 2: Addition of an Integer and a Float

# Python creates an Integer Object (10) and a Float Object (2.5).
# Before addition, Python automatically converts the Integer Object
# to a Float Object (10.0), performs the addition, creates a new
# Float Object (12.5), and stores its reference in 'c'.

a = 10
b = 2.5
c = a + b
print("Example 2: Addition of an Integer and a Float")
print(f"{a} + {b} = ")
print(f"{c}\n")

# Output
# 12.5

# Example 3: Addition of Two Floating-Point Numbers

# Python creates two Float Objects (10.5 and 20.5).
# It adds both Float Objects, creates a new Float Object (31.0),
# and stores its reference in 'c'.

a = 10.5
b = 20.5
c = a + b

print("Example 3: Addition of Two Floating-Point Numbers")
print(f"{a} + {b} = ")
print(f"{c}\n")

# Output
# 31.0

#  Example 4: Addition of integer and floating point numbers 
#  python creates an integer object for a and floating point for b  
#  before adding python ask can i add integer and floating point number 
#  yes why because we have learnt  Python Implicit type casting  Python automatically convert int to float 
#  but original value remains same (Remember)
#  than python adds both and Create new floating point object for c and result get assign to c
#  Python return final Result C
#  My Understanding is if you add int object + floating point object will get result in floating point 

a = 10
b = 20.5
c = a + b
print("Example 4: Addition of integer and floating point numbers")
print(f"{a} + {b} = ")
print(f"{c}\n")

# Output
# 30.5

# Example 5: Addition of Three Integer Numbers

a = 100
b = 150
c = 200
result = a + b + c
print("Example 5: Addition of Three Integer Numbers")
print(f"{a} + {b} + {c}  = ")
print(f"{result}\n\n")




# Example 1: Subtraction of Two Integer Numbers (" - ")
# 
print(" Subtraction Section\n")
print("-------------------------------------------------------------------------------")
a = 1000
b = 221
result = a - b
print("Example 1: Subtraction of Two Integer Numbers")
print(f"{a} - {b} = ")
print(f"{result}\n")


Num_1 =  10
Num_2 = 10.10
Total = Num_1 - Num_2
print("Example 2: Subtraction of an Integer and a Floating-Point Number")
print(f"{Num_1} - {Num_2} = ")
print(f"{Total}\n")

Float_1 = 10.10
Float_2 = 20.5
Result = Float_1 - Float_2
print("Example 3: Subtraction of Two Floating-Point Numbers")
print(f"{Float_1} - {Float_2} =")
print(f"{Result}\n")

Int1 = 101
Int2 = 202
Float1 = 101.1
Result = Int1 - Int2 - Float1
print("Example 4: Subtraction of Two Integers and One Floating-Point Number")
print(f"{Int1} - {Int2} - {Float1} = ")
print(f"{Result}\n")



# (Subtraction After Implicit Type Casting) This is trap no need to worry about this, we learnt python convert int to float there self
Num_A = 1000
Num_B = 101.1
Result = Num_A - Num_B
print("Example 5: Subtraction After Implicit Type Casting")
print(f"{Num_A} - {Num_B} =")
print(f"{Result}\n")
<<<<<<< HEAD


# Example 1: Multiplication of Two Integer Numbers

# Python creates Integer Objects for 10 and 20.
# Variables 'a' and 'b' store references to those objects.
# When 'a * b' is executed, Python multiplies both Integer Objects,
# creates a new Integer Object (200), and stores its reference in 'result'.

print("Multiplication Section")
print("-------------------------------------------------------------------------------")

a = 10
b = 20
result = a * b

print("Example 1: Multiplication of Two Integer Numbers")
print(f"{a} * {b} = ")
print(f"{result}\n")

# Output
# 200


# Example 2: Multiplication of an Integer and a Floating-Point Number

# Python creates an Integer Object (10) and a Float Object (2.5).
# Before multiplication, Python automatically converts the Integer Object
# to a Float Object (10.0), performs the multiplication, creates a new
# Float Object (25.0), and stores its reference in 'result'.

a = 10
b = 2.5
result = a * b

print("Example 2: Multiplication of an Integer and a Floating-Point Number")
print(f"{a} * {b} = ")
print(f"{result}\n")

# Output
# 25.0


# Example 3: Multiplication of Two Floating-Point Numbers

# Python creates two Float Objects (10.5 and 2.0).
# It multiplies both Float Objects, creates a new Float Object (21.0),
# and stores its reference in 'result'.

a = 10.5
b = 2.0
result = a * b

print("Example 3: Multiplication of Two Floating-Point Numbers")
print(f"{a} * {b} = ")
print(f"{result}\n")

# Output
# 21.0


# Example 4: Multiplication of Two Integers and One Floating-Point Number

# Python creates two Integer Objects and one Float Object.
# Before multiplication, Python converts Integer Objects to Float Objects.
# The original Integer Objects remain unchanged.
# Python multiplies all three values, creates a new Float Object,
# and stores its reference in 'result'.

a = 10
b = 5
c = 2.5
result = a * b * c

print("Example 4: Multiplication of Two Integers and One Floating-Point Number")
print(f"{a} * {b} * {c} = ")
print(f"{result}\n")

# Output
# 125.0


# Example 5: Multiplication After Implicit Type Casting

# Python creates an Integer Object and a Float Object.
# Python automatically performs implicit type casting by converting
# the Integer Object to a Float Object before multiplication.
# It creates a new Float Object for the result and stores
# its reference in 'result'.

a = 100
b = 1.25
result = a * b

print("Example 5: Multiplication After Implicit Type Casting")
print(f"{a} * {b} = ")
print(f"{result}\n")

# Output
# 125.0


# Example 1: Division of Two Integer Numbers

# Python creates Integer Objects for 20 and 10.
# Variables 'a' and 'b' store references to those objects.
# When 'a / b' is executed, Python performs true division,
# creates a new Float Object (2.0), and stores its reference in 'result'.

print("Division Section")
print("-------------------------------------------------------------------------------")

a = 20
b = 10
result = a / b

print("Example 1: Division of Two Integer Numbers")
print(f"{a} / {b} = ")
print(f"{result}\n")

# Output
# 2.0


# Example 2: Division of an Integer and a Floating-Point Number

# Python creates an Integer Object (20) and a Float Object (2.5).
# Before division, Python automatically converts the Integer Object
# to a Float Object (20.0), performs the division, creates a new
# Float Object (8.0), and stores its reference in 'result'.

a = 20
b = 2.5
result = a / b

print("Example 2: Division of an Integer and a Floating-Point Number")
print(f"{a} / {b} = ")
print(f"{result}\n")

# Output
# 8.0


# Example 3: Division of Two Floating-Point Numbers

# Python creates two Float Objects (20.5 and 2.5).
# It divides both Float Objects, creates a new Float Object (8.2),
# and stores its reference in 'result'.

a = 20.5
b = 2.5
result = a / b

print("Example 3: Division of Two Floating-Point Numbers")
print(f"{a} / {b} = ")
print(f"{result}\n")

# Output
# 8.2


# Example 4: Division of Two Integers and One Floating-Point Number

# Python creates two Integer Objects and one Float Object.
# Before division, Python converts Integer Objects to Float Objects.
# The original Integer Objects remain unchanged.
# Python performs the division from left to right,
# creates a new Float Object, and stores its reference in 'result'.

a = 100
b = 5
c = 2.0
result = a / b / c

print("Example 4: Division of Two Integers and One Floating-Point Number")
print(f"{a} / {b} / {c} = ")
print(f"{result}\n")

# Output
# 10.0


# Example 5: Division After Implicit Type Casting

# Python creates an Integer Object and a Float Object.
# Python automatically performs implicit type casting by converting
# the Integer Object to a Float Object before division.
# The '/' operator always returns a Float Object.
# Python stores the result in 'result'.

a = 50
b = 4.0
result = a / b

print("Example 5: Division After Implicit Type Casting")
print(f"{a} / {b} = ")
print(f"{result}\n")

# Output
# 12.5


# Example 1: Floor Division of Two Integer Numbers

# Python creates Integer Objects for 20 and 3.
# Variables 'a' and 'b' store references to those objects.
# When 'a // b' is executed, Python performs floor division,
# removes the fractional part, creates a new Integer Object (6),
# and stores its reference in 'result'.

print("Floor Division Section")
print("-------------------------------------------------------------------------------")

a = 20
b = 3
result = a // b

print("Example 1: Floor Division of Two Integer Numbers")
print(f"{a} // {b} = ")
print(f"{result}\n")

# Output
# 6


# Example 2: Floor Division of an Integer and a Floating-Point Number

# Python creates an Integer Object (20) and a Float Object (3.0).
# Before floor division, Python automatically converts the Integer Object
# to a Float Object (20.0), performs floor division, creates a new
# Float Object (6.0), and stores its reference in 'result'.

a = 20
b = 3.0
result = a // b

print("Example 2: Floor Division of an Integer and a Floating-Point Number")
print(f"{a} // {b} = ")
print(f"{result}\n")

# Output
# 6.0


# Example 3: Floor Division of Two Floating-Point Numbers

# Python creates two Float Objects (20.5 and 3.0).
# It performs floor division, removes the fractional part,
# creates a new Float Object (6.0),
# and stores its reference in 'result'.

a = 20.5
b = 3.0
result = a // b

print("Example 3: Floor Division of Two Floating-Point Numbers")
print(f"{a} // {b} = ")
print(f"{result}\n")

# Output
# 6.0


# Example 4: Floor Division of Two Integers and One Floating-Point Number

# Python creates two Integer Objects and one Float Object.
# Python automatically performs implicit type casting where required.
# Floor division is evaluated from left to right.
# Python creates a new Float Object and stores its reference in 'result'.

a = 100
b = 5
c = 2.0
result = a // b // c

print("Example 4: Floor Division of Two Integers and One Floating-Point Number")
print(f"{a} // {b} // {c} = ")
print(f"{result}\n")

# Output
# 10.0


# Example 5: Floor Division After Implicit Type Casting

# Python creates an Integer Object and a Float Object.
# Python automatically converts the Integer Object to a Float Object.
# It performs floor division, removes the fractional part,
# creates a new Float Object for the result,
# and stores its reference in 'result'.

a = 50
b = 4.0
result = a // b

print("Example 5: Floor Division After Implicit Type Casting")
print(f"{a} // {b} = ")
print(f"{result}\n")

# Output
# 12.0


# Example 1: Modulus of Two Integer Numbers

# Python creates Integer Objects for 20 and 3.
# Variables 'a' and 'b' store references to those objects.
# When 'a % b' is executed, Python calculates the remainder,
# creates a new Integer Object (2), and stores its reference in 'result'.

print("Modulus Section")
print("-------------------------------------------------------------------------------")

a = 20
b = 3
result = a % b

print("Example 1: Modulus of Two Integer Numbers")
print(f"{a} % {b} = ")
print(f"{result}\n")

# Output
# 2


# Example 2: Modulus of an Integer and a Floating-Point Number

# Python creates an Integer Object (20) and a Float Object (3.5).
# Python converts the Integer Object to a Float Object during the operation.
# It calculates the remainder, creates a new Float Object (2.5),
# and stores its reference in 'result'.

a = 20
b = 3.5
result = a % b

print("Example 2: Modulus of an Integer and a Floating-Point Number")
print(f"{a} % {b} = ")
print(f"{result}\n")

# Output
# 2.5


# Example 3: Modulus of Two Floating-Point Numbers

# Python creates two Float Objects (20.5 and 3.0).
# It calculates the remainder between both Float Objects,
# creates a new Float Object (2.5),
# and stores its reference in 'result'.

a = 20.5
b = 3.0
result = a % b

print("Example 3: Modulus of Two Floating-Point Numbers")
print(f"{a} % {b} = ")
print(f"{result}\n")

# Output
# 2.5


# Example 4: Modulus of Two Integers and One Floating-Point Number

# Python creates two Integer Objects and one Float Object.
# Python performs the modulus operation from left to right.
# If a Float Object is involved, the final result becomes a Float Object.
# Python creates a new Float Object and stores its reference in 'result'.

a = 100
b = 30
c = 4.0
result = a % b % c

print("Example 4: Modulus of Two Integers and One Floating-Point Number")
print(f"{a} % {b} % {c} = ")
print(f"{result}\n")

# Output
# 10.0


# Example 5: Modulus After Implicit Type Casting

# Python creates an Integer Object and a Float Object.
# Python automatically converts the Integer Object into a Float Object.
# It performs the modulus operation, creates a new Float Object,
# and stores its reference in 'result'.

a = 50
b = 6.0
result = a % b

print("Example 5: Modulus After Implicit Type Casting")
print(f"{a} % {b} = ")
print(f"{result}\n")

# Output
# 2.0

# % does not return the quotient. It returns the remainder after division.

# Example:

# 20 % 3

# Calculation:

# 20 = (3 × 6) + 2

# Result:

# 2


# Example 1: Exponentiation of Two Integer Numbers

# Python creates Integer Objects for 2 and 3.
# Variables 'a' and 'b' store references to those objects.
# When 'a ** b' is executed, Python raises 'a' to the power of 'b',
# creates a new Integer Object (8), and stores its reference in 'result'.

print("Exponent Section")
print("-------------------------------------------------------------------------------")

a = 2
b = 3
result = a ** b

print("Example 1: Exponentiation of Two Integer Numbers")
print(f"{a} ** {b} = ")
print(f"{result}\n")

# Output
# 8


# Example 2: Exponentiation of an Integer and a Floating-Point Number

# Python creates an Integer Object (2) and a Float Object (3.0).
# Python converts the Integer Object to a Float Object during the operation.
# It calculates the power, creates a new Float Object (8.0),
# and stores its reference in 'result'.

a = 2
b = 3.0
result = a ** b

print("Example 2: Exponentiation of an Integer and a Floating-Point Number")
print(f"{a} ** {b} = ")
print(f"{result}\n")

# Output
# 8.0


# Example 3: Exponentiation of Two Floating-Point Numbers

# Python creates two Float Objects (2.5 and 2.0).
# It calculates the power operation,
# creates a new Float Object (6.25),
# and stores its reference in 'result'.

a = 2.5
b = 2.0
result = a ** b

print("Example 3: Exponentiation of Two Floating-Point Numbers")
print(f"{a} ** {b} = ")
print(f"{result}\n")

# Output
# 6.25


# Example 4: Exponentiation of Two Integers and One Floating-Point Number

# Python creates two Integer Objects and one Float Object.
# Python evaluates exponentiation from right to left when multiple
# exponent operators are used.
# If a Float Object is involved, the final result becomes a Float Object.
# Python creates a new object and stores its reference in 'result'.

a = 2
b = 3
c = 2.0
result = a ** b ** c

print("Example 4: Exponentiation of Two Integers and One Floating-Point Number")
print(f"{a} ** {b} ** {c} = ")
print(f"{result}\n")

# Output
# 512.0


# Example 5: Exponentiation After Implicit Type Casting

# Python creates an Integer Object and a Float Object.
# Python automatically converts the Integer Object into a Float Object.
# It performs exponentiation, creates a new Float Object,
# and stores its reference in 'result'.

a = 5
b = 2.0
result = a ** b

print("Example 5: Exponentiation After Implicit Type Casting")
print(f"{a} ** {b} = ")
print(f"{result}\n")

# Output
# 25.0


# Assignment Operators
# ----------------------------------------------------------------------------------------------
#  Problem 1
x = 10
x += 5

print(x)

# Your explanation:

# treat as x+5 and calculate and python assign x to new number again now x = 15

# This is mostly correct.

# Let's make it more precise.

# Step 1
# x = 10

# Python creates

# Integer Object

# 10

# Memory

# x
# │
# ▼
# 10
# Step 2
# x += 5

# Python internally converts this into

# x = x + 5

# Python:

# Reads the object referenced by x (10).
# Adds 5.
# Creates a new integer object 15.
# Makes x refer to the new object 15.

# Memory

# Before

# x
# │
# ▼
# 10

# After

# x
# │
# ▼
# 15

# Notice:

#  Python did not change the object 10.

# It created a new object.

# This is because integers are immutable.




# Subtract and assign
x = 20

x -= 8

print(x)


# Multiply and assign
x = 6
x *= 4

print(x)



# Divide and assign
x = 10
x /= 1

print(x)




# Floor divide and assign
x = 15
x //= 2

print(x)





# Modulus and assign

x = 17
x %= 5

print(x)



# Exponent and assign

x = 50
x **= 3

print(x)