"""Write a program to find the factorial of first n numbers"""

n = int(input("Enter a limit:"))
fact = 1
i=1
while i<=n:
    fact*=i
    i+=1
print("Factorial is:",fact)