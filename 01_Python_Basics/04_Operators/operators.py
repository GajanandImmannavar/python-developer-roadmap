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
print("-----------------------------------------")
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



# (Subtraction After Implicit Type Casting) This trap no need to worry about this, we learnt python convert int to float there self
Num_A = 1000
Num_B = 101.1
Result = Num_A - Num_B
print("Example 5: Subtraction After Implicit Type Casting")
print(f"{Num_A} - {Num_B} =")
print(f"{Result}\n")