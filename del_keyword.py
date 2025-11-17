#del_Keyword = Used to delete object properties or object itself

class Stu:
    def __init__(self , name):
        self.name = name

s1 = Stu("Sakshi")
print(s1.name)  #it prints the name

del s1.name
print(s1.name)  #it delete the name object