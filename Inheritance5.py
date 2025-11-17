# super method = super() method is to access methods of the parent class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self , name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius","electric")
print(car1.type)


print("------------------------------------------------------")


class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand =brand
        self.camera =camera

    def buy(self):
        print("Buying a phone")

class Smartphone(phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()

s= Smartphone(20000,"Apple",13)
s.buy()


print("-------------------------------------------------------")


class phone:
    def __init__(self,price,brand,camera):
        print("Inside phne constructor")
        self.price = price
        self.brand =brand
        self.camera =camera

class Smartphone(phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os = os
        self.ram =ram
        print("Inside smartphone constructor")

s=Smartphone(20000,"Samsung",12,"android",8)
print(s.os)
print(s.brand)



print("-------------------------------------------------------")


class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
    
class child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.__val =val
    def get_val(self):
        return self.__val
    
son =child(100,200)
print(son.get_num())
print(son.get_val())


print("-------------------------------------------------------")


class Parent:
    def __init__(self):
        self.num =100
    def show(self):
        print("Parent:",self.num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10
    def show(self):
        print("Child:",self.__var)

dad=Parent()
dad.show()
son=Child()
son.show()
