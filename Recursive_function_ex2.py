print("----------------Factorial-----------------")

def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

print(fact(2))
print(fact(4))
print(fact(6))

print("----------------Palindrome----------------")

def palin(text):
    if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("Not a palindrome")
palin("madam")
palin("malayalam")
palin("python")

print("---------------1. Fibonacci-----------------")

def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1) +fib(m-2)   
print(fib(12))

print("---------------2. Fibonacci(Memoization)-----------------")

import time
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d) + memo(m-2,d)
        return d[m]
start = time.time()
d = {0:1,1:1}
print(memo(500,d))
print(time.time()-start)
print(d)