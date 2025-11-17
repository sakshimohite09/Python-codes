"""Write a function which converts inches to centimeters"""

def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter value in inches: "))
print("Your value in cms is: ",inch_to_cms(n))