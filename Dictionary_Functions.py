stu = { 
    "name":"V",
    "sub":{
        "phy":67,
        "chem":89,
        "math":78
    }
}

print(stu.keys()) #Returns all keys

print(list(stu.keys())) 

print(len(stu)) # length of dict

print(list(stu.values())) # Returns all values

print(list(stu.items())) # Returns all (key,val) pairs as tuples

print(stu["name"])

print(stu.get("name")) # Returns the key according to value

stu.update({"City":"Kolhapur"}) # Inserts the specified items to the dictionary 
print(stu)