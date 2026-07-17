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

