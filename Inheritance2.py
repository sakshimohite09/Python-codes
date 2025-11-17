#MULTILEVEL INHERITANCE

class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


print("----------------------------------------------------------------")


class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__pricw =price
        self.brand =brand
        self.camera =camera

    def Buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000,"Apple",12)
p=Phone(10000,"Samsung",1)

s.Buy()
s.review()
p.review()


print("----------------------------------------------------------------")


class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
    
class C(B):
    def m2(self):
        return 20
    
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj3.m1()+obj3.m2()) #20+30+20 =70