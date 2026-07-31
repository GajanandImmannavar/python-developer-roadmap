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


# Comparison Operators
# ---------------------------------------------------------------------------------------------

# Example 1: Comparing Two Equal Integer Objects

x = 10
y = 10
print(x == y)

# Step 1

# Python creates an Integer Object with value 10.

# Since the value already exists, Python may reuse the same Integer Object.

# Memory

#       x ─┐
#          │
#          ▼
#       Integer Object
#       Value : 10
#       Type  : int
#          ▲
#          │
#       y ─┘

# Step 2

# Python executes

# x == y

# Python performs these steps:

# 1. Looks at variable 'x'.
# 2. Finds the Integer Object referenced by 'x'.
# 3. Looks at variable 'y'.
# 4. Finds the Integer Object referenced by 'y'.
# 5. Compares their values.
# 6. Since both values are equal, Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Python retrieves the objects referenced by x and y, compares their values,
# creates a Boolean object True, 
# and print() displays it.



# Example 2: Comparing Two Different Integer Objects

x = 10
y = 20
print(x == y)

# Memory

# x ─────► Integer Object (10)

# y ─────► Integer Object (20)

# Python executes

# x == y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their values.
# 4. Since 10 is not equal to 20, Python creates the Boolean Object False.
# 5. print() displays False.

# Output

# False


# Example 3: Comparing Two Equal String Objects

a = "Python"
b = "Python"
print(a == b)

# Step 1

# Python creates a String Object with value "Python".

# Since the same string already exists, Python may reuse the same String Object.

# Memory

#       a ─┐
#          │
#          ▼
#      String Object
#      Value : "Python"
#      Type  : str
#          ▲
#          │
#       b ─┘

# Step 2

# Python compares the values of both String Objects.

# The values are equal.

# Python creates the Boolean Object True.

# Output

# True


# Example 4: Comparing Two Different String Objects

a = "Python"
b = "python"
print(a == b)

# Memory

# a ─────► String Object ("Python")

# b ─────► String Object ("python")

# Python compares both string values.

# Python is case-sensitive.

# "P" and "p" are different characters.

# Python creates the Boolean Object False.

# Output

# False

# Example 5: Comparing an Integer and a String

x = 10
y = "10"
print(x==y)

# Memory

# x ─────► Integer Object (10)

# y ─────► String Object ("10")

# Python executes

# x == y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the String Object referenced by 'y'.
# 3. Checks their types.
# 4. int and str are different object types.
# 5. Their values are not considered equal.
# 6. Python creates the Boolean Object False.
# 7. print() displays False.

# Output

# False
# Example 1: Comparing an Integer and a Floating-Point Number Using !=

x = 5
y = 5.0

print(x != y)

# Memory

# x ─────► Integer Object (5)

# y ─────► Float Object (5.0)

# Python executes

# x != y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. 5 and 5.0 represent the same numeric value.
# 5. Therefore, the values are equal.
# 6. Since != means "not equal", Python creates the Boolean Object False.
# 7. print() displays False.

# Output

# False

# Reason

# 5 and 5.0 have different types but the same numeric value.
# Therefore, they are equal and != returns False.


# Example 2: Comparing Two Equal String Objects Using !=

x = "AI"
y = "AI"

print(x != y)

# Memory

#       x ─┐
#          │
#          ▼
#      String Object
#      Value : "AI"
#          ▲
#          │
#       y ─┘

# Python executes

# x != y

# Python performs these steps:

# 1. Finds the String Object referenced by 'x'.
# 2. Finds the String Object referenced by 'y'.
# 3. Compares their values.
# 4. Both strings contain "AI".
# 5. The values are equal.
# 6. Since != means "not equal", Python creates the Boolean Object False.
# 7. print() displays False.

# Output

# False

# Reason

# Both String Objects contain the same value ("AI").
# Therefore, they are equal and != returns False.


# Example 3: Comparing Two Equal Boolean Objects Using !=

x = False
y = False

print(x != y)

# Memory

#       x ─┐
#          │
#          ▼
#     Boolean Object
#     Value : False
#          ▲
#          │
#       y ─┘

# Python executes

# x != y

# Python performs these steps:

# 1. Finds the Boolean Object referenced by 'x'.
# 2. Finds the Boolean Object referenced by 'y'.
# 3. Compares their values.
# 4. Both values are False.
# 5. The values are equal.
# 6. Since != means "not equal", Python creates the Boolean Object False.
# 7. print() displays False.

# Output

# False

# Reason

# Both Boolean Objects contain the same value (False).
# Therefore, they are equal and != returns False.


# Example 4: Comparing an Integer and a String Using !=

x = 100
y = "100"

print(x != y)

# Memory

# x ─────► Integer Object (100)

# y ─────► String Object ("100")

# Python executes

# x != y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the String Object referenced by 'y'.
# 3. Compares their values and types.
# 4. Integer Object (100) and String Object ("100") are different.
# 5. Therefore, the values are not equal.
# 6. Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Reason

# 100 and "100" may look similar, but one is an Integer Object and the other is a String Object.

# Therefore,

# 100 != "100"

# returns

# True.


# Example 1: Comparing Two Integer Numbers Using >

x = 20
y = 10

print(x > y)

# Memory

# x ─────► Integer Object (20)

# y ─────► Integer Object (10)

# Python executes

x > y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 20 is greater than 10.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# 20 is greater than 10.
# Therefore,

# 20 > 10

# returns

# True.

# Example 2: Comparing an Integer and a Floating-Point Number Using >

x = 15
y = 10.5

print(x > y)

# Memory

# x ─────► Integer Object (15)

# y ─────► Float Object (10.5)

# Python executes

x > y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 15 is greater than 10.5.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Python can compare Integer Objects and Float Objects because both are numeric types.

# 15 > 10.5

# returns

# True.



# Example 3: Comparing Two Floating-Point Numbers Using >

x = 5.5
y = 8.5

print(x > y)

# Memory

# x ─────► Float Object (5.5)

# y ─────► Float Object (8.5)

# Python executes

x > y

# Python performs these steps:

# 1. Finds the Float Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 5.5 is greater than 8.5.
# 5. Since the condition is False, Python creates the Boolean Object False.
# 6. print() displays False.

# Output

# False

# Reason

# 5.5 is less than 8.5.

# Therefore,

# 5.5 > 8.5

# returns

# False.


# Example 4: Comparing Two Equal Integer Numbers Using >

x = 100
y = 100

print(x > y)

# Memory

#       x ─┐
#          │
#          ▼
#     Integer Object
#     Value : 100
#          ▲
#          │
#       y ─┘

# Python executes

x > y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 100 is greater than 100.
# 5. Since both values are equal, the condition is False.
# 6. Python creates the Boolean Object False.
# 7. print() displays False.

# Output

False

# Reason

# 100 is equal to 100, not greater.

# Therefore,

# 100 > 100

# returns

# False.



# Example 5: Comparing an Integer and a String Using >

x = 10
y = "10"

print(x > y)

# Memory

# x ─────► Integer Object (10)

# y ─────► String Object ("10")

# Python executes

x > y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the String Object referenced by 'y'.
# 3. Python checks whether both objects can be compared.
# 4. Integer Objects and String Objects cannot be ordered using '>'.
# 5. Python raises a TypeError.
# 6. The program stops unless the error is handled.

# Output

# TypeError:
# '>' not supported between instances of 'int' and 'str'

# Reason

# The `>` operator compares the order of values.

# Python can compare numeric types like `int` and `float`, but it cannot compare an `int` with a `str`.

# Therefore,

10 > "10"

# raises a **TypeError** instead of returning `True` or `False`.




#####################################################################################################################
# Less than Operator

# Example 1: Comparing Two Integer Numbers Using <

x = 10
y = 20

print(x < y)

# Memory

# x ─────► Integer Object (10)

# y ─────► Integer Object (20)

# Python executes

x < y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 10 is less than 20.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# 10 is less than 20.

# Therefore,

# 10 < 20

# returns

# True.


# Example 2: Comparing an Integer and a Floating-Point Number Using <

x = 15
y = 20.5

print(x < y)

# Memory

# x ─────► Integer Object (15)

# y ─────► Float Object (20.5)

# Python executes

x < y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 15 is less than 20.5.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Python can compare Integer Objects and Float Objects because both are numeric types.

# 15 < 20.5

# returns

# True.



# Example 3: Comparing Two Floating-Point Numbers Using <

x = 30.5
y = 10.5

print(x < y)

# Memory

# x ─────► Float Object (30.5)

# y ─────► Float Object (10.5)

# Python executes

x < y

# Python performs these steps:

# 1. Finds the Float Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 30.5 is less than 10.5.
# 5. Since the condition is False, Python creates the Boolean Object False.
# 6. print() displays False.

# Output

# False

# Reason

# 30.5 is greater than 10.5.

# Therefore,

# 30.5 < 10.5

# returns

# False.



# Example 4: Comparing Two Equal Integer Numbers Using <

x = 100
y = 100

print(x < y)

# Memory

#       x ─┐
#          │
#          ▼
#     Integer Object
#     Value : 100
#          ▲
#          │
#       y ─┘

# Python executes

x < y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 100 is less than 100.
# 5. Since both values are equal, the condition is False.
# 6. Python creates the Boolean Object False.
# 7. print() displays False.

# Output

# False

# Reason

# 100 is equal to 100, not less.

# Therefore,

# 100 < 100

# returns

# False.

# Example 5: Comparing Two String Objects Using <


Str = "Apple"
Str1 = "Banana"

print(Str < Str1)

# Memory

# Str  ─────► String Object ("Apple")

# Str1 ─────► String Object ("Banana")

# Python executes

Str < Str1

# Python performs these steps:

# 1. Finds the String Object referenced by 'Str'.
# 2. Finds the String Object referenced by 'Str1'.
# 3. Compares both strings lexicographically (dictionary order).
# 4. Python compares the first characters:
#       'A' and 'B'
# 5. The character 'A' comes before 'B' in Unicode order.
# 6. Therefore, "Apple" is considered less than "Banana".
# 7. Python creates the Boolean Object True.
# 8. print() displays True.

# Output

# True

# Reason

# Python compares strings character by character.

# Since 'A' comes before 'B',

# "Apple" < "Banana"

# returns

# True.

#####################################################################################################################
# 5 examples for the >= (Greater Than or Equal To) operator in the same style as your repository.

# Example 1: Comparing Two Integer Numbers Using >=

x = 20
y = 10

print(x >= y)

# Memory

# x ─────► Integer Object (20)

# y ─────► Integer Object (10)

# Python executes

# x >= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 20 is greater than or equal to 10.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# 20 is greater than 10.

# Therefore,

# 20 >= 10

# returns

# True.


# Example 2: Comparing Two Equal Integer Numbers Using >=

x = 100
y = 100

print(x >= y)

# Memory

#       x ─┐
#          │
#          ▼
#     Integer Object
#     Value : 100
#          ▲
#          │
#       y ─┘

# Python executes

# x >= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 100 is greater than or equal to 100.
# 5. Since both values are equal, the condition is True.
# 6. Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Reason

# The values are equal.

# The '=' in '>=' allows equality.

# Therefore,

# 100 >= 100

# returns

# True.



# Example 3: Comparing an Integer and a Floating-Point Number Using >=

x = 50
y = 75.5

print(x >= y)

# Memory

# x ─────► Integer Object (50)

# y ─────► Float Object (75.5)

# Python executes

# x >= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 50 is greater than or equal to 75.5.
# 5. Since the condition is False, Python creates the Boolean Object False.
# 6. print() displays False.

# Output

# False

# Reason

# Python compares the numeric values.

# 50 is less than 75.5.

# Therefore,

# 50 >= 75.5

# returns

# False.


# Example 4: Comparing Two Floating-Point Numbers Using >=

x = 25.5
y = 25.5

print(x >= y)

# Memory

#       x ─┐
#          │
#          ▼
#      Float Object
#      Value : 25.5
#          ▲
#          │
#       y ─┘

# Python executes

x >= y

# Python performs these steps:

# 1. Finds the Float Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 25.5 is greater than or equal to 25.5.
# 5. Since both values are equal, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Both Float Objects have the same numeric value.

# Therefore,

# 25.5 >= 25.5

# returns

# True.



# Example 5: Comparing Two String Objects Using >=

Str = "Python"
Str1 = "Programming"

print(Str >= Str1)

# Memory

# Str  ─────► String Object ("Python")

# Str1 ─────► String Object ("Programming")

# Python executes

# Str >= Str1

# Python performs these steps:

# 1. Finds the String Object referenced by 'Str'.
# 2. Finds the String Object referenced by 'Str1'.
# 3. Compares both strings lexicographically (dictionary order).
# 4. Python compares the characters from left to right.
# 5. The first different characters determine the result.
# 6. Since 'y' comes after 'r' in Unicode order, "Python" is considered greater than "Programming".
# 7. Python creates the Boolean Object True.
# 8. print() displays True.

# Output

# True

# Reason

# Python compares strings character by character.

# "Python" comes after "Programming" in lexicographical order.

# Therefore,

# "Python" >= "Programming"

# returns

# True.

#############################################################################################################
# Operator "<="

# Example 1: Comparing Two Integer Numbers Using <=

x = 10
y = 20

print(x <= y)

# Memory

# x ─────► Integer Object (10)

# y ─────► Integer Object (20)

# Python executes

# x <= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 10 is less than or equal to 20.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# 10 is less than 20.

# Therefore,

# 10 <= 20

# returns

# True.



# Example 2: Comparing Two Equal Integer Numbers Using <=

x = 100
y = 100

print(x <= y)

# Memory

#       x ─┐
#          │
#          ▼
#     Integer Object
#     Value : 100
#          ▲
#          │
#       y ─┘

# Python executes

x <= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Integer Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 100 is less than or equal to 100.
# 5. Since both values are equal, the condition is True.
# 6. Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Reason

# The values are equal.

# The '=' in '<=' allows equality.

# Therefore,

# 100 <= 100

# returns

# True.



# Example 3: Comparing an Integer and a Floating-Point Number Using <=

x = 50
y = 75.5

print(x <= y)

# Memory

# x ─────► Integer Object (50)

# y ─────► Float Object (75.5)

# Python executes

x <= y

# Python performs these steps:

# 1. Finds the Integer Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 50 is less than or equal to 75.5.
# 5. Since the condition is True, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Python compares the numeric values.

# 50 is less than 75.5.

# Therefore,

# 50 <= 75.5

# returns


x = 25.5
# True.


# Example 4: Comparing Two Floating-Point Numbers Using <=
y = 25.5

print(x <= y)

# Memory

#       x ─┐
#          │
#          ▼
#      Float Object
#      Value : 25.5
#          ▲
#          │
#       y ─┘

# Python executes

x <= y

# Python performs these steps:

# 1. Finds the Float Object referenced by 'x'.
# 2. Finds the Float Object referenced by 'y'.
# 3. Compares their numeric values.
# 4. Checks whether 25.5 is less than or equal to 25.5.
# 5. Since both values are equal, Python creates the Boolean Object True.
# 6. print() displays True.

# Output

# True

# Reason

# Both Float Objects have the same numeric value.

# Therefore,

# 25.5 <= 25.5

# returns

# True.


# Example 5: Comparing Two String Objects Using <=

Str = "Apple"
Str1 = "Banana"

print(Str <= Str1)

# Memory

# Str  ─────► String Object ("Apple")

# Str1 ─────► String Object ("Banana")

# Python executes

Str <= Str1

# Python performs these steps:

# 1. Finds the String Object referenced by 'Str'.
# 2. Finds the String Object referenced by 'Str1'.
# 3. Compares both strings lexicographically (dictionary order).
# 4. Python compares the characters from left to right.
# 5. Since 'A' comes before 'B' in Unicode order, "Apple" is considered less than "Banana".
# 6. Python creates the Boolean Object True.
# 7. print() displays True.

# Output

# True

# Reason

# Python compares strings character by character.

# "Apple" comes before "Banana" in lexicographical order.

# Therefore,

# "Apple" <= "Banana"

# returns

# True.

############################################################################################


# Identity Operators in Python 

# Types of  Indetity Operators 
# 1: is 
# 2: is Not 

# Example 1: "is"

x = [1,2,3,4]
y = x

print(x == y)
print (x is y)

# Your answer:

# True
# True

# Correct.

# Memory:

# x ────────┐
#           ▼
#        [1,2,3,4]
#           ▲
# y ────────┘

# Both variables reference the exact same list object.

# Therefore:

# x == y → True
# x is y → True


x = 10
y = x

print(x == y)
print(x is y)

# Your answer:

# True
# True

# Correct.

# Because:

# y = x

# means y receives the same object reference.

# Conceptually:

# x ────────┐
#           ▼
#           10
#           ▲
# y ────────┘

# Therefore:

# x == y → True
# x is y → True
# 🧠 Important Correction for Professional Python

# Although your answer for Problem 3 is correct, remember this rule:

# x == y

# is the correct way to compare values.

# Do not normally write:

# x is y

# to compare integers, strings, or other ordinary values.

# For example:

# x = 1000
# y = 1000

# x == y

# is the correct value comparison.

# Use:

# x is y

# when you specifically want to ask:

# Are these the exact same object?

# The most common special case is:

# value is None

x = [1, 2, 3]
y = x

x.append(4)

print(x)
print(y)
print(x == y)
print(x is y)

# output:
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# True
# True

# Memory model
# x ───────┐
#          ▼
#      [1, 2, 3]
#          ▲
# y ───────┘

# Initially:

# y = x

# Both variables reference the same list object.

# Then:

# x.append(4)

# The list itself is modified:

# [1, 2, 3] → [1, 2, 3, 4]

# Because x and y point to the same object:

# x → [1, 2, 3, 4]
# y → [1, 2, 3, 4]

# Therefore:

# x == y   # True
# x is y   # True





x = [1, 2, 3]
y = [1, 2, 3]

x.append(4)

print(x)
print(y)
print(x == y)
print(x is y)

# output:
# [1, 2, 3, 4]
# [1, 2, 3]
# False
# False

# [1, 2, 3, 4]
# [1, 2, 3]
# False
# False



# Memory model
# x ─────► [1, 2, 3]

# y ─────► [1, 2, 3]

# Two separate list objects.

# After:

# x.append(4)

# Only the list referenced by x changes:

# x ─────► [1, 2, 3, 4]

# y ─────► [1, 2, 3]

# Therefore:

# x == y   # False

# The values are different.

# x is y   # False

# The objects are also different.

# x = [10, 20]
# y = x

# x = [100]

# print(x)
# print(y)
# print(x == y)
# print(x is y)

# # Output :
# # [100]
# # [10, 20]
# # False
# # False


####################################################
# is not

x = [10, 20]
y = x

print(x is y)
print(x is not y)

# Memory:

# x ───────┐
#          ▼
#       [10, 20]
#          ▲
# y ───────┘

# Output:

# True
# False

# Why?

# x is y

# Both refer to the same object:

# Same object → True

# Therefore:

# x is not y

# means:

# Different objects? → False



# Different Objects

x = [10, 20]
y = [10, 20]

print(x == y)
print(x is y)
print(x is not y)

# Output:

# True
# False
# True

# Explanation:

# Values are same       → x == y       → True
# Objects are different → x is y       → False
# Objects are different → x is not y   → True

# Memory:

# x ─────► [10, 20]

# y ─────► [10, 20]

# They have the same values but are two separate objects.


# ✅ Problem 1
# x = [1, 2, 3]
# y = x

# print(x is not y)

# Your answer:

# False

# ✅ Correct.

# Memory
# x ───────┐
#          ▼
#      [1, 2, 3]
#          ▲
# y ───────┘

# Python asks:

# "Are these different objects?"

# Answer:

# No

# So:

# x is not y

# returns

# False
# ✅ Problem 2
# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x is not y)

# Your answer:

# True

# ✅ Correct.

# Memory:

# x ─────► [1, 2, 3]

# y ─────► [1, 2, 3]

# Python asks:

# "Are these different objects?"

# Answer:

# Yes

# Therefore

# x is not y

# returns

# True
# ✅ Problem 3
# x = [10, 20]
# y = x

# x = [100]

# print(x is not y)

# Your answer:

# True

# ✅ Correct.

# Initially

# x ───────┐
#          ▼
#       [10,20]
#          ▲
# y ───────┘

# After

# x = [100]

# Memory becomes

# x ─────► [100]

# y ─────► [10,20]

# Now Python asks:

# "Are these different objects?"

# Yes.

# Therefore

# x is not y

# returns

# True
# 🎯 Master Revision (Identity Operators)
# Operator	Python asks	Compares	Returns
# is	Are both variables the same object?	Memory identity	True / False
# is not	Are both variables different objects?	Memory identity	True / False
# Memory Rule
# x = y
# x ───────┐
#          ▼
#       Object
#          ▲
# y ───────┘
# x is y → ✅ True
# x is not y → ❌ False
# x = [1]
# y = [1]
# x ─────► Object A

# y ─────► Object B
# x is y → ❌ False
# x is not y → ✅ True


############################################################################################################

# Membership  Operator

USN = [101, 102, 103, 104]
print(101 in USN )

# output 

# Step 1: Python creates the list

# Memory:

# USN
#  │
#  ▼
# +------------------------+
# | 101 | 102 | 103 | 104 |
# +------------------------+

# USN stores a reference to the list object.

# Step 2: Python evaluates
# 101 in USN

# Python asks:

# "Is 101 one of the elements inside this list?"

# Step 3: Search starts

# Python checks one element at a time.

# 101 ?

# ↓

# Found ✅

# ↓

# Stop searching

# Python doesn't continue because it already found the answer.

# Step 4: Python creates a Boolean object
# True
# Output
# True




name = "PYTHON"
print("P" in name)

# Step 1

# Python creates a string object.

# Memory

# name
#  │
#  ▼
# +-------------------+
# | P | Y | T | H | O | N |
# +-------------------+

# Strings are sequences of characters.

# Step 2

# Python evaluates

# "P" in name

# Python asks

# "Is the character P inside this string?"

# Step 3

# Search

# P ?

# ↓

# Found ✅

# ↓

# Stop
# Step 4

# Creates

# True
# Output
# True


name = "PYTHON"
print("Z" in name)

# Memory
# P
# Y
# T
# H
# O
# N
# Python asks

# "Is Z inside this string?"

# Search

# P ?

# No

# ↓

# Y ?

# No

# ↓

# T ?

# No

# ↓

# H ?

# No

# ↓

# O ?

# No

# ↓

# N ?

# No

# ↓

# Reached end

# Nothing matched.

# Python creates

# False

# Output: False

Numbers = [1,2,3,4,5,6,7,8,9,0]
print(1 not in Numbers)

# Numbers
#  │
#  ▼
# +------------------------------+
# |1|2|3|4|5|6|7|8|9|0|
# +------------------------------+

# Python first evaluates

# 1 in Numbers

# Search

# 1 ?

# ↓

# Found

# So

# 1 in Numbers

# becomes

# True

# Now Python applies

# not True

# which becomes

# False
# Output
# False


Numbers = [0,9,8,7,6,5,4,3,2,1]
print(1 in Numbers)

# Notice something important.

# Many beginners think because 1 is last, Python returns False.

# No.

# Python simply searches until it finds it.

# Memory

# 0
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# Search

# 0 ?

# No

# ↓

# 9 ?

# No

# ↓

# 8 ?

# No

# ↓

# ...

# ↓

# 1 ?

# Yes

# ↓

# Stop

# Output

# True

Student ={"Name": "Gajanand",
          "USN" : "1NH23AI406"}

print("USN" in Student)

# Memory
# Student
#  │
#  ▼

# +----------------------------------+
# | "Name" ─────► "Gajanand"         |
# | "USN"  ─────► "1NH23AI406"       |
# +----------------------------------+

# Notice there are two parts.

# Key

# Name
# USN

# Value

# Gajanand
# 1NH23AI406

# Python asks

# "Is USN one of the keys?"

# Search

# Name ?

# No

# ↓

# USN ?

# Yes

# Stop.

# Output

# True


student = {
    "name": "Gajanand",
    "age": 22
}

print("Gajanand" in student)


# Memory

# +------------------------------+
# | name ─────► Gajanand         |
# | age  ─────► 22               |
# +------------------------------+

# Python asks

# "Is Gajanand one of the keys?"

# Search

# name ?

# No

# ↓

# age ?

# No

# ↓

# End

# Notice

# Python never checks the values.

# It only checks

# Keys

# name
# age

# Therefore

# False
# Output
# False



# Universal Thinking Pattern

# Whenever you see:

# value in collection

# Think:

# Python

# ↓

# Evaluates left value

# ↓

# Evaluates right collection

# ↓

# Looks inside the collection

# ↓

# How it looks depends on the collection type

# List
# ↓

# Elements

# Tuple
# ↓

# Elements

# String
# ↓

# Characters

# Set
# ↓

# Elements (hash lookup)

# Dictionary
# ↓

# Keys



# Python's Internal Thinking

# Suppose

# numbers = [10, 20, 30]

# Now Python sees

# 20 in numbers

# Internally Python thinks:

# Step 1

# Evaluate the left operand.

# 20

# It becomes

# Search Value = 20
# Step 2

# Evaluate the right operand.

# numbers

# Python looks up the variable.

# It finds

# [10,20,30]

# Now Python knows

# Search Value

# 20

# Search Collection

# [10,20,30]
# Step 3

# Search begins

# 20 == 10 ?

# No

# ↓

# 20 == 20 ?

# Yes

# ↓

# Return True
# Another Example
# "P" in "PYTHON"

# Python sees

# "P"      in      "PYTHON"

# Left operand

# ↓

# P

# Right operand

# ↓

# PYTHON

# Python thinks

# Search

# P

# Inside

# PYTHON
# Another Example
# "USN" in student

# Suppose

# student = {
#     "Name":"Gajanand",
#     "USN":"1NH23AI406"
# }

# Python sees

# "USN"      in      student

# Left operand

# ↓

# USN

# Right operand

# ↓

# Dictionary

# Now Python thinks

# Search key

# USN

# Inside dictionary keys 

# Why doesn't Python search values?

# Because the dictionary is designed as a mapping.

# Think of it like a locker.

# Locker Number (Key)

# ↓

# Contains

# Student Bag (Value)

# Python knows the locker numbers.

# It does not know what is inside every locker until you open it.

# So when you write

# "USN" in student

# Python checks the locker labels (keys), not the contents (values).

# Universal Rule

# Every binary operator follows the same pattern.

# Left Operand

# ↓

# Operator

# ↓

# Right Operand

# Python:

# Evaluates the left operand into a value.
# Evaluates the right operand into a value.
# Applies the operator.
# Produces the result.
# Memory Trick

# Don't think:

# ❌ Left variable and right variable.

# Think:

# ✅ Left operand and right operand.

# An operand is simply anything that produces a value.

# Examples of operands:

# 10          # literal
# x           # variable
# x + y       # expression
# len(name)   # function call
# "Python"    # string literal


###########################################################################
# Bitwise Operator (&) And

First_Number = 10
Second_Number = 11
print(First_Number & Second_Number )


Num1 = 6
Num2 = 5
print(Num1 & Num2)

# output : 4

Left = 9
Right = 3
print(Left & Right)

# output = 1


First_And = 15
Second_And = 10
print(First_And & Second_And)

# Output :  10


First_Decimal = 8
Second_Decimal = 7
print(f"Output: {First_Decimal & Second_Decimal}")
# output : 0


print(13 & 11)


print(14 & 5)


print(2 & 1)


print(12 & 4)


print(11 & 6)


print(7 & 1)


# def Even_Odd(n):
#     if n & 1:
#         print(f"{n} is Odd")
#     else:
#         print(f"{n} is Even")
# while True:
#     n = int(input("Enter Number: "))
#     Even_Odd(n)


##############################

# Bitwise Operator (|) Or


A = 10
B = 2
print(A | B)

#output : 10


X = 100
Y = 0
print(X | Y)

# output : 100
# Because
# The Rule is :  X | 0 = X


P = 100
Q = 100

print(P | Q)

# Output: 100


Num1 = 12
Num2 = 3
print(Num1 | Num2)

# Output: 15

A = 7 
B = 15

print(A|B)

# Output 15

# Why Because 

# A New Property of OR

# If every 1 bit of B is already present in A, then:

# A | B = A

# Example:

# 15 | 7 = 15

# because:

# 15 = 1111

# 7 = 0111

# 7 doesn't contribute any new 1s.

First_Number = 1
Second_Number = 2
print(First_Number | Second_Number)


#  XOR Operations (^) 

a = 6
b = 10
print(a^b)


# Output = 12 

# 0 1 1 0
# 1 0 1 0
# -------
# 1 1 0 0


num1 = 11
num2 = 13
print(num1 ^ num2)

# output 6


First_Num = 9
Second_Num = 12
print(First_Num ^ Second_Num)

# Output 5 

left = 14
right = 5
print(left ^ right)

# output : 11

num1 = 8
num2 = 7
print(num1 ^ num2)


a = 456
b = 456
print(a ^ b)

# Output : 0



a = 999
b = 0
print(a ^ b)

# output : 999



I = 25
J = 24
K = 17

print(I^J^K)


####################################################################################################
# Bitwise NOT (~) 

print(~1)

# output : -2


print(~10)
# output : -11


print(~11)

# output -12


print(~15)
# output : -16

print(~16)
# output : -17


print(~100)

# output : -101

print(~1001)

# Output : -1002

x = -10

print(~x)

# Substitute it into the formula:

# ~(-10)

# = -((-10) + 1)

# = -(-9)

# = 9

Result = ~~10
print(Result)

# output : 10


Final = ~~1
print(Final)

# output : 1 


Number = ~-10
print(Number)

# output : 9


#################################################################
# left shift <<
































































































































####################################################################################################
# Right Shift >>

































# | Problem                                                     | Operator |
# | ----------------------------------------------------------- | -------- |
# | 1. Check whether a number is odd or even                    | ?        |
# | 2. Multiply a number by 8                                   | ?        |
# | 3. Divide a number by 4                                     | ?        |
# | 4. Turn ON the last bit                                     | ?        |
# | 5. Turn OFF the last bit                                    | ?        |
# | 6. Toggle the last bit                                      | ?        |
# | 7. Find the difference between two numbers at the bit level | ?        |
# | 8. Check whether the 3rd bit is ON                          | ?        |






a = 17
if a & 1:
    print("1")
else:
    print("0")
# Output 1  (Means Odd)
    
    
N = 13
print(N<<1)
 # output 26
 
Num=  9
print(Num<<8)



 
Number = 30
print(Number>>4)