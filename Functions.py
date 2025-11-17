"""Block of statements that perform a specific task"""

#Function definition
def cal_sum(a,b):       #Parameter
    sum=a+b
    print(sum)
    return sum
cal_sum(2,3)          #Function call
cal_sum(8,7)           #2,3,8,7 are arguments 

print("------------------------")

def cal_sum(x,y):
    return x+y
print(cal_sum(8,9))

print("------------------------")

def hi():
    print("Hello")
hi() 
hi()

print("------------Built in functions = print(),len(),type(),range()-------------")

print("Sakshi",end=" ")
print("Mohite")

print("------------User defined function-------------")