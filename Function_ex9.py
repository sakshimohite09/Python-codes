"""Write a program to remove a given word from a list and strip it at the same time"""

def rem(l,word):
    n =[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry","Rohan","Sahil","an"]

print(rem(l,"an")) 


def multi(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter a number: "))
multi(n)