#File I/O 
#Reading a file

#Read = reads entire file

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

print("------------------------------------------------------")

#Readline = Reads one line at a time

c = open("demo.txt","r")
line1 = c.readline()
print(line1)
line2 = c.readline()
print(line2)
c.close()

