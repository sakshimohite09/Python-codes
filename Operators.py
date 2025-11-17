"""Operators: Operators are used to perform operations on variables and values. 

    1. Arithmetic operators
    2. Comparison operators
    3. Logical operators
    4. Bitwise operators
    5. Assignment operators
    6. Identity operators
    7. Membership operators"""

a = 5
b = 2

print("-------------------------1. Arithmetic operators----------------------------")

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)   #a^b
print(a // 2)   #Integer division

print("-------------------------2. Comparison operators----------------------------")

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

print("-------------------------3. Logical operators----------------------------")

x = True
y = False
print(x or y)
print(x and y)
print(not x)

print("-------------------------4. Bitwise operators----------------------------")

x = 2
y = 3
print(x & y)
print(x | y)
print(x >> 2)
print(y << 3)
print(~x)


print("-------------------------5. Assignment operators----------------------------")

num = 10
num = num + 10 #10+10=20
print("Num: ",num)
no = 20
no += 10
print("Num: ",no)
c = 20
c -= 10
print("Num: ",c)
d = 20
d *= 10
print("Num: ",d)
e = 20
e /= 10
print("Num: ",e)
f = 20
f %= 10
print("Num: ",f)
g = 20
g **= 2
print("Num: ",g)

print("-------------------------6. Identity operators----------------------------")

a = 3 
b = 3
print(a is b)

x = [1,2,3]
y = [1,2,3]
print(a is b)
print(a is not b)

print("-------------------------7. Membership operators----------------------------")

x = "delhi"
print("D" not in x)
print("d" in x)

x = [1,2,3]
print(1 in x)