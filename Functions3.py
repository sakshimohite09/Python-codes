# Map function = Works on every item
print("---------------------Map function----------------------")

L=[1,2,3,4,5,6,7]
print(list(map(lambda x: x*2,L)))
print(list(map(lambda x: x%2==0,L))) #Even-odd

stu = [{'name':'sakshi mohite',
        'father name':'sudhir mohite',
        'add':'puikhadi'},
        {'name':'diksha patil',
         'father name':'maruti patil',
         'add':'koparde'},
         {'name':'asmita nilange',
          'father name':'omprakash nilange',
          'add':'nanded'}]
print(map(lambda stu: stu['name'],stu))
print(list(map(lambda stu: stu['name'],stu)))

# Filter function = Works on only condition
print("---------------------Filter function----------------------")

L=[1,2,3,4,5,6,7]
print(list(filter(lambda x:x>4,L)))

fruits=['apple','orange','mango','guava']
print(list(filter(lambda fruit:'e'in fruit,fruits)))

#Reduce function = reduces the list 
print("---------------------Reduce function----------------------")

import functools
L=[1,2,3,4,5,6,7]
print(functools.reduce(lambda x,y:x+y,L))

L1 = [34,11,65,34,98,66]
print(functools.reduce(lambda x,y:x if x>y else y ,L1))
print(functools.reduce(lambda x,y:x if x<y else y ,L1))

