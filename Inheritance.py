"""When one class(child/derived) devices the properties & methods of
    another class(parent/base)."""

#SINGLE INHERITANCE

class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
car1.start()


print("----------------------------------------------------------------")


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self._price =price
        self.brand =brand
        self.camera =camera

    def buy(self):
        print("Buying a phone")
    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(1000,"Apple","13px").buy()