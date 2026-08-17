Data = {
    "Name": "Gajanand",
    "Mobile_NO": 8660264369
}

print(type(Data))
print(Data["Name"])
print(Data["Mobile_NO"])


Personal_Data = {


   "About": {
        "Name": "Gajanand",
        "Education": "BE",
        "Stream": "AIML",
        "Job": "Looking for Job",
        "Salary": ""
           },


    "Family":{
                "Parents": "Lingaraj  and Sunanda",
                "Siblings":"Gireesh And Malati",
                "Grand_Parents":"Ramappa and Gangavva"  
            }

}

print("-------Whole Content Of Dictionary--------\n")
print(f"{Personal_Data}\n")

print(f"{Personal_Data['About']}\n")


print(f"{Personal_Data['About']['Stream']}\n")

print(f"{Personal_Data['Family']['Parents']}\n")


print(Personal_Data.get('About'))

print(Personal_Data.get('About').get('Stream'))

Salary = Personal_Data.get("About",{}).get("Salary",0)

print(Salary)

Personal_Data["About"]["Address"]= "Dist Bagalakot Tq Mudhol 587313"

print(Personal_Data.get("About"))

Personal_Data["About"]["Address"] = "Dist: Bagalakot Tq: Mudhol ATPost: Ingalagi 587313"

print(Personal_Data.get("About",{}).get("Address"))

del Personal_Data["About"]["Address"]

print(Personal_Data)




print(f"{Personal_Data.keys()}\n")

for key in Personal_Data.keys():
    print(f"{key}\n")


for value in Personal_Data.values():
    print(f"{value}\n")


for value, key in Personal_Data.items():
    print(f"{value, key}\n")

print("---nested_Key-----")
for key, value in Personal_Data.items():
    print("Main key",key)
    for nested_key in value.keys():
        print("Nested_Keys", nested_key)



print ("Name" in Personal_Data["About"])


           OR

print("Grand_Parents" in Personal_Data.get("Family",{}))



print("Gajanand" in Personal_Data["About"].values())




print("Gajanand" not in Personal_Data.get("About",{}).values())


print("Education" not in Personal_Data["About"].keys())

length = len(Personal_Data)
print(length)


length_of_nested_dict = len(Personal_Data["About"])
print(length_of_nested_dict)


for x in Personal_Data:
    print(x)


for value in Personal_Data.values():
    print(value)


for key, value in Personal_Data.items():
    print(key, value)

Update Method

Personal_Data.update({
    "About":{
    "Name": "Praveen"
           }
})
      Update only Name or Specific data
Personal_Data["About"]["Name"] = "Praveen"
print(Personal_Data)


Personal_Data.setdefault("Age", 22)

print(Personal_Data)

Student = Personal_Data.copy()

print(Student)





Student1 = {
    "Name" : "Gajanand",
    "Age": 22
}

Student2 = {
    "Address": "Mudhol",
    "Pin": 587313
}



Students = Student1 | Student2

print(Students)

Learners = Students

Learners.update({
    "Name": "Gajanana"
})

print(Learners)

Tables= {}

for Number in range(1, 10+1):
    Tables[Number] = Number*Number
print(Tables)

# Dictionary 

Grocessory = {
    "Names": ["Milk","Oil"],
    "Quantity": ["2L", "1K"]
}

print(Grocessory["Names"][1])

print(Grocessory["Quantity"][0])

# Dictionary with Sets

Dict = {
    "Unique_Numbers": {
        1,2,3,4,5,6,7
    }
}


Dict["Unique_Numbers"] = 1,1,1,1,1,1

print(Dict)






# Dictionary Dsa 


Name = "Gajanand"
frequency = {}

for char in Name:
    frequency[char] = frequency.get(char,0)+1

print(frequency)



Sentence = "Hi bro how are you, i am fine bro how are?"

result = Sentence.strip()
frequency ={}
for word in result.split():
    
    frequency[word] = frequency.get(word,0)+1

print(frequency)




