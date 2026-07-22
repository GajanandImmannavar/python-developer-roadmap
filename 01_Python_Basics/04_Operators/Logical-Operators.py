# Internal Working 
# Step 1: 10>2--------->True  
# Step 2: 10 == 12-----> False
# Step 3: True and False = False (According to Truth Table )

print(10>2 and 10==12)





# Example 2:
# True is Boolean Object = True 
# False is Boolean Object = False
# True AND False = False (Because Truth Table Says True AND True = True remaining are False)

print(True and False)








# Example 3:

print(True and False)
# output: False




# Example 4:

print(False and True)

# output : False 


# Example 5:

print(False and False)
# output: False



# Example 6:

print(10 > 5 and 8 > 2)

# output: True

# Example 7:

print(5 == 5 and 10 != 10)
# output: False



# Example 8:

print(20 >= 20 and 15 <= 15)
# output: True


# Expression 1 → Boolean result
# Expression 2 → Boolean result
#               ↓
#            AND operator
#               ↓
#         Final Boolean result



# Example:

# x > 5 and y < 10

# Python conceptually does:

# x > 5
# ↓
# True / False

# y < 10
# ↓
# True / False

# True/False and True/False
# ↓
# Final True/False

#######################################################################################################
# 🐍 Logical Operator: and — Level 2

# For now, remember:

# Empty → Falsy
# Zero → Falsy
# False → Falsy
# None → Falsy

# Non-empty → Truthy
# Non-zero → Truthy
# True → Truthy



# Truthy and Falsy — Beginner Explanation

# Imagine Python asks every value one simple question:

# "Should I treat you like True or False?"

# Python internally does something similar to:

# bool(value)

# 1. Basic Example
x = 10

print(bool(x))

# Output:

# True

# Why?

# Because 10 is a non-zero number.

# 10 → Truthy

# Now:

x = 0

print(bool(x))

# Output:

# False

# Why?

# Because 0 represents no value/zero quantity.

# 0 → Falsy
# 2. The Basic Rule

# For numbers:

# 0       → Falsy
# Any other number → Truthy

# Examples:

# bool(0)       # False
# bool(1)       # True
# bool(10)      # True
# bool(-10)     # True
# bool(3.14)    # True
# bool(0.0)     # False

# Think:

# Zero     → False
# Non-zero → True
# 3. Strings

# Now:

# name = ""
# print(bool(name))

# Output:

# False

# Why?

# Because the string is empty.

# "" → contains 0 characters → Falsy

# But:

# name = "Python"
# print(bool(name))

# Output:

# True

# Why?

# Because it contains characters.

# "Python" → contains characters → Truthy
# Very Important Difference
# bool(0)

# Output:

# False

# But:

# bool("0")

# Output:

# True

# Why?

# 0
# Integer
# Value = zero
# Falsy
# "0"
# String
# Contains one character: 0
# Non-empty
# Truthy

# Python does not look at the meaning of the character "0".

# It only asks:

# Is the string empty?

# 4. Lists
# items = []

# print(bool(items))

# Output:

# False

# Why?

# The list contains nothing.

# [] → empty list → Falsy

# Now:

# items = [10]

# print(bool(items))

# Output:

# True

# The list contains one item.

# [10] → non-empty list → Truthy

# Even:

# items = [0]

# print(bool(items))

# Output:

# True

# This is important.

# The list is not empty.

# So:

# [0] → Truthy
# 5. Simple Mental Model

# For containers such as:

# String
# List
# Tuple
# Dictionary
# Set

# Python asks:

# Is it empty?

# Empty       → Falsy
# Not empty   → Truthy

# Examples:

# ""      → Falsy
# "Hi"    → Truthy

# []      → Falsy
# [0]     → Truthy

# ()      → Falsy
# (0,)    → Truthy

# {}      → Falsy
# {"a":1} → Truthy
# 6. The and Connection

# Now let's connect this to the previous topic.

# Example 1
print(10 and 20)

# Python checks the first value:

# 10

# Question:

# Is 10 truthy?

# Yes.

# So Python goes to the second value:

# 20

# Result:

# 20

# # So:

# 10 and 20 → 20

###################################################################################

print(bool(5))

# output True 

# Because:

# 5 ≠ 0

# All non-zero numbers are truthy.




print(bool(0))

# output False
# Because 0 → Falsy




print(bool(""))

# output  False
# "" → Empty String → Falsy




print(bool("0"))

#output True 





print(bool([]))

# Output False 





print(bool([0]))

# output True 





# 🔴 Falsy Values


# | Value   | Type             |
# | ------- | ---------------- |
# | `False` | bool             |
# | `None`  | NoneType         |
# | `0`     | int              |
# | `0.0`   | float            |
# | `0j`    | complex          |
# | `""`    | empty string     |
# | `[]`    | empty list       |
# | `()`    | empty tuple      |
# | `{}`    | empty dictionary |
# | `set()` | empty set        |

# Truthy Values


# True
# 1
# 10
# -1
# 3.14
# "Python"
# " "
# [1]
# [0]
# (1,)
# {"a": 1}
# {1}

# Rule:
# 0 → Falsy
# Any non-zero number → Truthy

# So:

# 0       → False
# 1       → True
# -1      → True
# 100     → True
# -999    → True  
##########################################################################################################################

# Float Values

print(bool(0.0))

# output False

print(bool(3.14))

# output True

print(bool(-2.5))

# output True
#########################################################################################################

# Strings

print(bool(""))

# output  False

# Non-Empty String

print(bool("Python"))

# output True


print(bool("0"))

# output True

#########################################################################################################


# Spaces

print(bool(" "))

#  output  True  Space consider as character 


# ""   → 0 characters → Falsy
# " "  → 1 character  → Truthy

#########################################################################################################

# Lists

print(bool([]))

# output False

print(bool([1]))

# output True 

print(bool([0]))

# output True

#######################################################################################################

# Tuples

print(bool(()))

# output False

print(bool((1,)))

# output True

############################################################################################

# Dictionaries

print(bool({}))

#output False

print(bool({"name": "Gajanand"})) 

# output True


###################################################################################################

# Sets


print(bool(set()))

# output False



print(bool((1,2,3)))

# output True


#########################################################################################################

# Logical AND


print(10 and 20)

# Python checks:

# 10

# Is 10 falsy?

# No

# Therefore Python returns the second operand:

# 20

# Final output:
# 20

# output 20




print(0 and 20)

# output 0



print(5 and 0)

# output 0




print(-10 and 100)

# out put 100


print([1,2] and [1,2,3,4])

# output : [1,2,3,4]

print([] and [1, 2, 3])
# Output : []



#################################################################################################

# Or Logical Operator



print(True or False)

# out put True Because Or find True Value  and return if there is no true value  it returns False as Output


print(True or True)

# output True  Because First value is True and  either is true  and  if first value is true or integer(1,2,3,4...) python doesn't check next value it return first value instead of checking  second value 



print(False or True)

# output  : True  


print(False or False)

# output : False



print("" or "Gajanand")

# output : Gajanand because first string is empty so second string contains Gajanand 


print(" " or "Hi")

#output : Nothing you will not get anything as output because 
# first string has white space and python consider whitespace as a value  so python return nothing even though 
# having value in second  string 



print(10>12 or 10<8)

# output: False 


print(10 or 20)

# output: 10





##################################################################################################

# Not Operator  

# Simple Rule
# If a value is Truthy, not returns False.
# If a value is Falsy, not returns True.

print(not True)

# Output False 

print(not False)

# output : True 


print(not 0)

# output : True  

print(not 10)


# output False 


print(not "")

# out-put: True  


print(not "Python")

# out-put: False

print(not [])

# Output : True


print(not [0])

# output: False


print(not (10 > 5))

# output False  


print(not (10 < 5))

# output : True 
