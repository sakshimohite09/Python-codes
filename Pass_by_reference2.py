def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 =[1,2,3,4]
print(id(L1))
print(L1)

change(L1[:]) #Cloning function = Makes copy 
print(L1)

print("---------------------------------")

def chang(K):
    print(id(K))
    K= K+(5,6)
    print(id(K))

K1 =[1,2,3,4]
print(id(K1))
print(K1)

chang(K1) #Cloning function = Makes copy 
print(K1)