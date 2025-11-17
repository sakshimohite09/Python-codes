#Private(like) attributes & methods (__)
#Conceptual implementation in python

"""Private attributes & methods are meant to be used only within the class and
     are not accessible from outside the class."""

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())
print(p1.__name)    #It shows error

print(p1.__hello())     #It shows error