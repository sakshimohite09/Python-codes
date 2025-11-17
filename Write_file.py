#File I/O 
#Writing a file

#Write = Overwrites the entire file

f = open("demo.txt","w")
f.write("I want to learn Javascript tomorrow...")
f.close()

#Append = adds to the file

c= open("demo.txt","a")
c.write("\nThen i'll move to reactJS")
c.close()

#Creats new file if it doesnot exist

e = open("sak.txt","w")
e.write("Sakshi")
e.close()