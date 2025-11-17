# Tuple operations
# Immutable / unchangeable
"""A built in data type that lets us create 
   immutable sequences of values"""
tup = (2,1,3,4,5)

t5 = tuple("Sakshi")
print(t5)

tup1 = ("Sakshi",23,2.3) #Heterogeeneous tuple

print("------------------------indexing--------------------------")

print(tup[0])
tup2 = ()  # Empty tuple
print(tup2)
tup3 = (1,) # "," with single element in tuple
print(tup3)

print("-------------------slicing(Similar to list)-------------------")

print(tup[2:4])

print("------------------------2D tuple--------------------------")

t4 = (1,2,3,(4,5))

print("------------------------single item tuple--------------------------")

t2 =("hello",) #by adding ","
print(t2)
print(type(t2))


