# Dictionary operations
"""Dictionaries are used to store data values in key:value pairs.
    They are unordered, mutable, & don't allow duplicate keys"""

info = {
    "Key":"value",
    "Name":"sakshi mohite",
    "Age":19,
    "is_adult":True,
    "Marks":94.4,
    "Sub":("python","C","Java","HTML"),
    12.67:897
}

print("-----------------Accesing items-----------------")
print(info)
print(info["Name"])
print(info["Sub"])

print("-----------------Reassign------------------")
info["Name"] = "Saku" 
print(info)

print("---------------------Null dictionary--------------------")
null_dict = {}
null_dict["Name"] = "Sakshi"
print(null_dict)

print("------------------------Nested dictionary-----------------------")

stu = { 
    "name":"V",
    "sub":{
        "phy":67,
        "chem":89,
        "math":78
    }
}
print(stu["sub"]["math"])

print("----------------------2D dictionary---------------------")

d1 = {"Name":"Sakshi","marks":{'m1':'90','m2':'89'}}
print(d1)

print(d1['marks']['m1'])
