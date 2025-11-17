# Write a function to convert USD to INR

def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =" , inr_val,"INR")

convert(100)

# Write a function to find even-odd numbers 

def num():
    number = int(input("Enter a number:"))
    if(number%2==0):
        print("Even")
    else:
        print("Odd")
num()
num()