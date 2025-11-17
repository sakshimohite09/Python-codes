# Write a program to find the factorial of n. (n is the parameter)
n = int(input("Enter a number:"))
def cal_fact(n):

    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(n)