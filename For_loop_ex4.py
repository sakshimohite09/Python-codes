"""Write a program to find the factorial of first n numbers"""

n = int(input("Enter a limit:"))
fact = 1

for i in range(1,n+1):
    fact*=i
print("Factorial is:",fact)