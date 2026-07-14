# Example 1: Addition of Two Integers

# Python creates Integer Objects for 10 and 20.
# Variables 'a' and 'b' store references to those objects.
# When 'a + b' is executed, Python adds both Integer Objects,
# creates a new Integer Object (30), and stores its reference in 'c'.

a = 10
b = 20
c = a + b
print("Addition of two Number")
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
print("Addition of an Integer and a Float")
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

print("Addition of Two Floating-Point Numbers")
print(f"{c}\n")

# Output
# 31.0

#  Example 3: Addition of integer and floating point numbers 
#  python creates an integer object for a and floating point for b  
#  before adding python ask can i add integer and floating point number 
#  yes why because we have learnt  Python Implicit type casting  Python automatically convert int to float 
#  but original value remains same (Remember)
#  than python adds both and Create new floating point object for c and result get assign to c
#  Python return final Result C

a = 10
b = 20.5
c = a + b
print("Addition of integer and floating point numbers")
print(c)

# Output
# 30.5
