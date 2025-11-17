collection = set()

collection.add(1) #Adds an elements
collection.add(2)

collection.remove(1) #Remove

collection.add("Sakshi")

collection.add((4,5,6))

print(collection)
collection.clear() #Empties the set

print(len(collection)) # Length

set1 = {"Hello","Sakshi","Sudhir","Mohite"}

print(set1.pop()) # Removes a random value

set2 = {1,2,3}
set3 = {4,5,3}

print(set2.union(set3)) # Combines both the values & returns new

print(set2.intersection(set3)) #Combines common values & returns new
