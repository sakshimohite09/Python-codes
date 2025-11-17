#Lambda function

x = lambda x:x**2
print(x(4))

a = lambda x,y:x+y
print(a(4,5))
print(type(a))

b= lambda x:x[0]=='a'
print(b('apple'))
print(b('banana'))

print("-------------Even-odd------------")

b= lambda x:'Even'if x%2==0 else 'Odd'
print(b(4))
print((b(3)))

