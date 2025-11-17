# List operations
# Mutable / changeable
"""Built in data type that stores set of values it can store
   elements of different types (integers, float, string, etc.)"""

student = ["Sakshi", 78.4, 48, "Kolhapur"]
print(len(student))

print("----------------------indexing---------------------")
print(student[2])
print(student)

student[2]="Saku" #Mutable
print(student)

marks = [26,34,67,87,76]

print("-----------------------slicing----------------------")
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

print("-----------------------2D list----------------------")

l3 = [[4,5],5,[6,9]]

print(l3[0][1])
print(l3[-1][-1])

print("-------------------------3D list---------------------")

l4 = [[[4,5],5,[6,9]],[2,4]]

print(l4[0][2][-1])