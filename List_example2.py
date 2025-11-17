""""Write a program to check if a list contains a palindrome of elements.
    eg.,[1,2,3,2,1]"""

list1 = [1,2,1]
list2 = ["a","b","c"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not palindrome")



copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("Not palindrome")


