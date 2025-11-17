lst = [2,1,3,4,5]
lst2 = ["a", "b", "c", "d", "e"]
list3 = list("Sakshi") #We can crete list by using functions

print(list3)

print(len(lst))

print(min(lst))

print(max(lst))

print(sorted(lst))

print(sorted(lst, reverse = True))

print(lst.index(4))

print("-------------------------------------------------------------")

lst.append(6) #Adds one element at the end
print(lst)

lst.extend([500,400,800]) #Adds many elements at the end
print(lst)

lst.insert(1,7) #Insert element at index
print(lst)

lst.sort() #Sorts in ascending order
print(lst)

lst2.sort(reverse =True) #Sorts in descending order
print(lst2)

lst2.extend("goa") # it adds list at the end 
print(lst2)

lst2.reverse() #Reverse list
print(lst2)

lst.remove(5) 
print(lst)

lst.pop(3) 
print(lst)

del lst[0]
print(lst)

lst.clear() #clear whole list
print(lst)

print("=-------------------------------------------------------")

sample = "how are you?"
print(sample.split())
l=[]
for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())
print(l)
print(" ".join(l))

print("--------------------------------------------------------")

sample = "sakshi@yahoo.com"
print(sample[:sample.find("@")]) #Print elements which are before @
l1 = [1,1,2,2,3,3,4,4]
l2 = [1,2,3,1]
l =[]
for i in l1: # or l2
    if i not in l:
        l.append(i)
print(l)