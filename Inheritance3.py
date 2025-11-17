#MULTIPLE INHERITANCE

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


print("----------------------------------------------------------------")


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand =brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Product:
    def buy(self):
        print("Product by method")

    def review(self):
        print("Customer review")

class SmartPhone(Product,Phone): 
    pass

s= SmartPhone(20000,"Apple",12)
s.buy() # MRO (Method resolution order) = It depends on which class you inherited 1st
s.review()