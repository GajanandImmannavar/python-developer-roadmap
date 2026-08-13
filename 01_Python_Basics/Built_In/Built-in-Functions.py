# print()

# Num = 1
# print(Num)



# x = 1
# y = x
# print(y)
# print(x)


# Input 

# Age = input("Enter Age: ")
# print("Gajanand is  " + Age + " Years Old")


# print("Age Is=" +str(25))


Name =input("Enter Your Sweet Name: ")
PetName = input("Enter Your Pet Name If You have ")
Age = input("Enter You Age to make sure whether your eligible for ticket or not: ")

print("About Candidate : " +Name+ "  and Pet Name is  " +PetName+ " and  " +Age+ " Years Old" )
# print("Pet Name " +PetName)
# print("Age is " +Age)


# Type function

a = 22
print(type(a))

b = str(a)

print(type(b))

Name = "Gajanand"
Ages =[[1,2],[3,4],[5,6]]
Usn = [1,2,3,4]
dict ={"Name": "Gajanand", "Age": 22}
Majority = ((1,2,3,4,5))
print(type(Name))
print(type(Ages))

print(type(Usn))
print(type(dict))
print(type(Majority))



# bool() function 

x = 10
print(bool(x))

# Output: True
# Because the integer is not zero, it returns True.




Name = "Gajanand"
print(bool(Name))

# Output: True
# Because the string is not empty, it returns True.


Age = 12
My = 13
print(bool(Age>My))

# Output: False
# Because the condition is not satisfied, it returns False.


list1 = [1,2,3,4,5]
print(bool(list1))

# Output: True
# Because the list is not empty, it returns True.






name =" "
print(bool(name))
# Output: True 
# Because the string is not empty, it returns True. and Whitespaces are also considered as a character in Python. 
# So, it returns True.





# list()  function 


Name = "Gajanand"
iterable = list(Name)
print(iterable)

# Output: ['G', 'a', 'j', 'a', 'n', 'a', 'n', 'd']
# Because the string is iterable, it returns a list of characters in the string.

Number = 12345
iterable = list(str(Number))
print(iterable)

# Steps 
# 1: Convert the integer to a string using str(). 
# Because integers are not iterable, we need to convert it to a string first.
# 2: Then, we can use the list() function to convert the string to a list of characters.
# Each character in the string will become an element in the list.
# Output: ['1', '2', '3', '4', '5']


dict = {"Name": "Gajanand", "Age": 22, "Mobile_No": 8660264369}

List = list(dict.values())# .values() method returns a view object that displays a list of all the values in the dictionary.
List1 = list(dict)  # list(dict) == list(dict.keys()) It will return a list of all the keys in the dictionary.
print(type(List))
print(List1)
print(List)

# <class 'list'>
# ['Name', 'Age', 'Mobile_No']
# ['Gajanand', 22, 8660264369]




data = (1,2,3,4)
# data[0] = 10 # why Not Possible because tuple is immutable
print(type(data))
List = list(data)
List[0] = 10 # Before converting to list, we cannot change the value of tuple because tuple is immutable but after converting to list, we can change the value of list because list is mutable.
print(List)

# Output: <class 'tuple'>
# [10, 2, 3, 4]





# Set () function

Ages = {11,12,22,32,42,52,62,72,82,92}
# Ages[0] = 10 # why Not Possible because set is mutable but it does not support indexing
Ages.add(10)  # 
print(type(Ages))
List = list(Ages)
List[0] = 10
print(List) # Order of elements in the list may not be same as the order of elements in the set because set is unordered collection of elements.

# Output: <class 'set'>
# [10, 72, 42, 11, 12, 10, 82, 52, 22, 92, 62]


 # Print each set element

numbers = {10,20,30,40,50}
print(type(numbers)) 
print(numbers) # set are unorder Elements no guarrent of sequences

# Addding new element using .add

Numbers = {1,2,3,4,5}
Numbers.add(10)
print(Numbers)



# Add Duplicate
# A set automatically ignores duplicates.
Sets = {1,2,3,4,5}
Sets.add(1)
print(Sets) 

# Remove an Element

Usns = {1101, 2002, 3003, 1110}
Usns.remove(1101) # ⚠️ remove() gives an error if the element doesn't exist.
print(Usns)

# . discard()

Sequences = {400, 401, 402, 403, 404, 405, 406}
Sequences.discard(400) # discard() no error if missing
print(Sequences)

# Membership
# Check if Element Exists

Users = {101, 102, 103, 104, 105, 106}
print(101  in Users) # True ( in, not in both are membership Operators to check whether is it exist or not)
print(10001 not in Users) # true




# set Size

Numbers = {1,2,3,4,5,8}
Length = len(Numbers) # len() is built-in function to check length of datatype
print(Length) 
# Output 6


# Union
# Combine both sets.

A = {1,2,3,4,5}
B = {6,7,8,9,0}
print(A | B)
# or:
print(A.union(B))


# Intersection
# Find common elements.

P = {1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1}
Q = {1, 10, 20, 30, 40, 6}
print(P & Q) # & gives comman elements from both sets A AND B → common
# OR
print(P.intersection(Q))


# Difference
#  Elements in A but NOT in B.

M = { 101, 102, 103, 104, 105}
N = {101, 106,107,108}

print(M - N ) # {104, 105, 102, 103}   Elements in M but not in N
print(N-M) # {106, 107, 108} Elements in N but not in M


# Symmetric Difference
# Elements that are in either A or B, but not both.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print( A ^ B) #  {1, 2, 3, 6, 7, 8} A only + B only Elements that are in either A or B, but not both.

# Set Relatiship Operations
# Check Subset

A = {1,2,3,4,5}
B = {1,2,3}
print(B.issubset(A)) # Every element of B exists in A.






