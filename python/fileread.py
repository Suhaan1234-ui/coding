a= open("file.txt")   #general syntax is open("filename","mode")
data=a.read()          #default mode is "r" for read (reading a file) , read reads the the code as a 
                       #string
print(data)
a.close()       #closing the file after reading, not necessary but good practice
#or simply
print(open("file.txt").read())
#close is not necessary here as file is closed automatically after reading





#modes: "r"=read, "w"=write, "a"=append, "r+"=read and write
# "rb"=read binary, "wb"=write binary, "ab"=append binary
# "x"=create file, returns error if file exists         