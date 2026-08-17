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
        "Educaion": "BE",
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

# print("-------Whole Content Of Dictionary--------\n")
# print(f"{Personal_Data}\n")

# print(f"{Personal_Data['About']}\n")


# print(f"{Personal_Data['About']['Stream']}\n")

# print(f"{Personal_Data['Family']['Parents']}\n")


print(Personal_Data.get('About'))
print(Personal_Data.get('About').get('Stream'))

Salary = Personal_Data.get("About",{}).get("Salary",0)
print(Salary)



# Personal_Data["About"]["Address"]= "Dist Bagalakot Tq Mudhol 587313"

print(Personal_Data.get("About"))



Personal_Data["About"]["Address"] = "Dist: Bagalakot Tq: Mudhol ATPost: Ingalagi 587313"




print(Personal_Data.get("About",{}).get("Address"))


del Personal_Data["About"]["Address"]



print(Personal_Data)
