# String operations
#immutable / Unchangeable
# String is data type that stores a sequence of characters

str1 = "Sakshi"
str2 = ' Mohite'

print(str1+str2) # Concatenation
print(len(str1)) #length of string
print(len(str2))
str="Sakshi Mohite"

print("------------------Indexing--------------------")
print(str1[4])  #Positive indexing
print(str[-1])  #Negative indexing

print("---------------------Slicing-------------------")
print(str[1:4]) # Include 1 exclude 4
print(str[5:]) # [5:len(str)]
print(str[:5]) # [0:4]
print(str[-3:-1]) # len(str)-3 : len(str)-1
print(str[2:6:2]) 
print(str[-5:-1:2])
print(str[::-1]) #Reverse string
print(str[-1:-5:-1])

print("------------------Multiline string----------------")
a = """Sakshi
Sudhir
Mohite"""
print(a)
