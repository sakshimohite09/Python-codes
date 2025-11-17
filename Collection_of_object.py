#Collection of object

class Customer:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def intro(self):
        print("I am",self.name,"and I am",self.age)

c1 =Customer("Sakshi",20)
c2 =Customer("Diksha",21)
c3 =Customer("Swara",14)

L=[c1,c2,c3] # <--- Collection of object
for i in L:
    i.intro()