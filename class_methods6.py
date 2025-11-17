"""Property = We use @property decorator on any method in the class to use the method as property."""

class Stu:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def Percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + " %"
    
stu1 = Stu(98 , 90, 97)
print(stu1.Percentage)

stu1.phy = 86
print(stu1.Percentage)