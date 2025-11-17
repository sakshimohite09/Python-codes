#Modules

"""Consider a module to be the same as a code library.
   - A file containing a set of functions you want to include in your application
   Examples of python modules:
   1. Math
   2. Random
   3. os
   4. time"""

#print(help('modules'))

print("------------------------math-----------------------")
import math
print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.ceil(6.4))
print(math.floor(6.4))
print(math.sqrt(100))

print("------------------------random-----------------------")
import random
print(random.randint(1,100))

a = [1,2,3,4,5]
print(random.shuffle(a))

print("------------------------time-----------------------")
import time
print(time.time())
print(time.ctime())

print("Hello")
time.sleep(1)
print("World")

print("------------------------os-----------------------")
import os
print(os.getcwd())
print(os.listdir())