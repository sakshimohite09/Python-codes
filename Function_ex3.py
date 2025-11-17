# Write a function to print the elements of a list in a single line. (List is the parameter)

cities = ["Kolhapur","Delhi","Gurgaon","Noida","Mumbai"]

def print_len(list):
    print(len(list))

def print_list(list):
    for i in list:
        print(i, end=" ")

print_len(cities)
print_list(cities)
