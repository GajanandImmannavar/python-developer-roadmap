#----------------------------()()()()-------------------------------------------------------
# Append() Method

List = [1,2,3,4,5]

List.append(1) # Important: append() modifies the original list

print(List)


Result1 = [100,98, 99, 100, 100, 100]

Final = Result1


Final[1] = 100

print(Final)
print(Result1)


Final.append(100)

print(type(Final))

print(len(Final))

print(Final)




Usns = [101, 102, 103, 104, 105 ]

finallist = Usns.append(106)  

print(finallist)

# output 
# None

# Because 
# append()
#    ↓
# modifies list
#    ↓
# returns None


# append() adds exactly ONE element


Numbers = [10001, 1002, 2002, 222,520]

Updated_List = Numbers.append([1,2,3,4])

print(Updated_List) # output None append returns none 

print(Numbers)

#------------------------------------()()()()----------------------------------------

# Extend method()

# extend() adds multiple elements from an iterable.

Marks = [1,2,3,4,5,6]

Marks.extend([1,2,3,4,5,6])

print(len(Marks))
print(Marks)

# Memory trick
# append()
#    ↓
# ONE element


# extend()
#    ↓
# ELEMENTS from iterable

# extend() works with strings


String = ["A", "B", "C", "D"]

String.extend("EF")

print(String)


#---------------------------------()()()()()----------------------------------------
# Insert Method
# Adds an element at a specific index.

Flames = [1,2,3,4,5,6,7,8,9,0]

Result = Flames.insert(10, 10)

print(Flames)

# ---------------------------------()()()())()--------------------------------------
# remove()
# Removes the first occurrence of a value.
# Important
# remove() searches by value, not index.

Numbers = [1,1,2,2,3,3,4,4,5,5,6,6]

Numbers.remove(1)

print(Numbers)

#------------------------------------()()()()---------------------------------------------

# pop()

Numbers = [10,20,30,40,50,60]

print(f"{Numbers}\n")
Updated = Numbers.pop()


print(f"Poped Element is : {Updated}\n")
print(Numbers)

# pop(index)

# You can specify an index.

Indexed_pop = Numbers.pop(4)

print(Indexed_pop)


# clear()  

Name = ["Gajanand", "Akash", "Veeresh", "Chandrashaker"]

print(Name)

Name.clear()

print(Name)

#------------------------------------()()()()-------------------------------------------
# index() 

# Finds the index of the first occurrence of a value.


Heights = [10, 12, 11, 8, 9, 10]

Result = Heights.index(10)

print(Result) # 0 


# index() with start

Result1 = Heights.index(10,2)

print(Result1) # output 5 Find 10 starting from index 2.


# index() with start and stop

Integers = [2,3,4,5,1,2,3,4,5]

Findings = Integers.index(1,0,5)

print(Findings) # output 4 because 1 in 4th index index search number from 0 to 5 if found return else raise value error

# General syntax:

# list.index(value, start, stop)

 #--------------------------------------------------()()()()-------------------------------

#  count() 
# count how many time value appears

Sequences = [1,2,3,4,5,6,7,1,8,4,2,6,7,1,8,9,3,5,6,7,3]

Repeated_Number = Sequences.count(1)

print(Repeated_Number)

#------------------------------------------()()()()----------------------------------------
# sort()

Natural_Numbers = [100, 1001, 1, 65, 23, 89, 56, 24, 99, 0, 1002]

Natural_Numbers.sort(reverse=True) # descending order 

print(Natural_Numbers)

Natural_Numbers.sort()

print(Natural_Numbers)


# Important: sort() returns None
# numbers = [3, 1, 2]


# result = numbers.sort()


# print(result)

# Output:

# None

# Remember:

# sort()
#  ↓
# modifies original list
#  ↓
# returns None


# ---------------------------------------------------()()()()-----------------------------

# reverse()
# Reverses the list in place.

numbers = [11, 2, 34, 10]
numbers.reverse()
print(numbers)


#---------------------------------------------()()()()-------------------------------------

# copy

# Creates a shallow copy of the list.

A = [1,2,3,4]
B = A.copy()

print(B)

B.append(10)

print(B)

# output
# [1, 2, 3, 4]
# [1, 2, 3, 4, 10]

#Now conceptually:

# numbers      → List A
# new_numbers  → List B
# 
# They are separate list objects.


#-------------------------------------()()()()()()----------------------------------------------





# Indexing() 

# numbers[1]
# means:

# Give me the value stored at index 1.

# It does not mean:

# Find the value 1.

# Index Formula

# For a list with length n:

# Positive indexes
# 0 → n - 1

Array = [12,13,14,12,13,14,15,16,17,18]

print(Array[0])
print(Array[1])
print(Array[3])
print(Array[4])
print(Array[5])

# Negative indexing
# Negative indexes
# -n → -1

Numbers = [101, 102, 103, 104, 105, 106, 107, 108]

print(Numbers[-1])

# indexing tuple

data = (1,2,3,45,6,7,8,9,0,)
print(type(data))
print(data)

print(data[1])
print(data[-1])

# The important difference is not indexing.

# Both list and tuple support indexing.

# The major difference is:

# List   → mutable
# Tuple  → immutable

# | Data structure | Indexing   |
# | -------------- | ---------- |
# | List           | ✅          |
# | Tuple          | ✅          |
# | String         | ✅          |
# | Set            | ❌          |
# | Dictionary     | ❌ by index |


# Indexing Can Be Used to Modify a List

Items = ["A", "B", "C", "D", "E"]

print(Items)

Items[0] = "Z"
Items[-1] = "Y"

print(Items)

# Indexing Nested Lists

Matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
         ] 

print(Matrix[1]) # Second row

# Two-Level Indexing
print(Matrix[0][0]) # first row first element


#  Three-Level Indexing

data = [
    [
        [10,20],
        [30,40]
    ]
]

print(data[0][1][1])


# Indexing + len()

copuns = [10123, 104563, 112896, 10856]

print(copuns[len(copuns)-1])
#----------------------------------------------()()()()----------------------------------
# Slicing

# Indexing gets one element.
# Slicing gets multiple elements from a sequence.
# list[start:stop]
# start → where to begin
# stop  → where to stop
# ⭐ Most important rule
# Start is included. Stop is excluded.



Numbers = [1,2,3,4,5,6,7]
print(Numbers[1:2]) 
# utput [2]


numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# Index:     0    1    2    3    4
# Value:    10   20   30   40   50
#                 ↑              ↑
#               start           stop
#                 │               │
#                include        exclude


# output [20, 30, 40]


# Why Is Stop Excluded?
# 
# This is one of the most important Python rules.
# 
# numbers[1:4]
# 
# means:
# 
# index 1
# index 2
# index 3
# 
# but not index 4.
# 
# So:
# 
# 1 ≤ index < 4
# 
# This makes slicing work naturally with lengths and ranges.

A = [100, 200, 300, 400,500]
print(A[0:4])

# output [100, 200, 300, 400]

# Start Can Be Omitted
# When start is omitted, Python starts from the beginning.

print(A[:3]) # means print(A[0:3])

# output [100, 200, 300]

# Stop Can Be Omitted 
#  When stop is omitted, Python goes until the end.

B = [1001, 1002, 1003, 1004, 1005, 1006]

print(B[2:])

# output  [1003, 1004, 1005, 1006]-------------------------------------------------------------

# --------------------------------------------------------------------------------------------------

# Both Start and Stop Omitted
# This selects the entire list.

nums = [1, 2, 3, 4, 5, 6]

print(nums[:])

# Important
# 
# numbers[:] creates a new list containing the same element references.
# 
# It is therefore commonly used as a shallow copy.


Threes = [123, 213, 234, 223, 212]

New_Threes = Threes[:]

print(New_Threes)

# output [123, 213, 234, 223, 212]

print(New_Threes is Threes) 



# Slicing With Negative Indexes


numbers = [10, 20, 30, 40, 50]

# Value:       10    20    30    40    50
# Positive:     0     1     2     3     4
# Negative:    -5    -4    -3    -2    -1

print(numbers[-4:-1])
# output [20, 30, 40]

# Negative Start + Positive Stop

print(numbers[-5:4])
# output  [10, 20, 30, 40]


# Positive Start + Negative Stop

print(numbers[1:-1])
# output [20, 30, 40]



Lists = [101,202, 303, 404, 505, 606]

print(Lists[:]) # all elements
# output [101, 202, 303, 404, 505, 606]



# The Third Parameter: step

L1 = [1,2,3,4,5,6]
print(L1[1:6:2]) # list[start:stop:step]

print(L1[0:3:2])
#output [1,3]


