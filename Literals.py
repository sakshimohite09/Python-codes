"""Literals = Literal is a raw data given in python, there are 
    various types of literals they are as follows.
    
    Four types of literals:
    1. Numeric literals
    2. String literals
    3. Boolean literals
    4. Special literals"""

print("----------------------------1. Numeric literals---------------------------------")

#Int literals

a = 0b1010  #Binary literals
b = 100     #Decimal literals
c = 0o310   #Octal literals
d = 0x12c   #Hexadecimal literals
print(a, b, c, d)

#Float literals

float_1 = 10.5
float_2 = 1.5e2
float_3 =1.5e-3
print(float_1, float_2, float_3)

#Complex literals

x = 3.14j
print(x, x.imag, x.real)

print("-----------------------------2. String literals--------------------------------")

string = 'Python'
strings = "Python"
char = "C"
multiline_str = """This is a multiline string with more than one line"""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n Python Lang"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

print("-----------------------------3. Boolean literals--------------------------------")

a = True + 4
b = False + 10

print("a:",a)
print("b:",b)

print("-----------------------------4. Special literals--------------------------------")

a = None    #Variable declaration
print(a)