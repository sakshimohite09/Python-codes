"""Search for a number x in this tuple using loop.
    [1,4,9,16,25,36,49,64,81,100]"""

lst = [1,4,9,16,25,36,49,64,81,100]

i = 0
for ele in lst:
    if(ele == 16):
        print("number found at index",i)
    i+=1
    