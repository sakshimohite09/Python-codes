# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameter.

def lst(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    lst(list, idx+1)

fruits = ["Mango","Litchi","Apple","Banana"]

lst(fruits)