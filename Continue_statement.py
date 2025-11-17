"""Terminates execution in the current iteration & continues execution 
    of the loop with the next iteration."""

i = 0
while i<= 5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1
print("----------------------------------------")

#Even numbers
s = 1
while s<=10:
    if (s%2==0):
        s+=1
        continue
    print(s)
    s+=1
print("-----------------------------------------")

#Odd numbers
v = 1
while v<=10:
    if (v%2!=0):
        v+=1
        continue
    print(v)
    v+=1
