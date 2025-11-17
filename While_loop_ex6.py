""" Write a program to find the sum of first n natural numbers"""

n = int(input("Enter a limit:"))
sum = 0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum is:",sum)