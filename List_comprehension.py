# List comprehension

L=[1,2,3,4,5,6,7]
L1 = [item *2 for item in L]
print(L1)

L2 = [i**2 for i in range(10)]
print(L2)

L3 = [i**2 for i in range(10) if i%2!=0]
print(L3)

fruits=['apple','orange','mango','guava']
L4 = [fruit for fruit in fruits if fruit[0]=='o']
print(L4)

D={'name':'nitish','gender':'male','age':30}
print(D.items())

D1={key:value for key,value in D.items() if len(key)>3}
print(D1)