"""Write a program to enter marks of 3 subjects from the user and store 
    them in a dictionary. Start with an empty dictionary & add 
    one by one. Use subjects name as key & marks as value."""

marks = {}

x = int(input("Enter physics marks:"))
marks.update({"phy" : x})

x = int(input("Enter chemistry marks:"))
marks.update({"chem" : x})

x = int(input("Enter maths marks:"))
marks.update({"maths" : x})

print(marks)
