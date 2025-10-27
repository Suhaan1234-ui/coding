with open("p48source.html") as a:
    b=a.readline()
    lineno=0
    while(b!=""):
           lineno+=1
           if("python" in b):
                 print(lineno)
                 break
           b=a.readline()

#or
with open("p48source.html") as a:
    b=a.readline()
    lineno=0
    while(not("python" in b)):
           lineno+=1
           b=a.readline()
    lineno+=1
    print(lineno)
#or
with open("p48source.html") as a:
    b=a.readline()
    lineno=0
    c=False

    while not a :
           lineno+=1
           if("python" in b):
                 print(lineno)
                 c=True
           b=a.readline()
#or


with open("p48source.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")

