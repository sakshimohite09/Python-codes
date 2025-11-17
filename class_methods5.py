#class method

"""A class method is bound to the class & receives the 
    class as an implicit first argument."""

"""Note - static method can't access or modify class state & generally for utility."""

class Person:
    name = "Anonymous"

    @classmethod
    def changeName(cls , name):
        cls.name = name

n1 =Person()
n1.changeName("Sakshi")
print(n1.name)
print(Person.name)