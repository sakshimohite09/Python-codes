#Product of numbers

def flexi(*num): #Converts num in tuple
    product =1
    print(num) # Gives tuple
    for i in num:
        product = product * i

    print(product)

flexi(1)
flexi(1,2)
flexi(1,2,3,4,5)
flexi(1,2,3,4,5,6,7)