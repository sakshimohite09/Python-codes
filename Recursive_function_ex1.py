'''Recursion function = When a function calls itself repeatedly'''

#Prints n to 1 backwards

def show(n):
    if(n == 0):  #base case
        return
    print(n)
    show(n-1)

show(5)

print("-----------------------------")

#Multiplication

def mul(a,b):
    if b == 1:
        return a
    else:
        return a + mul(a,b-1)
    
print(mul(3,6))