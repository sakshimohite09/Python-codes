#File I/O 

#r+

f = open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

#w+

c = open("demo.txt","w+")
print(c.read())
c.write("abc")
c.close()

#a+

e = open("demo.txt","a+")
print(e.read())
e.write("ABC")
e.close()