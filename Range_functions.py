"""Range functions returns a sequence of numbers,
    starting from 0 by default, and increments bt 1
    (by default), and stops before a specified number.
    
    range(start?,stop,step?)"""

seq = range(10)

#1
for i in seq:
    print(i)

print("------------------")

#2
for i in range(10):
    print(i)

print("------------------")

for i in range(2,10):
    print(i)

print("------------------")

for i in range(2,10,2):
    print(i)