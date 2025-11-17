#Conditional statements
#Traffic light codes

light=(input("light color:"))

if(light =="red" or light =="Red"):
    print("Stop")
elif(light =="yellow" or light =="Yellow"):
    print("Look")
elif(light =="green" or light =="Green"):
    print("Go")
else:
    print("Light is broken")
