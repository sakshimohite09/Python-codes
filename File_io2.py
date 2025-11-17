#With syntax

#Read

with open("demo.txt","r") as f:
    data = f.read()
    print(data)

#Write

with open("demo.txt","w") as c:
    dta = c.write("Name")