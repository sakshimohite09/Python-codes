#Static methods = methods that don't use the self parameter (work at class level)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name,"Your avg score is:",sum/3)

s1 =Student("Sakshi",[89,99,90])
s1.avg()
s1.hello()

s1.name = "Sak" #Name change
s1.avg()

"""Decorators allow us to wrap another function in order to extend the
    behaviour of the wrapped function, without permanently modifying it."""