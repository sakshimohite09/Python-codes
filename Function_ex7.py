"""
Write a python program using function to convert Celsius to Fahrenheit

Formula = c = 5*(f-32)/9
"""

def cal_f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter temperature in F:"))
print(f"{cal_f_to_c(f)} degree C")