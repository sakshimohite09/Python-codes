#Conditional statement
#Clever if / Ternary Operator
# <var> = (false_value, true_value) [<condition>]

age = int(input("Age: "))
vote = ("Yes","No") [age<18]
print(vote)