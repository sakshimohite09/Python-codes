# METHOD OVERRIDING = buy() method is double ...but it executes buy() of child class


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class smartphone(Phone):

    def buy(self):
        print("Buying a smartphone")

s=smartphone(20000,"Apple",13)
s.buy()