"""Write a function that replaces all occurrences of "Java" with "Python" in "practise.txt" file"""
def replace_data():
    with open("practise.txt","r") as f:
        data = f.read()

    new_data = data.replace("Java","Python")
    print(new_data)

    with open("practise.txt","w") as f:
        f.write(new_data)

replace_data()