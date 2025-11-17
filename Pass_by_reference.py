class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(customer):
    if customer.gender=="male":
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"ma'am")

    cust2 =Customer("Ram","Male")
    return cust2
cust =Customer("Sakshi","female")
greet(cust)

cust =Customer("Krishna","male")
greet(cust)

new_cust =greet(cust)
print(new_cust.name)
    