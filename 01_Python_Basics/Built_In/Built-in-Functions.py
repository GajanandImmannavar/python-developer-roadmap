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








