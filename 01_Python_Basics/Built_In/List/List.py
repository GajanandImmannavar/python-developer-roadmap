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











