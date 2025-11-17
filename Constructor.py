""" All function have a function called _init_(),
    which is always executed when the class is being initiated."""

class Student:

    #Default constructors
    def __init__(self):
        pass

    #Parameterized constructors
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks      #Attributes
        print("Adding new student in database..")

s1 = Student("Sakshi",98)
print(s1.name, s1.marks)

s2 = Student("Diksha",95)
print(s2.name, s2.marks)

"""The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class"""