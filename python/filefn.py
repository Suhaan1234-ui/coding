a=open("file3.txt")
print(a.readlines(), type(a.readlines()))  #reads file line by line and returns a list of lines
a.seek(0)  #to reset the pointer to the beginning of the file
# read one line at a time but store the result before asking its type 
#readline fn stops until an empty string is encountered
line1 = a.readline()
print(line1, type(line1))

line2 = a.readline()
print(line2, type(line2))

line3 = a.readline()
print(line3, type(line3))

line4 = a.readline()
print(line4, type(line4))
print(line4== '') 
'''

print(a.readline(), type(a.readline())) 
print(a.readline(),type(a.readline())) 
print(a.readline(),type(a.readline())) 
print(a.readline(),type(a.readline())  ) 
this is wrong as the pointer has moved ahead after each readline() call ie 2 readline() are called
in each print statement
'''
#or simply
a.seek(0)
line = a.readline()
while(line!=''):
    print(line, type(line))
    line = a.readline()


a.close()
   

    