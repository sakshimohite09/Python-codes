"""Create a new file "practise.txt" using python. Add the following data in it.
        Hi everyone
        We are learning file I/O
        Using Java.
        I like programming in Java"""

s =  open("practise.txt","w")
s.write("Hi everyone\nWe are learning file I/O\nUsing Java.\nI like programming in Java")
s.close()